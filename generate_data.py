import csv
import random

random.seed(42)

COMPANIES = {
    "Google": "Mountain View, CA", "Meta": "Menlo Park, CA", "Apple": "Cupertino, CA",
    "Amazon": "Seattle, WA", "Microsoft": "Redmond, WA", "Netflix": "Los Gatos, CA",
    "Tesla": "Austin, TX", "NVIDIA": "Santa Clara, CA", "Adobe": "San Jose, CA",
    "Salesforce": "San Francisco, CA", "Oracle": "Austin, TX", "IBM": "New York, NY",
    "Intel": "Santa Clara, CA", "Uber": "San Francisco, CA", "Lyft": "San Francisco, CA",
    "Airbnb": "San Francisco, CA", "Stripe": "San Francisco, CA", "Shopify": "Remote",
    "Twitter/X": "San Francisco, CA", "Snap": "Los Angeles, CA",
    "Spotify": "New York, NY", "Pinterest": "San Francisco, CA",
    "LinkedIn": "Sunnyvale, CA", "PayPal": "San Jose, CA", "Block": "San Francisco, CA",
    "Databricks": "San Francisco, CA", "Snowflake": "Bozeman, MT",
    "Palantir": "Denver, CO", "Cloudflare": "San Francisco, CA",
    "MongoDB": "New York, NY", "Elastic": "Remote", "HashiCorp": "San Francisco, CA",
    "Confluent": "Remote", "Twilio": "San Francisco, CA", "Okta": "San Francisco, CA",
    "CrowdStrike": "Austin, TX", "Palo Alto Networks": "Santa Clara, CA",
    "Datadog": "New York, NY", "Figma": "San Francisco, CA", "Canva": "Remote",
    "Notion": "San Francisco, CA", "Vercel": "Remote", "Supabase": "Remote",
    "OpenAI": "San Francisco, CA", "Anthropic": "San Francisco, CA",
    "Mistral AI": "Remote", "Cohere": "Remote", "Hugging Face": "Remote",
    "Scale AI": "San Francisco, CA", "Waymo": "Mountain View, CA",
    "Cruise": "San Francisco, CA", "Rivian": "Irvine, CA",
    "SpaceX": "Hawthorne, CA", "Anduril": "Costa Mesa, CA",
    "Plaid": "San Francisco, CA", "Robinhood": "Menlo Park, CA",
    "Coinbase": "Remote", "Ripple": "San Francisco, CA",
    "DocuSign": "San Francisco, CA", "Zoom": "San Jose, CA",
    "Atlassian": "San Francisco, CA", "GitLab": "Remote",
    "GitHub": "Remote", "JetBrains": "Remote",
    "Red Hat": "Raleigh, NC", "VMware": "Palo Alto, CA",
    "Cisco": "San Jose, CA", "Dell": "Round Rock, TX",
    "Samsung": "San Jose, CA", "Sony": "San Mateo, CA",
    "Qualcomm": "San Diego, CA", "AMD": "Santa Clara, CA",
    "Broadcom": "San Jose, CA", "Arm": "San Jose, CA",
    "Roblox": "San Mateo, CA", "Unity": "San Francisco, CA",
    "Epic Games": "Cary, NC", "Riot Games": "Los Angeles, CA",
    "Activision Blizzard": "Santa Monica, CA",
    "Wise": "Remote", "Brex": "San Francisco, CA",
    "Mercury": "Remote", "Chime": "San Francisco, CA",
    "Affirm": "San Francisco, CA", "Klarna": "Remote",
    "Lucid Motors": "Newark, CA", "Joby Aviation": "Santa Cruz, CA",
    "Form Energy": "Somerville, MA", "QuantumScape": "San Jose, CA",
    "Moderna": "Cambridge, MA", "23andMe": "Sunnyvale, CA",
    "Recursion": "Salt Lake City, UT", "Tempus": "Chicago, IL",
    "Sentry": "San Francisco, CA", "Honeycomb": "Remote",
    "Postman": "San Francisco, CA", "Linear": "Remote",
    "Retool": "San Francisco, CA", "Replit": "San Francisco, CA",
    "DoorDash": "San Francisco, CA", "Instacart": "San Francisco, CA",
    "Wayfair": "Boston, MA", "Etsy": "Brooklyn, NY",
    "Reddit": "San Francisco, CA", "Discord": "San Francisco, CA",
    "Khan Academy": "Mountain View, CA", "Duolingo": "Pittsburgh, PA",
    "Two Sigma": "New York, NY", "Jane Street": "New York, NY",
    "Citadel": "Chicago, IL", "Hudson River Trading": "New York, NY",
}

EXTRA_LOCATIONS = [
    "New York, NY", "Austin, TX", "Seattle, WA", "Boston, MA", "Denver, CO",
    "Chicago, IL", "Los Angeles, CA", "San Francisco, CA", "Remote",
    "Portland, OR", "Atlanta, GA", "Miami, FL", "Dallas, TX", "Phoenix, AZ",
    "San Diego, CA", "Minneapolis, MN", "Nashville, TN", "Raleigh, NC",
    "Washington, DC", "Philadelphia, PA",
]

