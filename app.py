import os
import pandas as pd
from flask import Flask, render_template, request, jsonify

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "claude-sonnet-4-6")

client = None
if ANTHROPIC_API_KEY and not ANTHROPIC_API_KEY.startswith("sk-ant-your-"):
    from anthropic import Anthropic
    client = Anthropic(api_key=ANTHROPIC_API_KEY)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
jobs_df = pd.read_csv(os.path.join(BASE_DIR, "data", "jobs.csv"))
candidates_df = pd.read_csv(os.path.join(BASE_DIR, "data", "candidates.csv"))

EDUCATION_LEVELS = {"Associate": 1, "Bachelor": 2, "Master": 3, "PhD": 4}


def parse_skills(s):
    return {x.strip().lower() for x in str(s).split(",") if x.strip()}


def calc_match(candidate, job, weights):
    cand_skills, job_skills = parse_skills(candidate["skills"]), parse_skills(job["required_skills"])
    sk = len(cand_skills & job_skills) / len(job_skills) if job_skills else 0

    ex = 1.0 if candidate["experience_years"] >= job["min_experience"] else candidate["experience_years"] / max(job["min_experience"], 1)

    c_ed, j_ed = EDUCATION_LEVELS.get(candidate["education"], 0), EDUCATION_LEVELS.get(job["education"], 0)
    ed = 1.0 if c_ed >= j_ed else c_ed / max(j_ed, 1)

    cl, jl = candidate["preferred_location"], job["location"]
    lo = 1.0 if cl == jl else (0.7 if "Remote" in (cl, jl) else 0.3)

    tw = sum(weights.values())
    if tw == 0:
        return None
    w = {k: v / tw for k, v in weights.items()}
    total = w["skills"] * sk + w["experience"] * ex + w["education"] * ed + w["location"] * lo
    return {
        "total": round(total * 100, 1),
        "skill": round(sk * 100, 1),
        "experience": round(ex * 100, 1),
        "education": round(ed * 100, 1),
        "location": round(lo * 100, 1),
    }


def llm_explain(candidate, job, scores):
    if client is None:
        return (
            f"**{candidate['name']}** is a strong candidate for **{job['title']}** at **{job['company']}** "
            f"with an overall match score of **{scores['total']}/100**.\n\n"
            f"### Match Highlights\n"
            f"- Skills alignment: {scores['skill']}% of required skills matched\n"
            f"- Experience level: {scores['experience']}% match with {candidate['experience_years']} years of experience\n"
            f"- Education: {scores['education']}% — meets the {job['education']} requirement\n\n"
            f"### Main Gaps\n"
            f"- Location preference ({candidate['preferred_location']}) vs job location ({job['location']}): {scores['location']}% match\n"
            f"- Some required skills may need upskilling\n\n"
            f"### Recommendation\n"
            f"Consider scheduling an interview to assess hands-on proficiency in the specific required technologies.\n\n"
            f"*Connect your Claude API key in `.env` for personalized AI-generated analysis.*"
        )
    prompt = f"""You are an experienced HR consultant. Based on the information below, give a concise job match analysis (under 300 words, in Markdown).

[Candidate] {candidate['name']}
- Skills: {candidate['skills']}
- Years of experience: {candidate['experience_years']}
- Education: {candidate['education']}
- Preferred location: {candidate['preferred_location']}
- Expected salary: ${candidate['expected_salary']:,}
- Self-introduction: {candidate['self_intro']}

[Job] {job['title']} @ {job['company']} ({job['location']})
- Required skills: {job['required_skills']}
- Minimum experience: {job['min_experience']} years
- Education requirement: {job['education']}
- Salary range: ${job['salary_min']:,}-${job['salary_max']:,}
- Description: {job['description']}

[System scores] Total {scores['total']}/100 (Skills {scores['skill']}, Experience {scores['experience']}, Education {scores['education']}, Location {scores['location']})

Output format:
### Match Highlights
(2-3 bullets on where the candidate fits well)

### Main Gaps
(2-3 bullets on weaknesses or risks)

### Recommendation
(One-sentence action recommendation for the HR team or the candidate)"""
    try:
        resp = client.messages.create(
            model=LLM_MODEL, max_tokens=600,
            system="You are an experienced and concise HR consultant.",
            messages=[{"role": "user", "content": prompt}],
        )
        return next((b.text for b in resp.content if b.type == "text"), "")
    except Exception as e:
        return f"Claude API error: {e}"


@app.route("/")
def index():
    cands = []
    for _, c in candidates_df.iterrows():
        cands.append({
            "id": c["candidate_id"], "name": c["name"],
            "education": c["education"], "experience": int(c["experience_years"]),
            "location": c["preferred_location"], "skills": c["skills"],
            "salary": int(c["expected_salary"]), "intro": c["self_intro"],
        })
    locs = sorted(jobs_df["location"].unique().tolist())
    return render_template("index.html", candidates=cands, locations=locs,
                           has_api=client is not None,
                           total_jobs=len(jobs_df), total_candidates=len(candidates_df))


@app.route("/api/match", methods=["POST"])
def match():
    d = request.json
    cand = candidates_df[candidates_df["candidate_id"] == d["candidate_id"]].iloc[0]
    weights = {
        "skills": float(d.get("w_skills", 0.5)),
        "experience": float(d.get("w_experience", 0.2)),
        "education": float(d.get("w_education", 0.15)),
        "location": float(d.get("w_location", 0.15)),
    }
    flocs = d.get("locations", [])
    msal = int(d.get("min_salary", 0))
    topn = int(d.get("top_n", 8))
    query = str(d.get("query", "")).strip().lower()

    filtered = jobs_df.copy()
    if flocs:
        filtered = filtered[filtered["location"].isin(flocs)]
    if msal > 0:
        filtered = filtered[filtered["salary_max"] >= msal]
    if query:
        haystack = (
            filtered["title"].astype(str).str.lower() + " " +
            filtered["company"].astype(str).str.lower() + " " +
            filtered["required_skills"].astype(str).str.lower() + " " +
            filtered["description"].astype(str).str.lower()
        )
        filtered = filtered[haystack.str.contains(query, regex=False, na=False)]
    if len(filtered) == 0:
        return jsonify({"error": "No jobs match the current filters."})

    rows = []
    for _, job in filtered.iterrows():
        s = calc_match(cand, job, weights)
        if not s:
            continue
        rows.append({
            "job_id": job["job_id"], "title": job["title"],
            "company": job["company"], "location": job["location"],
            "salary_min": int(job["salary_min"]), "salary_max": int(job["salary_max"]),
            "required_skills": job["required_skills"], "description": job["description"],
            "education": job["education"], "min_experience": int(job["min_experience"]),
            "total": s["total"], "skill": s["skill"], "experience": s["experience"],
            "education_score": s["education"], "location_score": s["location"],
        })
    rows.sort(key=lambda r: r["total"], reverse=True)
    tw = sum(weights.values())
    norm = {k: round(v / tw * 100) for k, v in weights.items()} if tw else weights
    return jsonify({"results": rows[:topn], "normalized_weights": norm, "total_jobs": len(filtered)})


@app.route("/api/explain", methods=["POST"])
def explain():
    d = request.json
    cand = candidates_df[candidates_df["candidate_id"] == d["candidate_id"]].iloc[0]
    job = jobs_df[jobs_df["job_id"] == d["job_id"]].iloc[0]
    return jsonify({"explanation": llm_explain(cand, job, d["scores"])})


if __name__ == "__main__":
    print("\n  Job Matching System: http://localhost:5001\n")
    app.run(debug=False, host="0.0.0.0", port=5001)
