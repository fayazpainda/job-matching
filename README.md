# LLM-Powered Job Matching System
## Final Project for the "LLM-Assisted Intelligent Decision Application" Course

**Name**: PAINDA MOHAMMAD FAYAZ
**Student ID**: 22511204
**Submission Date**: 2026-06

---

## File Structure

```
Final Project/
├── job_matching.ipynb      # Main deliverable (run this)
├── data/
│   ├── jobs.csv            # Job database (~80 jobs, LinkedIn-style)
│   └── candidates.csv      # Candidate database (~25 candidates)
├── requirements.txt        # Python dependencies
├── .env.example            # API key template
└── README.md               # This file
```

---

## Quick Start

### 1. Install dependencies
```bash
cd ~/Desktop/Final\ Project
pip install -r requirements.txt
```

### 2. Configure Anthropic Claude API Key
1. Sign up / log in at **https://console.anthropic.com/**
2. Create an API key: **https://console.anthropic.com/settings/keys** → "Create Key" → copy `sk-ant-...`
3. Top up: **Settings → Billing** (new accounts usually get free credit, enough for this demo)

```bash
cd ~/Desktop/Final\ Project
cp .env.example .env
open -e .env             # Edit in TextEdit, replace sk-ant-your-key-here with your real key
```

**Test the API key**:
```bash
python3 -c "
import os
from dotenv import load_dotenv
from anthropic import Anthropic
load_dotenv()
c = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
r = c.messages.create(model='claude-opus-4-7', max_tokens=20, messages=[{'role':'user','content':'Reply with: success'}])
print('Claude:', r.content[0].text)
"
```

> If you don't have an API key yet, the notebook still runs — the LLM section shows mock responses.
> **Cost estimate**: ~10 Claude calls for the demo, ~600 tokens each, total ~$0.15 USD.

### 3. Launch Jupyter
```bash
jupyter notebook job_matching.ipynb
```

### 4. Run all cells
`Cell` → `Run All` (or `Shift+Enter` through each cell). The interactive control panel appears in Module 4.

---

## Presentation Notes (10+5 min)

The assignment requires answering 5 questions. Use these as a script:

### 1. What problem are you solving? (Background)
> **Scenario**: HR teams in tech companies need to match candidates to job postings — for campus or social recruiting.
> **Users**: HR, job seekers, recruiting platforms.
> **Goal**: Produce sortable, explainable matches across multiple dimensions (skills, experience, education, location, salary).

### 2. What are the current difficulties?
- **Low efficiency**: HR spends 5-10 minutes per resume comparing to job requirements.
- **Subjective**: Different HR people have different criteria — hard to quantify.
- **Black box**: Traditional ATS systems give a single score with no explanation.
- **Multi-dimensional**: Weights for skills/experience/education/location differ per company, per role.

### 3. Solution approach
**Two-layer combination: rule-based scoring (explainable) + LLM (semantic understanding)**

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Data input  │ -> │ Rule scoring│ -> │ Sort/Display│ -> │ LLM explain │
│ (CSV/UI)    │    │ (4-dim wtd) │    │ (table+chart│    │ (top match) │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                          ^                  ^
                          |                  |
                  ipywidgets live interaction (weights/filters/Top-N)
```

**Why this design?**
- Pure rules: transparent but rigid
- Pure LLM: flexible but black box, expensive, unreliable
- Combined: **rules provide auditable scores; LLM adds semantic explanation and human advice for the top recommendation**

### 4. How is the LLM used?

| Stage | LLM role |
|---|---|
| **Design phase** | Discussed with the LLM how to decompose into "input/analysis/display/recommendation" modules |
| **Code generation** | LLM generated the ipywidgets UI template and the matplotlib dual-view chart |
| **Debugging** | LLM helped debug font display, weight normalization, CSV parsing issues |
| **Runtime (core feature)** | LLM is the **decision-support engine** — generates "highlights / gaps / recommendation" analysis for the top match |
| **Optimization** | LLM suggested giving remote/different-location a 0.3 score (not 0) to preserve remote work options |

**LLM prompt design at runtime**:
- Role setup: *"You are an experienced and concise HR consultant"*
- Structured output: three-section Markdown (✅ highlights / ⚠️ gaps / 💡 recommendation)
- Model: `claude-opus-4-7` (configurable via `LLM_MODEL` env var)
- `max_tokens: 600` to control cost

### 5. How well does it work?

**Live demo flow** (recommended 3-4 min):
1. Pick candidate `Alex Johnson` (Python backend, 5 years)
2. Run with default weights → Top 5 shows Senior Python Backend Engineer jobs at ~90 score
3. Raise the **Location** weight → location-matched jobs jump to top
4. Filter to `San Francisco, CA` only → live filtering
5. Show the Claude-generated "highlights / gaps / recommendation" output
6. Switch candidate to `Harper Scott` (LLM engineer) → Top 1 auto-changes to LLM Engineer roles

**Capabilities demonstrated**:
- Quantitative multi-dimensional matching (4 dimensions + adjustable weights)
- Clean visualization (dual bar charts + global heatmap)
- Live interactivity (9 controls)
- LLM intelligent explanation (natural-language recommendation rationale)

**Limitations and improvements**:
- Skill matching is keyword-level; doesn't recognize React ↔ Vue as related
  → Replace keyword sets with embeddings
- Sample size is limited (~80 jobs, ~25 candidates)
  → Connect to real resume databases and job board APIs
- Every LLM call requires internet, latency 2-5 seconds
  → Cache common combinations; pre-generate in batches
- No learning-feedback loop
  → Let HR rate recommendations, reverse-adjust weights (RL)

---

## Topic-Choice Notes

This project covers the **Job Matching** topic from the assignment's list. The framework adapts easily to other topics (Risk Warning, Inventory Ordering, etc.):
- Replace the CSVs under `data/`
- Adjust the scoring logic in `calculate_match()`
- Update the LLM prompt template
- UI + visualization framework reuses

---

## Self-Assessment

| Assignment Requirement | Status |
|---|---|
| Complete "input → analysis → display → recommendation" app powered by LLM | Modules 1-4 + LLM analysis |
| Python + Jupyter Notebook | `job_matching.ipynb` |
| Use pandas / matplotlib / scikit-learn / ipywidgets | All present |
| Include data input, analysis & decision, results display, parameter interaction | All four modules |
| Not just chat logs, static docs, or non-runnable code | Fully runnable, end-to-end |

---

**Submitted by**: PAINDA MOHAMMAD FAYAZ (Student ID: 22511204)
**Contact**: fayazpainda@mail.dlut.edu.cn