JOB_TEMPLATES = [
    # Backend
    {"title": "Senior Python Backend Engineer", "skills": "Python,Django,FastAPI,PostgreSQL,Redis,Docker,AWS,Linux", "exp": 5, "edu": "Bachelor", "sal": (170000, 260000)},
    {"title": "Python Backend Developer", "skills": "Python,Flask,PostgreSQL,Docker,Git,REST", "exp": 3, "edu": "Bachelor", "sal": (130000, 195000)},
    {"title": "Java Backend Engineer", "skills": "Java,Spring,SpringBoot,MySQL,Kafka,Redis,Microservices", "exp": 4, "edu": "Bachelor", "sal": (160000, 245000)},
    {"title": "Senior Java Engineer", "skills": "Java,Spring,Hibernate,Kafka,AWS,Docker,Kubernetes", "exp": 6, "edu": "Bachelor", "sal": (180000, 280000)},
    {"title": "Go Backend Engineer", "skills": "Go,gRPC,PostgreSQL,Redis,Kubernetes,Docker", "exp": 3, "edu": "Bachelor", "sal": (155000, 240000)},
    {"title": "Senior Go Developer", "skills": "Go,gRPC,Kafka,PostgreSQL,Kubernetes,Terraform,AWS", "exp": 5, "edu": "Bachelor", "sal": (175000, 270000)},
    {"title": "Node.js Backend Engineer", "skills": "Node.js,Express,TypeScript,MongoDB,Redis,GraphQL", "exp": 3, "edu": "Bachelor", "sal": (140000, 220000)},
    {"title": "Ruby on Rails Engineer", "skills": "Ruby,Rails,PostgreSQL,Sidekiq,Redis,Heroku", "exp": 4, "edu": "Bachelor", "sal": (150000, 235000)},
    {"title": "Rust Systems Engineer", "skills": "Rust,C++,Linux,Networking,Concurrency,Systems", "exp": 4, "edu": "Bachelor", "sal": (170000, 275000)},
    {"title": "C++ Systems Developer", "skills": "C++,STL,Linux,Multithreading,CMake,Performance", "exp": 5, "edu": "Bachelor", "sal": (165000, 260000)},
    {"title": "Scala Backend Engineer", "skills": "Scala,Akka,Kafka,Spark,PostgreSQL,Functional", "exp": 4, "edu": "Master", "sal": (170000, 265000)},
    {"title": "PHP Full Stack Developer", "skills": "PHP,Laravel,MySQL,JavaScript,Vue,Docker", "exp": 3, "edu": "Bachelor", "sal": (110000, 170000)},
    # Frontend
    {"title": "Senior React Frontend Engineer", "skills": "React,TypeScript,Redux,Next.js,CSS,Webpack,Testing", "exp": 5, "edu": "Bachelor", "sal": (165000, 255000)},
    {"title": "React Developer", "skills": "React,JavaScript,TypeScript,HTML,CSS,Redux", "exp": 3, "edu": "Bachelor", "sal": (130000, 200000)},
    {"title": "Vue.js Frontend Engineer", "skills": "Vue,Vuex,JavaScript,TypeScript,HTML,CSS,Webpack", "exp": 3, "edu": "Bachelor", "sal": (125000, 195000)},
    {"title": "Angular Frontend Developer", "skills": "Angular,TypeScript,RxJS,HTML,CSS,NgRx", "exp": 3, "edu": "Bachelor", "sal": (125000, 195000)},
    {"title": "Senior Frontend Architect", "skills": "React,TypeScript,GraphQL,Next.js,Performance,A11y,Design Systems", "exp": 7, "edu": "Bachelor", "sal": (190000, 300000)},
    {"title": "UI Engineer", "skills": "JavaScript,React,CSS,HTML,Figma,Animation,Responsive", "exp": 3, "edu": "Bachelor", "sal": (130000, 205000)},
    # Full Stack
    {"title": "Full Stack Engineer", "skills": "React,Node.js,TypeScript,PostgreSQL,AWS,Docker", "exp": 4, "edu": "Bachelor", "sal": (155000, 245000)},
    {"title": "Senior Full Stack Developer", "skills": "React,Python,Django,PostgreSQL,Redis,AWS,Docker,Kubernetes", "exp": 6, "edu": "Bachelor", "sal": (180000, 280000)},
    {"title": "Full Stack Engineer (MERN)", "skills": "MongoDB,Express,React,Node.js,TypeScript,AWS", "exp": 3, "edu": "Bachelor", "sal": (135000, 210000)},
    # Mobile
    {"title": "iOS Engineer", "skills": "Swift,UIKit,SwiftUI,CoreData,XCode,Combine,MVVM", "exp": 4, "edu": "Bachelor", "sal": (155000, 245000)},
    {"title": "Senior iOS Developer", "skills": "Swift,SwiftUI,Combine,CoreML,ARKit,CI/CD,Testing", "exp": 6, "edu": "Bachelor", "sal": (175000, 275000)},
    {"title": "Android Engineer", "skills": "Kotlin,Jetpack Compose,Android SDK,Room,Coroutines,MVVM", "exp": 4, "edu": "Bachelor", "sal": (150000, 240000)},
    {"title": "Senior Android Developer", "skills": "Kotlin,Jetpack Compose,Dagger,Retrofit,Testing,CI/CD", "exp": 6, "edu": "Bachelor", "sal": (170000, 265000)},
    {"title": "React Native Developer", "skills": "React Native,TypeScript,Redux,REST,Firebase,Mobile", "exp": 3, "edu": "Bachelor", "sal": (130000, 205000)},
    {"title": "Flutter Developer", "skills": "Flutter,Dart,Firebase,REST,Mobile,Git", "exp": 3, "edu": "Bachelor", "sal": (125000, 200000)},
    # Data & ML
    {"title": "Data Scientist", "skills": "Python,Pandas,Scikit-learn,SQL,Statistics,Matplotlib,Jupyter", "exp": 3, "edu": "Master", "sal": (145000, 230000)},
    {"title": "Senior Data Scientist", "skills": "Python,Pandas,TensorFlow,PyTorch,SQL,Statistics,MLOps,Experiment Design", "exp": 6, "edu": "Master", "sal": (180000, 300000)},
    {"title": "Machine Learning Engineer", "skills": "Python,PyTorch,TensorFlow,MLOps,Docker,AWS,Kubernetes,SQL", "exp": 4, "edu": "Master", "sal": (170000, 280000)},
    {"title": "Senior ML Engineer", "skills": "Python,PyTorch,Distributed Training,MLOps,Kubernetes,AWS,C++", "exp": 6, "edu": "Master", "sal": (200000, 350000)},
    {"title": "NLP Engineer", "skills": "Python,PyTorch,Transformers,HuggingFace,NLP,LLM,Fine-tuning", "exp": 4, "edu": "Master", "sal": (175000, 290000)},
    {"title": "Computer Vision Engineer", "skills": "Python,PyTorch,OpenCV,CNNs,Object Detection,3D Vision", "exp": 4, "edu": "Master", "sal": (170000, 275000)},
    {"title": "LLM Engineer", "skills": "Python,PyTorch,Transformers,LangChain,RAG,Fine-tuning,Prompt Engineering", "exp": 3, "edu": "Master", "sal": (185000, 320000)},
    {"title": "AI Research Scientist", "skills": "Python,PyTorch,Math,Statistics,Research,NLP,Reinforcement Learning", "exp": 5, "edu": "PhD", "sal": (200000, 380000)},
    {"title": "Data Analyst", "skills": "Python,SQL,Excel,Tableau,Statistics,Pandas,Data Visualization", "exp": 2, "edu": "Bachelor", "sal": (95000, 150000)},
    {"title": "Senior Data Analyst", "skills": "Python,SQL,Tableau,Power BI,Statistics,ETL,Storytelling", "exp": 5, "edu": "Bachelor", "sal": (130000, 200000)},
    {"title": "Data Engineer", "skills": "Python,SQL,Spark,Airflow,AWS,Kafka,ETL,Data Modeling", "exp": 4, "edu": "Bachelor", "sal": (155000, 250000)},
    {"title": "Senior Data Engineer", "skills": "Python,Spark,Airflow,Kafka,AWS,Terraform,dbt,Data Modeling", "exp": 6, "edu": "Bachelor", "sal": (180000, 290000)},
    {"title": "Analytics Engineer", "skills": "SQL,dbt,Python,Snowflake,Looker,Data Modeling,Git", "exp": 3, "edu": "Bachelor", "sal": (130000, 210000)},
    {"title": "ML Platform Engineer", "skills": "Python,Kubernetes,Docker,MLflow,Airflow,AWS,Terraform", "exp": 5, "edu": "Master", "sal": (180000, 290000)},
    {"title": "Recommendation Systems Engineer", "skills": "Python,PyTorch,Collaborative Filtering,A/B Testing,SQL,Spark", "exp": 4, "edu": "Master", "sal": (170000, 275000)},
    # DevOps & Infra
    {"title": "DevOps Engineer", "skills": "AWS,Terraform,Docker,Kubernetes,CI/CD,Linux,Python,Ansible", "exp": 4, "edu": "Bachelor", "sal": (150000, 240000)},
    {"title": "Senior DevOps Engineer", "skills": "AWS,Terraform,Kubernetes,Helm,ArgoCD,Monitoring,Python,Linux", "exp": 6, "edu": "Bachelor", "sal": (175000, 280000)},
    {"title": "Site Reliability Engineer", "skills": "Python,Go,Kubernetes,AWS,Monitoring,Linux,Terraform,Incident Management", "exp": 5, "edu": "Bachelor", "sal": (170000, 275000)},
    {"title": "Cloud Architect", "skills": "AWS,Azure,GCP,Terraform,Kubernetes,Networking,Security,Architecture", "exp": 7, "edu": "Bachelor", "sal": (190000, 320000)},
    {"title": "Platform Engineer", "skills": "Kubernetes,Docker,Terraform,AWS,Go,CI/CD,Service Mesh", "exp": 4, "edu": "Bachelor", "sal": (160000, 255000)},
    {"title": "Infrastructure Engineer", "skills": "Linux,AWS,Terraform,Ansible,Docker,Networking,Python", "exp": 4, "edu": "Bachelor", "sal": (145000, 235000)},
    # Security
    {"title": "Security Engineer", "skills": "Python,Security,Penetration Testing,AWS,Networking,OWASP,Linux", "exp": 4, "edu": "Bachelor", "sal": (155000, 250000)},
    {"title": "Senior Security Engineer", "skills": "Security,AWS,Kubernetes,IAM,SIEM,Threat Modeling,Compliance,Python", "exp": 6, "edu": "Bachelor", "sal": (180000, 300000)},
    {"title": "Application Security Engineer", "skills": "Security,OWASP,Code Review,Python,SAST,DAST,Threat Modeling", "exp": 4, "edu": "Bachelor", "sal": (160000, 260000)},
    # QA
    {"title": "QA Automation Engineer", "skills": "Python,Selenium,Pytest,CI/CD,API Testing,SQL,Git", "exp": 3, "edu": "Bachelor", "sal": (110000, 175000)},
    {"title": "Senior QA Engineer", "skills": "Python,Selenium,Cypress,Playwright,CI/CD,Performance Testing,API Testing", "exp": 5, "edu": "Bachelor", "sal": (140000, 220000)},
    {"title": "SDET", "skills": "Java,Selenium,TestNG,REST,CI/CD,Docker,API Testing", "exp": 4, "edu": "Bachelor", "sal": (135000, 215000)},
    # Product & Design
    {"title": "Product Manager", "skills": "Product Strategy,Analytics,SQL,A/B Testing,Roadmapping,Agile", "exp": 5, "edu": "Bachelor", "sal": (160000, 260000)},
    {"title": "Senior Product Manager", "skills": "Product Strategy,Analytics,SQL,Stakeholder Management,Vision,GTM", "exp": 7, "edu": "Bachelor", "sal": (190000, 310000)},
    {"title": "Technical Program Manager", "skills": "Program Management,Agile,Cross-functional,Risk Management,Technical", "exp": 6, "edu": "Bachelor", "sal": (170000, 270000)},
    {"title": "UX Designer", "skills": "Figma,User Research,Prototyping,Design Systems,Wireframing,A11y", "exp": 3, "edu": "Bachelor", "sal": (120000, 190000)},
    {"title": "Senior UX Designer", "skills": "Figma,User Research,Design Systems,Prototyping,Leadership,Strategy", "exp": 6, "edu": "Bachelor", "sal": (160000, 255000)},
    {"title": "Product Designer", "skills": "Figma,UI,UX,Prototyping,Design Systems,User Research", "exp": 4, "edu": "Bachelor", "sal": (140000, 225000)},
    # Blockchain & Web3
    {"title": "Blockchain Engineer", "skills": "Solidity,Ethereum,Web3.js,Smart Contracts,DeFi,Node.js", "exp": 3, "edu": "Bachelor", "sal": (160000, 280000)},
    {"title": "Smart Contract Developer", "skills": "Solidity,Hardhat,Foundry,EVM,Security,Auditing,TypeScript", "exp": 4, "edu": "Bachelor", "sal": (170000, 300000)},
    # Embedded & Hardware
    {"title": "Embedded Systems Engineer", "skills": "C,C++,RTOS,ARM,Linux,Hardware,Firmware", "exp": 4, "edu": "Bachelor", "sal": (140000, 225000)},
    {"title": "FPGA Engineer", "skills": "VHDL,Verilog,FPGA,Xilinx,Signal Processing,C++", "exp": 4, "edu": "Master", "sal": (150000, 245000)},
    {"title": "Robotics Software Engineer", "skills": "C++,Python,ROS,Computer Vision,SLAM,Linux,Control Systems", "exp": 4, "edu": "Master", "sal": (160000, 260000)},
    # Leadership / Senior IC
    {"title": "Engineering Manager (Backend)", "skills": "Python,Go,Leadership,Hiring,Architecture,Mentorship,Agile,Roadmapping", "exp": 8, "edu": "Bachelor", "sal": (210000, 320000)},
    {"title": "Engineering Manager (Frontend)", "skills": "React,TypeScript,Leadership,Mentorship,Architecture,Design Systems,Hiring", "exp": 8, "edu": "Bachelor", "sal": (205000, 310000)},
    {"title": "Staff Software Engineer", "skills": "Architecture,Distributed Systems,Mentorship,Go,Python,Design Docs,Leadership", "exp": 9, "edu": "Bachelor", "sal": (230000, 360000)},
    {"title": "Principal Engineer", "skills": "Architecture,Systems Design,Mentorship,Strategy,Cross-team,Leadership", "exp": 12, "edu": "Bachelor", "sal": (270000, 420000)},
    {"title": "Director of Engineering", "skills": "Leadership,Strategy,Hiring,Org Design,Roadmapping,Cross-functional,Budgeting", "exp": 12, "edu": "Bachelor", "sal": (280000, 450000)},
    # Gaming
    {"title": "Game Engine Programmer", "skills": "C++,Unreal,Graphics,Math,Performance,Multithreading,Physics", "exp": 4, "edu": "Bachelor", "sal": (160000, 250000)},
    {"title": "Game Server Engineer", "skills": "Go,C++,Networking,Distributed Systems,Linux,Multiplayer,Performance", "exp": 4, "edu": "Bachelor", "sal": (155000, 245000)},
    {"title": "Gameplay Programmer (Unity)", "skills": "C#,Unity,Game Design,Animation,Physics,Mobile,Testing", "exp": 3, "edu": "Bachelor", "sal": (130000, 200000)},
    {"title": "Graphics Engineer", "skills": "C++,HLSL,GLSL,Vulkan,DirectX,Graphics,Math,Performance", "exp": 5, "edu": "Bachelor", "sal": (175000, 280000)},
    # Quant / Trading
    {"title": "Quantitative Developer", "skills": "C++,Python,Low Latency,Linux,FIX,Networking,Algorithms,Math", "exp": 4, "edu": "Master", "sal": (200000, 380000)},
    {"title": "Quant Researcher", "skills": "Python,Statistics,Math,Machine Learning,Time Series,R,Backtesting", "exp": 4, "edu": "PhD", "sal": (220000, 420000)},
    {"title": "HFT Engineer", "skills": "C++,Linux,Networking,Kernel,FPGA,Performance,Latency", "exp": 5, "edu": "Bachelor", "sal": (240000, 450000)},
    # Bio / Climate
    {"title": "Bioinformatics Engineer", "skills": "Python,R,Genomics,Pandas,Snakemake,AWS,Biology,Statistics", "exp": 3, "edu": "Master", "sal": (140000, 220000)},
    {"title": "Computational Biologist", "skills": "Python,R,Bioinformatics,Statistics,Machine Learning,Biology,Genomics", "exp": 4, "edu": "PhD", "sal": (155000, 250000)},
    {"title": "Climate Tech Software Engineer", "skills": "Python,GIS,Geospatial,PostgreSQL,AWS,Data Pipelines,Numerical Computing", "exp": 4, "edu": "Bachelor", "sal": (150000, 230000)},
    # Autonomous / Mapping
    {"title": "Autonomous Vehicle Engineer", "skills": "C++,Python,ROS,Perception,SLAM,Sensor Fusion,Linux,Math", "exp": 4, "edu": "Master", "sal": (175000, 285000)},
    {"title": "Mapping Engineer", "skills": "Python,C++,GIS,Geospatial,Geometry,PostGIS,Point Clouds,Algorithms", "exp": 4, "edu": "Bachelor", "sal": (155000, 235000)},
    # Platform / Infra deep
    {"title": "Database Engineer", "skills": "PostgreSQL,MySQL,Query Optimization,Replication,Linux,Performance,Backup", "exp": 5, "edu": "Bachelor", "sal": (165000, 255000)},
    {"title": "Distributed Systems Engineer", "skills": "Go,Rust,Consensus,Raft,Distributed,Linux,Networking,Storage", "exp": 6, "edu": "Bachelor", "sal": (190000, 300000)},
    {"title": "Compiler Engineer", "skills": "C++,LLVM,Rust,Compilers,Code Generation,Optimization,Linux", "exp": 5, "edu": "Master", "sal": (180000, 290000)},
    {"title": "Kernel Engineer", "skills": "C,Linux Kernel,eBPF,Drivers,Performance,Debugging,Networking", "exp": 6, "edu": "Bachelor", "sal": (190000, 305000)},
    {"title": "Build & Release Engineer", "skills": "Bazel,Make,CI/CD,Jenkins,Python,Linux,Containers,Monorepo", "exp": 4, "edu": "Bachelor", "sal": (145000, 220000)},
    {"title": "API Platform Engineer", "skills": "Go,Python,gRPC,OpenAPI,GraphQL,Auth,Rate Limiting,Observability", "exp": 4, "edu": "Bachelor", "sal": (160000, 240000)},
    # Emerging tech
    {"title": "AR/VR Engineer", "skills": "C++,Unity,Unreal,3D Graphics,Spatial Computing,Math,SDK", "exp": 4, "edu": "Bachelor", "sal": (165000, 260000)},
    {"title": "Computer Graphics Researcher", "skills": "C++,GLSL,HLSL,Math,Rendering,Ray Tracing,Real-time Graphics", "exp": 5, "edu": "PhD", "sal": (190000, 310000)},
    {"title": "Audio DSP Engineer", "skills": "C++,DSP,Audio,Signal Processing,Math,SIMD,Real-time", "exp": 5, "edu": "Master", "sal": (165000, 255000)},
    {"title": "Quantum Computing Engineer", "skills": "Python,Qiskit,Cirq,Linear Algebra,Physics,Math,Quantum Algorithms", "exp": 4, "edu": "PhD", "sal": (170000, 280000)},
    # DevRel / Customer-facing
    {"title": "Developer Advocate", "skills": "Public Speaking,Technical Writing,Python,JavaScript,Demos,Community,Conferences", "exp": 4, "edu": "Bachelor", "sal": (140000, 215000)},
    {"title": "Solutions Engineer", "skills": "Python,APIs,SQL,Communication,Pre-sales,Demos,Architecture,Customer Success", "exp": 4, "edu": "Bachelor", "sal": (145000, 225000)},
    {"title": "Forward Deployed Engineer", "skills": "Python,SQL,Data Pipelines,Customer-facing,Communication,Travel,Problem Solving", "exp": 3, "edu": "Bachelor", "sal": (155000, 240000)},
    # More frontend / fullstack variety
    {"title": "WebGL / 3D Engineer", "skills": "JavaScript,TypeScript,Three.js,WebGL,WebGPU,Math,Performance,Shaders", "exp": 4, "edu": "Bachelor", "sal": (155000, 240000)},
    {"title": "Design Engineer", "skills": "React,TypeScript,CSS,Figma,Animation,Design Systems,Storybook,A11y", "exp": 4, "edu": "Bachelor", "sal": (155000, 235000)},
    {"title": "Senior PostgreSQL DBA", "skills": "PostgreSQL,Linux,Backup,Replication,pgBouncer,Performance,Monitoring,SQL", "exp": 6, "edu": "Bachelor", "sal": (175000, 270000)},
]

