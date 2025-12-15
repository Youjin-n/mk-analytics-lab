# DS Learning Lab - Folder Structure

> 60 haftalık Data Science, MLOps ve AI Security öğrenim yolculuğu için hiyerarşik klasör yapısı.

## 📁 Structure Overview

```
ds-learning-lab/
│
├── 📁 faz-1-core/                    # Week 1-20: Core Engineering & Analytics
│   ├── track-engineering/            # Python, Clean Code, Linux (Week 1-5)
│   ├── track-data-engineering/       # SQL & ETL (Week 6-12)
│   ├── track-backend/                # FastAPI & Security (Week 13-16)
│   └── track-analytics/              # Excel & Power BI (Week 17-20)
│
├── 📁 faz-2-production/              # Week 21-34: Production & Deploy
│   ├── track-mlops/                  # Docker (Week 21-22)
│   ├── track-cloud/                  # LocalStack & Live Deploy (Week 23-24)
│   ├── track-observability/          # Logging & Monitoring (Week 25)
│   ├── track-cicd/                   # GitHub Actions (Week 26-27)
│   ├── track-airflow/                # Orchestration (Week 28-30)
│   ├── track-data-quality/           # Great Expectations (Week 31)
│   ├── track-dbt/                    # dbt Core (Week 32-33)
│   └── track-career/                 # Career Sprint (Week 34)
│
├── 📁 faz-3-ml/                      # Week 35-50: ML & MLOps
│   ├── track-data-science/           # Math, Pandas, ML Basics (Week 35-41)
│   ├── track-mlops-advanced/         # MLflow, Serving, Drift (Week 42-47)
│   └── track-portfolio/              # PhishGuard & Visibility (Week 48-50)
│
├── 📁 faz-4-ai-security/             # Week 51-60: AI Security & RAG
│   ├── track-genai/                  # LLM Basics (Week 51)
│   ├── track-security/               # OWASP, Defense, NIST (Week 52-54)
│   ├── track-rag/                    # RAG Implementation (Week 55-57)
│   ├── track-devsecops/              # Scanning (Week 58)
│   ├── track-integration/            # Final Integration (Week 59)
│   └── track-portfolio/              # Grand Finale (Week 60)
│
├── 📁 _templates/                    # Reusable templates
│   └── week-template/                # Standard week folder structure
│       ├── exercises/
│       ├── notes/
│       └── artifacts/
│
├── 📁 _resources/                    # Learning resources
│   ├── cheatsheets/
│   ├── references/
│   └── interview-prep/
│
├── 📁 progress/                      # Progress tracking
│   ├── ROADMAP.md                    # Master 60-week plan
│   ├── WEEKLY_LOG.md                 # Weekly summaries
│   └── DONE_EVIDENCE.md              # Completion evidence
│
├── .gitignore
├── requirements.txt
├── STRUCTURE.md                      # This file
└── README.md
```

## 🏷️ Naming Convention

| Level | Format | Example |
|-------|--------|---------|
| Faz | `faz-{N}-{name}` | `faz-1-core` |
| Track | `track-{name}` | `track-engineering` |
| Week | `week-{NN}-{topic}` | `week-01-python-env` |

## 📊 Week Distribution

| Faz | Weeks | Focus |
|-----|-------|-------|
| Faz 1 | 1-20 | Core Engineering & Analytics |
| Faz 2 | 21-34 | Production & Deploy |
| Faz 3 | 35-50 | ML & MLOps |
| Faz 4 | 51-60 | AI Security & RAG |

## 🎯 Per-Week Folder Contents

Each week folder should contain:
- `README.md` - Week goals, checklist, resources
- `exercises/` - Practice problems and solutions
- `notes/` - Theory notes and summaries
- `artifacts/` - Screenshots, demos, outputs (DONE evidence)