DESCRIPTIONS = {
    "Backend": "Design and build scalable backend services, optimize APIs for performance and reliability, and contribute to system architecture decisions.",
    "Frontend": "Build responsive, accessible user interfaces with modern frameworks, collaborate with design teams, and optimize web performance.",
    "Full Stack": "Work across the stack to deliver features end-to-end, from database design to pixel-perfect UIs, in a fast-paced agile environment.",
    "Mobile": "Develop and maintain high-quality mobile applications, implement new features, and ensure smooth app performance across devices.",
    "Data": "Analyze large datasets to derive actionable insights, build dashboards and reports, and collaborate with product teams on data-driven decisions.",
    "ML": "Design and implement machine learning models, build training pipelines, deploy models to production, and improve model performance iteratively.",
    "AI": "Push the boundaries of AI research, publish papers, develop novel architectures, and translate research into production systems.",
    "LLM": "Build and fine-tune large language models, develop RAG systems, optimize inference, and integrate LLM capabilities into products.",
    "DevOps": "Build and maintain CI/CD pipelines, manage cloud infrastructure, ensure system reliability, and automate operational tasks.",
    "SRE": "Ensure service reliability at scale, manage incident response, build monitoring and alerting systems, and drive reliability culture.",
    "Security": "Identify and mitigate security vulnerabilities, conduct security reviews, build security tooling, and respond to security incidents.",
    "QA": "Design and implement test automation frameworks, write comprehensive test suites, and ensure product quality through rigorous testing.",
    "Product": "Define product vision and strategy, prioritize features based on data, collaborate with engineering and design, and drive product execution.",
    "Design": "Create intuitive user experiences, build design systems, conduct user research, and collaborate closely with engineering teams.",
    "Blockchain": "Develop and audit smart contracts, build decentralized applications, and contribute to protocol design and security.",
    "Systems": "Optimize systems for performance and reliability, work on low-level software, and solve complex distributed systems challenges.",
    "Embedded": "Develop firmware and embedded software for hardware products, optimize for power and performance, and debug hardware-software interfaces.",
    "Leadership": "Lead and grow a high-performing engineering team, drive technical direction, partner with product and design, and own hiring and mentorship.",
    "StaffIC": "Operate as a senior individual contributor across teams: drive architectural decisions, mentor engineers, and own large multi-quarter initiatives.",
    "Gaming": "Build the systems behind immersive gameplay — engine, networking, or graphics — and ship features that millions of players experience daily.",
    "Quant": "Design low-latency systems and quantitative strategies for live markets, balancing performance, risk, and statistical rigor.",
    "Bio": "Combine software engineering with biology to analyze experimental data, build pipelines for sequencing or drug discovery, and accelerate scientific work.",
    "Climate": "Build software that addresses climate change — from geospatial analytics to grid optimization — partnering closely with domain experts.",
    "AV": "Build perception, planning, or mapping systems that move autonomous vehicles toward safe, large-scale deployment.",
    "Graphics": "Push the state of the art in real-time rendering: shaders, ray tracing, and GPU pipelines that ship in millions of devices.",
    "DevRel": "Engage developers through writing, talks, and demos; turn user feedback into product priorities and grow a thriving community.",
    "Solutions": "Partner with customers to integrate, deploy, and extend the product; translate ambiguous business needs into working technical solutions.",
}

def get_desc(title):
    t = title.lower()
    if "engineering manager" in t or "director" in t: return DESCRIPTIONS["Leadership"]
    if "staff" in t or "principal" in t: return DESCRIPTIONS["StaffIC"]
    if "game" in t or "graphics" in t and ("research" not in t): return DESCRIPTIONS["Gaming"]
    if "quant" in t or "hft" in t or "trading" in t: return DESCRIPTIONS["Quant"]
    if "bio" in t: return DESCRIPTIONS["Bio"]
    if "climate" in t: return DESCRIPTIONS["Climate"]
    if "autonomous" in t or "mapping" in t: return DESCRIPTIONS["AV"]
    if "ar/vr" in t or "compiler" in t or "kernel" in t: return DESCRIPTIONS["Systems"]
    if "developer advocate" in t or "devrel" in t: return DESCRIPTIONS["DevRel"]
    if "solutions engineer" in t or "forward deployed" in t: return DESCRIPTIONS["Solutions"]
    if "llm" in t or "nlp" in t: return DESCRIPTIONS["LLM"]
    if "ml" in t or "machine learning" in t or "recommendation" in t: return DESCRIPTIONS["ML"]
    if "ai" in t or "research" in t or "vision" in t: return DESCRIPTIONS["AI"]
    if "data scientist" in t or "data analyst" in t or "analytics" in t: return DESCRIPTIONS["Data"]
    if "data engineer" in t: return DESCRIPTIONS["DevOps"]
    if "frontend" in t or "react" in t or "vue" in t or "angular" in t or "ui engineer" in t or "design engineer" in t or "webgl" in t: return DESCRIPTIONS["Frontend"]
    if "full stack" in t or "mern" in t: return DESCRIPTIONS["Full Stack"]
    if "ios" in t or "android" in t or "mobile" in t or "flutter" in t or "react native" in t: return DESCRIPTIONS["Mobile"]
    if "devops" in t or "platform" in t or "infrastructure" in t or "cloud" in t or "build & release" in t: return DESCRIPTIONS["DevOps"]
    if "sre" in t or "reliability" in t: return DESCRIPTIONS["SRE"]
    if "security" in t: return DESCRIPTIONS["Security"]
    if "qa" in t or "sdet" in t or "automation" in t: return DESCRIPTIONS["QA"]
    if "product manager" in t or "program manager" in t: return DESCRIPTIONS["Product"]
    if "designer" in t or "ux" in t: return DESCRIPTIONS["Design"]
    if "blockchain" in t or "smart contract" in t: return DESCRIPTIONS["Blockchain"]
    if "embedded" in t or "fpga" in t or "robotics" in t or "firmware" in t: return DESCRIPTIONS["Embedded"]
    if "rust" in t or "c++" in t or "systems" in t or "distributed" in t or "database" in t or "dba" in t: return DESCRIPTIONS["Systems"]
    return DESCRIPTIONS["Backend"]

# Generate jobs
jobs = []
jid = 1
companies_list = list(COMPANIES.items())
for template in JOB_TEMPLATES:
    n_postings = random.randint(8, 14)
    chosen_companies = random.sample(companies_list, min(n_postings, len(companies_list)))
    for company_name, hq_loc in chosen_companies:
        loc = random.choice([hq_loc, random.choice(EXTRA_LOCATIONS)]) if random.random() > 0.4 else hq_loc
        sal_min = template["sal"][0] + random.randint(-15000, 15000)
        sal_max = template["sal"][1] + random.randint(-15000, 15000)
        sal_min = max(sal_min, 60000)
        sal_max = max(sal_max, sal_min + 30000)
        exp = template["exp"] + random.choice([-1, 0, 0, 0, 1])
        exp = max(exp, 0)
        jobs.append({
            "job_id": f"J{jid:04d}",
            "title": template["title"],
            "company": company_name,
            "location": loc,
            "required_skills": template["skills"],
            "min_experience": exp,
            "education": template["edu"],
            "salary_min": sal_min,
            "salary_max": sal_max,
            "description": get_desc(template["title"]),
        })
        jid += 1

random.shuffle(jobs)
print(f"Generated {len(jobs)} jobs")

# Generate candidates
FIRST_NAMES = [
    "James","Mary","Robert","Patricia","John","Jennifer","Michael","Linda","David","Elizabeth",
    "William","Barbara","Richard","Susan","Joseph","Jessica","Thomas","Sarah","Christopher","Karen",
    "Charles","Lisa","Daniel","Nancy","Matthew","Betty","Anthony","Margaret","Mark","Sandra",
    "Andrew","Ashley","Joshua","Kimberly","Kenneth","Emily","Kevin","Donna","Brian","Michelle",
    "George","Carol","Timothy","Amanda","Ronald","Dorothy","Jason","Melissa","Edward","Deborah",
    "Ryan","Stephanie","Jacob","Rebecca","Gary","Sharon","Nicholas","Laura","Eric","Cynthia",
    "Jonathan","Kathleen","Stephen","Amy","Larry","Angela","Justin","Shirley","Scott","Brenda",
    "Brandon","Emma","Benjamin","Anna","Samuel","Pamela","Raymond","Nicole","Gregory","Samantha",
    "Alexander","Katherine","Patrick","Christine","Frank","Debra","Jack","Rachel","Dennis","Carolyn",
    "Jerry","Janet","Tyler","Catherine","Aaron","Maria","Jose","Heather","Nathan","Diane",
    "Wei","Priya","Raj","Yuki","Min","Sanjay","Aisha","Omar","Fatima","Ahmed",
    "Hiroshi","Mei","Arjun","Nadia","Carlos","Sofia","Diego","Valentina","Marco","Giulia",
]
LAST_NAMES = [
    "Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez",
    "Hernandez","Lopez","Gonzalez","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin",
    "Lee","Perez","Thompson","White","Harris","Sanchez","Clark","Ramirez","Lewis","Robinson",
    "Walker","Young","Allen","King","Wright","Scott","Torres","Nguyen","Hill","Flores",
    "Green","Adams","Nelson","Baker","Hall","Rivera","Campbell","Mitchell","Carter","Roberts",
    "Chen","Wang","Zhang","Li","Liu","Park","Kim","Patel","Singh","Kumar",
    "Tanaka","Yamamoto","Sato","Müller","Schmidt","Weber","Rossi","Ferrari","Santos","Silva",
]

CANDIDATE_PROFILES = [
    {"skills": "Python,Django,FastAPI,PostgreSQL,Redis,Docker,AWS,Linux", "title_hint": "Python Backend", "sal_range": (150000, 210000)},
    {"skills": "Python,Flask,PostgreSQL,Docker,Git,REST,CI/CD", "title_hint": "Python Backend", "sal_range": (110000, 160000)},
    {"skills": "Java,Spring,SpringBoot,MySQL,Kafka,Redis,Microservices", "title_hint": "Java Backend", "sal_range": (150000, 220000)},
    {"skills": "Java,Spring,Hibernate,MySQL,Docker,Git", "title_hint": "Java Backend", "sal_range": (90000, 130000)},
    {"skills": "Go,gRPC,PostgreSQL,Redis,Kubernetes,Docker,AWS", "title_hint": "Go Backend", "sal_range": (160000, 230000)},
    {"skills": "Go,gRPC,PostgreSQL,Docker,Git,REST", "title_hint": "Go Backend", "sal_range": (120000, 170000)},
    {"skills": "Node.js,Express,TypeScript,MongoDB,Redis,GraphQL,React", "title_hint": "Full Stack Node.js", "sal_range": (130000, 185000)},
    {"skills": "Node.js,Express,TypeScript,MongoDB,AWS,Docker", "title_hint": "Node.js Backend", "sal_range": (120000, 170000)},
    {"skills": "Ruby,Rails,PostgreSQL,Sidekiq,Redis,Heroku,JavaScript", "title_hint": "Ruby Rails", "sal_range": (140000, 200000)},
    {"skills": "Rust,C++,Linux,Networking,Concurrency,Systems,Performance", "title_hint": "Systems", "sal_range": (170000, 240000)},
    {"skills": "C++,STL,Linux,Multithreading,CMake,Performance,Debugging", "title_hint": "C++ Systems", "sal_range": (160000, 230000)},
    {"skills": "React,TypeScript,Redux,Next.js,CSS,Webpack,Testing,GraphQL", "title_hint": "Senior React Frontend", "sal_range": (160000, 225000)},
    {"skills": "React,JavaScript,TypeScript,HTML,CSS,Redux,REST", "title_hint": "React Frontend", "sal_range": (120000, 175000)},
    {"skills": "Vue,Vuex,JavaScript,TypeScript,HTML,CSS,Webpack,Pinia", "title_hint": "Vue Frontend", "sal_range": (115000, 165000)},
    {"skills": "Angular,TypeScript,RxJS,HTML,CSS,NgRx,Testing", "title_hint": "Angular Frontend", "sal_range": (120000, 170000)},
    {"skills": "React,Node.js,TypeScript,PostgreSQL,AWS,Docker,GraphQL", "title_hint": "Full Stack", "sal_range": (145000, 210000)},
    {"skills": "React,Python,Django,PostgreSQL,Redis,AWS,Docker", "title_hint": "Full Stack", "sal_range": (155000, 225000)},
    {"skills": "Swift,UIKit,SwiftUI,CoreData,Combine,MVVM,XCode", "title_hint": "iOS Developer", "sal_range": (150000, 215000)},
    {"skills": "Swift,SwiftUI,Combine,CoreML,ARKit,CI/CD,Testing", "title_hint": "Senior iOS", "sal_range": (170000, 240000)},
    {"skills": "Kotlin,Jetpack Compose,Android SDK,Room,Coroutines,MVVM", "title_hint": "Android Developer", "sal_range": (140000, 205000)},
    {"skills": "React Native,TypeScript,Redux,REST,Firebase,Mobile,Git", "title_hint": "React Native Mobile", "sal_range": (120000, 175000)},
    {"skills": "Flutter,Dart,Firebase,REST,Mobile,Git,CI/CD", "title_hint": "Flutter Mobile", "sal_range": (115000, 170000)},
    {"skills": "Python,Pandas,Scikit-learn,SQL,Statistics,Matplotlib,Jupyter,R", "title_hint": "Data Scientist", "sal_range": (130000, 195000)},
    {"skills": "Python,PyTorch,TensorFlow,MLOps,Docker,AWS,Kubernetes,SQL", "title_hint": "ML Engineer", "sal_range": (165000, 245000)},
    {"skills": "Python,PyTorch,Transformers,HuggingFace,NLP,LLM,Fine-tuning,RAG", "title_hint": "NLP/LLM Engineer", "sal_range": (175000, 260000)},
    {"skills": "Python,PyTorch,OpenCV,CNNs,Object Detection,3D Vision,C++", "title_hint": "Computer Vision", "sal_range": (160000, 235000)},
    {"skills": "Python,PyTorch,Transformers,LangChain,RAG,Fine-tuning,Prompt Engineering,Vector DB", "title_hint": "LLM Engineer", "sal_range": (180000, 270000)},
    {"skills": "Python,PyTorch,Math,Statistics,Research,NLP,Reinforcement Learning,Publishing", "title_hint": "AI Research", "sal_range": (190000, 300000)},
    {"skills": "Python,SQL,Excel,Tableau,Statistics,Pandas,Data Visualization,Power BI", "title_hint": "Data Analyst", "sal_range": (85000, 130000)},
    {"skills": "Python,SQL,Spark,Airflow,AWS,Kafka,ETL,Data Modeling,dbt", "title_hint": "Data Engineer", "sal_range": (150000, 225000)},
    {"skills": "SQL,dbt,Python,Snowflake,Looker,Data Modeling,Git,Analytics", "title_hint": "Analytics Engineer", "sal_range": (120000, 185000)},
    {"skills": "AWS,Terraform,Docker,Kubernetes,CI/CD,Linux,Python,Ansible,Monitoring", "title_hint": "DevOps Engineer", "sal_range": (145000, 215000)},
    {"skills": "AWS,Terraform,Kubernetes,Helm,ArgoCD,Monitoring,Python,Linux,Go", "title_hint": "Senior DevOps", "sal_range": (170000, 250000)},
    {"skills": "Python,Go,Kubernetes,AWS,Monitoring,Linux,Terraform,Incident Management", "title_hint": "SRE", "sal_range": (165000, 240000)},
    {"skills": "AWS,Azure,GCP,Terraform,Kubernetes,Networking,Security,Architecture", "title_hint": "Cloud Architect", "sal_range": (185000, 280000)},
    {"skills": "Python,Security,Penetration Testing,AWS,Networking,OWASP,Linux,Compliance", "title_hint": "Security Engineer", "sal_range": (150000, 220000)},
    {"skills": "Python,Selenium,Pytest,CI/CD,API Testing,SQL,Git,Postman", "title_hint": "QA Engineer", "sal_range": (100000, 155000)},
    {"skills": "Product Strategy,Analytics,SQL,A/B Testing,Roadmapping,Agile,Communication", "title_hint": "Product Manager", "sal_range": (155000, 230000)},
    {"skills": "Figma,User Research,Prototyping,Design Systems,Wireframing,A11y,Sketch", "title_hint": "UX Designer", "sal_range": (115000, 175000)},
    {"skills": "Figma,UI,UX,Prototyping,Design Systems,User Research,Visual Design", "title_hint": "Product Designer", "sal_range": (135000, 200000)},
    {"skills": "Solidity,Ethereum,Web3.js,Smart Contracts,DeFi,Node.js,Hardhat", "title_hint": "Blockchain Engineer", "sal_range": (155000, 245000)},
    {"skills": "C,C++,RTOS,ARM,Linux,Hardware,Firmware,Embedded", "title_hint": "Embedded Systems", "sal_range": (130000, 200000)},
    {"skills": "C++,Python,ROS,Computer Vision,SLAM,Linux,Control Systems", "title_hint": "Robotics Engineer", "sal_range": (155000, 230000)},
    {"skills": "Scala,Akka,Kafka,Spark,PostgreSQL,Functional,JVM", "title_hint": "Scala Backend", "sal_range": (160000, 235000)},
    {"skills": "PHP,Laravel,MySQL,JavaScript,Vue,Docker,REST,Redis", "title_hint": "PHP Full Stack", "sal_range": (100000, 155000)},
    {"skills": "Python,Kubernetes,Docker,MLflow,Airflow,AWS,Terraform,MLOps", "title_hint": "ML Platform", "sal_range": (170000, 250000)},
    {"skills": "Python,PyTorch,Collaborative Filtering,A/B Testing,SQL,Spark,RecSys", "title_hint": "RecSys Engineer", "sal_range": (165000, 240000)},
    {"skills": "Python,Pandas,TensorFlow,PyTorch,SQL,Statistics,MLOps,Experiment Design", "title_hint": "Senior Data Scientist", "sal_range": (175000, 260000)},
    {"skills": "VHDL,Verilog,FPGA,Xilinx,Signal Processing,C++,SystemVerilog", "title_hint": "FPGA Engineer", "sal_range": (145000, 215000)},
    {"skills": "Python,Spark,Airflow,Kafka,AWS,Terraform,dbt,Data Modeling,Snowflake", "title_hint": "Senior Data Engineer", "sal_range": (175000, 260000)},
    # --- Additional profiles for more candidates ---
    {"skills": "Python,Django,PostgreSQL,Celery,Redis,Docker,REST,Git", "title_hint": "Python Backend", "sal_range": (125000, 180000)},
    {"skills": "Python,FastAPI,PostgreSQL,Docker,AWS,Microservices,CI/CD", "title_hint": "Python Microservices", "sal_range": (140000, 205000)},
    {"skills": "Java,Spring,SpringBoot,PostgreSQL,Docker,Kubernetes,AWS", "title_hint": "Java Cloud", "sal_range": (155000, 230000)},
    {"skills": "Java,Spring,MySQL,Kafka,Docker,Monitoring,Linux", "title_hint": "Java Platform", "sal_range": (135000, 200000)},
    {"skills": "Go,PostgreSQL,Kubernetes,Docker,Terraform,CI/CD,Monitoring", "title_hint": "Go Platform", "sal_range": (150000, 220000)},
    {"skills": "Node.js,TypeScript,PostgreSQL,Redis,Docker,AWS,GraphQL,React", "title_hint": "Node.js Full Stack", "sal_range": (140000, 200000)},
    {"skills": "Node.js,Express,MongoDB,Socket.io,TypeScript,Docker,Redis", "title_hint": "Node.js Realtime", "sal_range": (125000, 180000)},
    {"skills": "Ruby,Rails,PostgreSQL,Redis,JavaScript,React,Heroku", "title_hint": "Rails Full Stack", "sal_range": (130000, 190000)},
    {"skills": "Rust,WebAssembly,Linux,Performance,Systems,Networking", "title_hint": "Rust Systems", "sal_range": (165000, 245000)},
    {"skills": "C++,Python,Linux,Algorithms,Data Structures,Performance,Concurrency", "title_hint": "C++ Performance", "sal_range": (155000, 235000)},
    {"skills": "React,TypeScript,Next.js,TailwindCSS,GraphQL,Testing,Storybook", "title_hint": "React Frontend", "sal_range": (140000, 210000)},
    {"skills": "React,JavaScript,CSS,HTML,Redux,Webpack,Performance,A11y", "title_hint": "Frontend", "sal_range": (115000, 170000)},
    {"skills": "Vue,TypeScript,Nuxt.js,Pinia,TailwindCSS,Testing", "title_hint": "Vue Frontend", "sal_range": (120000, 180000)},
    {"skills": "Angular,TypeScript,RxJS,NgRx,Material,Testing,CI/CD", "title_hint": "Angular Enterprise", "sal_range": (130000, 195000)},
    {"skills": "React,TypeScript,Three.js,WebGL,Canvas,Animation,Performance", "title_hint": "Creative Frontend", "sal_range": (145000, 215000)},
    {"skills": "React,Node.js,PostgreSQL,Docker,AWS,TypeScript,CI/CD,Redis", "title_hint": "Full Stack", "sal_range": (150000, 220000)},
    {"skills": "Python,Django,React,PostgreSQL,AWS,Docker,REST", "title_hint": "Full Stack Python", "sal_range": (140000, 210000)},
    {"skills": "Swift,SwiftUI,UIKit,CoreData,Combine,Testing,CI/CD,Firebase", "title_hint": "iOS Developer", "sal_range": (155000, 225000)},
    {"skills": "Kotlin,Android SDK,Jetpack,Room,Retrofit,MVVM,Testing,CI/CD", "title_hint": "Android Developer", "sal_range": (145000, 215000)},
    {"skills": "React Native,TypeScript,Redux,Navigation,Firebase,Jest,Detox", "title_hint": "React Native", "sal_range": (125000, 185000)},
    {"skills": "Flutter,Dart,Provider,Firebase,REST,Testing,CI/CD,Git", "title_hint": "Flutter Developer", "sal_range": (120000, 180000)},
    {"skills": "Python,Pandas,NumPy,SQL,Scikit-learn,Matplotlib,Statistics,A/B Testing", "title_hint": "Data Scientist", "sal_range": (125000, 190000)},
    {"skills": "Python,TensorFlow,Keras,SQL,Pandas,Feature Engineering,MLOps", "title_hint": "ML Engineer", "sal_range": (155000, 235000)},
    {"skills": "Python,PyTorch,Transformers,LLM,RLHF,Distributed Training,CUDA", "title_hint": "LLM Research", "sal_range": (190000, 310000)},
    {"skills": "Python,PyTorch,GANs,Diffusion Models,Computer Vision,CUDA,Math", "title_hint": "Generative AI", "sal_range": (180000, 290000)},
    {"skills": "Python,SQL,Tableau,Power BI,Excel,Statistics,Storytelling,Dashboards", "title_hint": "Business Analyst", "sal_range": (90000, 140000)},
    {"skills": "Python,SQL,Spark,Kafka,Flink,AWS,Streaming,Data Pipelines", "title_hint": "Streaming Engineer", "sal_range": (160000, 240000)},
    {"skills": "SQL,Python,dbt,BigQuery,Looker,Airflow,Data Modeling", "title_hint": "Analytics Engineer", "sal_range": (125000, 190000)},
    {"skills": "AWS,GCP,Terraform,Docker,Kubernetes,Python,Monitoring,Linux,Helm", "title_hint": "Multi-Cloud DevOps", "sal_range": (155000, 235000)},
    {"skills": "Kubernetes,Docker,Istio,ArgoCD,Terraform,Go,Linux,Monitoring", "title_hint": "Platform Engineer", "sal_range": (160000, 245000)},
    {"skills": "Python,Go,AWS,Terraform,Monitoring,Grafana,PagerDuty,Linux,SLOs", "title_hint": "SRE", "sal_range": (160000, 240000)},
    {"skills": "Azure,Terraform,Docker,Kubernetes,PowerShell,CI/CD,Networking", "title_hint": "Azure Cloud", "sal_range": (150000, 225000)},
    {"skills": "Security,Compliance,SOC2,GDPR,Risk Assessment,AWS,Python,Audit", "title_hint": "Security Compliance", "sal_range": (140000, 210000)},
    {"skills": "Security,Reverse Engineering,Malware Analysis,Python,Assembly,Forensics", "title_hint": "Security Researcher", "sal_range": (160000, 250000)},
    {"skills": "Python,Playwright,Cypress,CI/CD,API Testing,Performance Testing,SQL", "title_hint": "QA Automation", "sal_range": (110000, 165000)},
    {"skills": "Java,TestNG,Selenium,REST Assured,Jenkins,Docker,API Testing", "title_hint": "SDET", "sal_range": (120000, 180000)},
    {"skills": "Product Strategy,Data Analysis,SQL,User Research,Agile,Jira,Metrics", "title_hint": "Product Manager", "sal_range": (150000, 225000)},
    {"skills": "Technical Writing,API Docs,Markdown,Git,Developer Experience,Tutorials", "title_hint": "Technical Writer", "sal_range": (100000, 155000)},
    {"skills": "Figma,Sketch,User Research,Interaction Design,Prototyping,Usability Testing", "title_hint": "UX Researcher", "sal_range": (120000, 180000)},
    {"skills": "Figma,UI,Motion Design,Illustration,Design Tokens,Brand,Typography", "title_hint": "Visual Designer", "sal_range": (125000, 190000)},
    {"skills": "Solidity,Foundry,EVM,DeFi,Security Auditing,TypeScript,Hardhat", "title_hint": "Smart Contract", "sal_range": (165000, 260000)},
    {"skills": "C,C++,FreeRTOS,ARM,SPI,I2C,UART,Debugging,Oscilloscope", "title_hint": "Firmware Engineer", "sal_range": (125000, 195000)},
    {"skills": "C++,ROS2,Python,SLAM,Perception,Motion Planning,Simulation", "title_hint": "Autonomous Systems", "sal_range": (165000, 250000)},
    {"skills": "Python,R,Bayesian Statistics,Causal Inference,SQL,Experiment Design", "title_hint": "Research Scientist", "sal_range": (160000, 250000)},
    {"skills": "Python,Airflow,dbt,Snowflake,AWS,Terraform,Great Expectations", "title_hint": "Data Platform", "sal_range": (155000, 235000)},
    {"skills": "TypeScript,React,Node.js,GraphQL,PostgreSQL,Prisma,Docker,AWS", "title_hint": "TypeScript Full Stack", "sal_range": (145000, 215000)},
    {"skills": "Python,FastAPI,React,TypeScript,PostgreSQL,Docker,AWS,Redis", "title_hint": "Full Stack Python/React", "sal_range": (150000, 220000)},
    {"skills": "Elixir,Phoenix,PostgreSQL,LiveView,Docker,Distributed Systems", "title_hint": "Elixir Backend", "sal_range": (140000, 215000)},
    {"skills": "Python,Django,Celery,PostgreSQL,Elasticsearch,Docker,AWS,Monitoring", "title_hint": "Python Search", "sal_range": (145000, 215000)},
    {"skills": "JavaScript,TypeScript,Svelte,SvelteKit,CSS,TailwindCSS,Testing", "title_hint": "Svelte Frontend", "sal_range": (120000, 180000)},
    # --- Leadership / senior IC ---
    {"skills": "Leadership,Hiring,Architecture,Mentorship,Python,Go,Agile,Roadmapping", "title_hint": "Engineering Manager", "sal_range": (200000, 290000)},
    {"skills": "Leadership,Mentorship,React,TypeScript,Design Systems,Architecture,Hiring", "title_hint": "Frontend Manager", "sal_range": (195000, 285000)},
    {"skills": "Architecture,Distributed Systems,Mentorship,Go,Python,Design Docs,Leadership", "title_hint": "Staff Engineer", "sal_range": (220000, 330000)},
    {"skills": "Architecture,Systems Design,Strategy,Cross-team,Mentorship,Leadership", "title_hint": "Principal Engineer", "sal_range": (250000, 380000)},
    {"skills": "Leadership,Strategy,Hiring,Org Design,Budgeting,Cross-functional", "title_hint": "Director of Engineering", "sal_range": (270000, 410000)},
    # --- Junior IC ---
    {"skills": "Python,Flask,SQL,Git,HTML,CSS,JavaScript", "title_hint": "Junior Backend", "sal_range": (75000, 105000)},
    {"skills": "JavaScript,React,HTML,CSS,Git,REST,Bootstrap", "title_hint": "Junior Frontend", "sal_range": (70000, 100000)},
    {"skills": "Python,Pandas,SQL,Excel,Statistics,Tableau,Git", "title_hint": "Junior Data Analyst", "sal_range": (70000, 95000)},
    {"skills": "Java,Spring,MySQL,Git,Maven,JUnit", "title_hint": "Junior Java", "sal_range": (75000, 105000)},
    # --- Gaming ---
    {"skills": "C++,Unreal,Graphics,Math,Performance,Multithreading,Physics", "title_hint": "Game Engine Programmer", "sal_range": (150000, 230000)},
    {"skills": "C#,Unity,Game Design,Animation,Physics,Mobile,Testing", "title_hint": "Unity Gameplay", "sal_range": (125000, 195000)},
    {"skills": "Go,C++,Networking,Distributed Systems,Linux,Multiplayer,Performance", "title_hint": "Game Backend", "sal_range": (150000, 235000)},
    {"skills": "C++,HLSL,GLSL,Vulkan,DirectX,Graphics,Math", "title_hint": "Graphics Programmer", "sal_range": (170000, 270000)},
    # --- Quant / Trading ---
    {"skills": "C++,Python,Low Latency,Linux,Networking,Algorithms,Math", "title_hint": "Quantitative Developer", "sal_range": (200000, 350000)},
    {"skills": "Python,Statistics,Math,Machine Learning,Time Series,R,Backtesting", "title_hint": "Quant Researcher", "sal_range": (220000, 380000)},
    {"skills": "C++,Linux,Networking,Kernel,FPGA,Performance,Latency", "title_hint": "HFT Engineer", "sal_range": (240000, 420000)},
    # --- Bio / Climate / Hardware ---
    {"skills": "Python,R,Genomics,Pandas,Snakemake,AWS,Biology,Statistics", "title_hint": "Bioinformatics", "sal_range": (130000, 200000)},
    {"skills": "Python,R,Bioinformatics,Statistics,Machine Learning,Biology,Genomics", "title_hint": "Computational Biologist", "sal_range": (150000, 235000)},
    {"skills": "Python,GIS,Geospatial,PostgreSQL,AWS,Data Pipelines,Numerical Computing", "title_hint": "Climate Tech Engineer", "sal_range": (140000, 215000)},
    {"skills": "C++,Python,ROS,Perception,SLAM,Sensor Fusion,Linux", "title_hint": "AV Perception", "sal_range": (175000, 275000)},
    {"skills": "Python,C++,GIS,Geospatial,PostGIS,Point Clouds,Algorithms", "title_hint": "Mapping Engineer", "sal_range": (150000, 225000)},
    # --- Platform deep ---
    {"skills": "PostgreSQL,MySQL,Query Optimization,Replication,Linux,Performance,Backup", "title_hint": "Database Engineer", "sal_range": (160000, 240000)},
    {"skills": "Go,Rust,Consensus,Raft,Distributed,Linux,Networking,Storage", "title_hint": "Distributed Systems", "sal_range": (180000, 280000)},
    {"skills": "C++,LLVM,Rust,Compilers,Code Generation,Optimization,Linux", "title_hint": "Compiler Engineer", "sal_range": (175000, 280000)},
    {"skills": "C,Linux Kernel,eBPF,Drivers,Performance,Debugging,Networking", "title_hint": "Kernel Engineer", "sal_range": (180000, 290000)},
    {"skills": "Bazel,Make,CI/CD,Jenkins,Python,Linux,Containers,Monorepo", "title_hint": "Build Engineer", "sal_range": (140000, 215000)},
    {"skills": "Go,Python,gRPC,OpenAPI,GraphQL,Auth,Rate Limiting,Observability", "title_hint": "API Platform", "sal_range": (155000, 230000)},
    # --- Emerging ---
    {"skills": "C++,Unity,Unreal,3D Graphics,Spatial Computing,Math,SDK", "title_hint": "AR/VR Engineer", "sal_range": (160000, 245000)},
    {"skills": "C++,GLSL,HLSL,Math,Rendering,Ray Tracing,Real-time Graphics", "title_hint": "Graphics Researcher", "sal_range": (180000, 290000)},
    {"skills": "C++,DSP,Audio,Signal Processing,Math,SIMD,Real-time", "title_hint": "Audio DSP", "sal_range": (155000, 240000)},
    {"skills": "Python,Qiskit,Cirq,Linear Algebra,Physics,Math,Quantum Algorithms", "title_hint": "Quantum Engineer", "sal_range": (165000, 260000)},
    # --- DevRel / Customer-facing ---
    {"skills": "Public Speaking,Technical Writing,Python,JavaScript,Demos,Community,Conferences", "title_hint": "Developer Advocate", "sal_range": (130000, 200000)},
    {"skills": "Python,APIs,SQL,Communication,Pre-sales,Demos,Architecture", "title_hint": "Solutions Engineer", "sal_range": (140000, 215000)},
    {"skills": "Python,SQL,Data Pipelines,Customer-facing,Communication,Problem Solving", "title_hint": "Forward Deployed", "sal_range": (150000, 230000)},
    # --- More variety ---
    {"skills": "JavaScript,TypeScript,Three.js,WebGL,WebGPU,Math,Performance,Shaders", "title_hint": "WebGL Engineer", "sal_range": (150000, 230000)},
    {"skills": "React,TypeScript,CSS,Figma,Animation,Design Systems,Storybook,A11y", "title_hint": "Design Engineer", "sal_range": (150000, 225000)},
    {"skills": "PostgreSQL,Linux,Backup,Replication,pgBouncer,Performance,Monitoring,SQL", "title_hint": "PostgreSQL DBA", "sal_range": (165000, 250000)},
    {"skills": "Java,Kotlin,Spring,PostgreSQL,Docker,Microservices,Kafka", "title_hint": "Kotlin Backend", "sal_range": (145000, 220000)},
    {"skills": "Python,Django,Stripe,REST,PostgreSQL,Redis,Celery,Docker", "title_hint": "Payments Engineer", "sal_range": (155000, 230000)},
    {"skills": "Elixir,Phoenix,LiveView,PostgreSQL,GraphQL,Testing", "title_hint": "Elixir Full Stack", "sal_range": (145000, 220000)},
    {"skills": "Go,Kubernetes,Prometheus,Grafana,Linux,Networking,Monitoring", "title_hint": "Observability Engineer", "sal_range": (160000, 240000)},
    {"skills": "Python,LangChain,Vector DB,RAG,Prompt Engineering,FastAPI,OpenAI", "title_hint": "Applied LLM", "sal_range": (170000, 260000)},
    {"skills": "Python,Pinecone,Embeddings,RAG,FastAPI,LangChain,Anthropic", "title_hint": "Search & RAG", "sal_range": (170000, 255000)},
    {"skills": "TypeScript,Next.js,tRPC,Prisma,Tailwind,Vercel,PostgreSQL", "title_hint": "TypeScript Full Stack", "sal_range": (140000, 210000)},
    {"skills": "Python,SQL,Looker,dbt,BigQuery,Tableau,Stakeholder Communication", "title_hint": "Analytics Lead", "sal_range": (145000, 220000)},
    {"skills": "Java,Android,Jetpack Compose,Coroutines,Hilt,Room,Testing,CI/CD", "title_hint": "Android Senior", "sal_range": (160000, 240000)},
    {"skills": "Swift,SwiftUI,UIKit,Combine,Async/Await,XCTest,Fastlane", "title_hint": "iOS Senior", "sal_range": (165000, 245000)},
    {"skills": "Python,Triton,CUDA,PyTorch,Performance,GPU,Distributed Training", "title_hint": "ML Performance", "sal_range": (185000, 295000)},
    {"skills": "Python,Kubeflow,MLflow,Kubernetes,GCP,Vertex AI,MLOps", "title_hint": "MLOps Engineer", "sal_range": (165000, 250000)},
    {"skills": "Python,FastAPI,WebSockets,Redis,PostgreSQL,Docker,Async", "title_hint": "Realtime Backend", "sal_range": (150000, 225000)},
    {"skills": "Go,Postgres,gRPC,Kubernetes,Helm,Linux,Tracing,Open Telemetry", "title_hint": "Cloud Native", "sal_range": (160000, 245000)},
    {"skills": "Rust,Tokio,Axum,Postgres,Kafka,Linux,Performance", "title_hint": "Rust Backend", "sal_range": (170000, 260000)},
    {"skills": "C++,Linux,Storage,Filesystems,Performance,RAID,SAN", "title_hint": "Storage Engineer", "sal_range": (170000, 260000)},
]

EDUCATIONS = ["Bachelor", "Bachelor", "Bachelor", "Bachelor", "Master", "Master", "PhD"]
INTROS = [
    "{exp} years of {hint} experience, passionate about building scalable and reliable systems.",
    "Experienced {hint} professional with {exp} years in the industry, focused on clean code and best practices.",
    "{exp}-year {hint} veteran, contributed to multiple high-traffic production systems serving millions of users.",
    "Results-driven {hint} engineer with {exp} years of hands-on experience at both startups and large enterprises.",
    "{hint} specialist with {exp} years of experience, strong background in distributed systems and performance optimization.",
    "Creative {hint} professional with {exp}+ years, passionate about user experience and technical excellence.",
    "{exp} years in {hint}, led cross-functional teams and delivered projects from concept to production.",
    "Self-motivated {hint} developer with {exp} years of experience, quick learner and effective communicator.",
]

candidates = []
used_names = set()
for i, profile in enumerate(CANDIDATE_PROFILES):
    while True:
        name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
        if name not in used_names:
            used_names.add(name)
            break
    exp = random.randint(1, 8)
    edu = random.choice(EDUCATIONS)
    if "Research" in profile["title_hint"] or "Senior Data Scientist" in profile["title_hint"]:
        edu = random.choice(["Master", "PhD"])
        exp = max(exp, 4)
    loc = random.choice(EXTRA_LOCATIONS)
    sal = random.randint(profile["sal_range"][0], profile["sal_range"][1])
    intro = random.choice(INTROS).format(exp=exp, hint=profile["title_hint"])
    candidates.append({
        "candidate_id": f"C{i+1:03d}",
        "name": name,
        "skills": profile["skills"],
        "experience_years": exp,
        "education": edu,
        "preferred_location": loc,
        "expected_salary": sal,
        "self_intro": intro,
    })

print(f"Generated {len(candidates)} candidates")

with open("data/jobs.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["job_id","title","company","location","required_skills","min_experience","education","salary_min","salary_max","description"])
    w.writeheader()
    w.writerows(jobs)

with open("data/candidates.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["candidate_id","name","skills","experience_years","education","preferred_location","expected_salary","self_intro"])
    w.writeheader()
    w.writerows(candidates)

print("Saved to data/jobs.csv and data/candidates.csv")
