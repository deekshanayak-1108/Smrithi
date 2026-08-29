# SMRITHI – Backend REST API
### AI-Based Cognitive Gaming and Memory Assistance Platform for Elderly Dementia Patients in the North Eastern Region (NER)
**Smart India Hackathon (SIH) Problem Statement:** `SIH26003`

---

## 📌 Project Overview

**SMRITHI** is an AI-driven, culturally grounded cognitive stimulation and memory assistance backend platform engineered specifically for elderly dementia patients in North East India.

This repository contains the **REST API Backend**, designed to be consumed by clinical portals, mobile caregiver applications, or edge touch devices. It is completely independent and testable through Postman, Swagger UI, and cURL.

---

## 🚀 Key Architecture & Features

```
smrithi-backend/
│
├── app/
│   ├── main.py                     # FastAPI Application Initialization & Lifespan
│   ├── core/
│   │   └── config.py               # Pydantic Settings & Environment Configuration
│   ├── database/
│   │   └── db.py                   # MongoDB Manager + Zero-Config In-Memory Fallback
│   ├── models/                     # Database Document Models
│   ├── schemas/                    # Pydantic V2 Request & Response Validation Schemas
│   ├── routes/                     # Clean Modular REST API Routers
│   │   ├── auth.py                 # JWT Authentication & Role-Based Access Control
│   │   ├── patients.py             # Elderly Patient Profile Lifecycle & MMSE Tracking
│   │   ├── caregivers.py           # Caregiver Accounts, Associations & Clinical Alerts
│   │   ├── games.py                # 5 Cognitive Games Engine & Attempt History
│   │   ├── adaptive.py             # Adaptive Difficulty Evaluation Endpoints
│   │   ├── progress.py             # Multi-Domain Progress Tracking & Analytics
│   │   ├── languages.py            # Multilingual NER Localization & Translation
│   │   ├── voice.py                # Text-To-Speech (TTS) Voice Synthesis Service
│   │   ├── reminders.py            # Routine, Medication & Gaming Reminders
│   │   └── reports.py              # AI Clinical Progress Summary & Doctor Reports
│   ├── services/                   # Business Logic & External Service Abstractions
│   ├── ai/
│   │   ├── adaptive/
│   │   │   ├── feature_extractor.py # Statistical Rolling Feature Extraction
│   │   │   ├── adaptive_rules.py   # Heuristic Rule-Based Progression Engine
│   │   │   └── ml_pipeline.py      # Modular Preprocessing, Model & Evaluation Pipeline
│   │   └── ai_report_service.py    # Clinical Progress Synthesizer (Gemini + Local Rules)
│   ├── middleware/
│   │   ├── auth_guard.py           # Bearer Token & Role Guards
│   │   └── error_handler.py        # Global Exception Handlers (Zero Crashes)
│   └── utils/
│       └── helpers.py              # Timezone-aware UTC helpers
│
├── tests/
│   └── test_backend_api.py         # Pytest Automated Test Suite (100% Pass)
│
├── Smrithi_Backend.postman_collection.json # Complete Postman Collection
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 🧠 5 Cognitive Games with North Eastern Cultural Context

| Game Type | Cognitive Domain | Cultural Context (NER) | Description & Stimuli |
| :--- | :--- | :--- | :--- |
| **1. Memory** | *Short-term & Working Memory* | Assamese Japi, Folk Dhol, Bamboo Kula, Pepa Hornpipe | Displays N cultural stimuli for brief observation. Patient recalls target items from distractor options. |
| **2. Attention** | *Selective & Sustained Attention* | Folk craft symbols, Bell-metal utensils | Patient quickly scans a visual grid of distractors to locate a target cultural motif. |
| **3. Sequence** | *Executive Function & Reasoning* | Assam tea preparation, Traditional recipes, Weaving setup | Patient orders disordered daily routine steps into the correct chronological sequence. |
| **4. Pattern** | *Pattern Recognition & Inductive Logic* | Eri, Muga, and tribal textile borders | Patient predicts the next repeating geometric motif in a traditional handloom pattern. |
| **5. Recognition** | *Semantic & Visual Memory* | Regional heritage items, musical instruments | Identifies regional cultural tools and symbols from visual cues and names. |

---

## 📈 Multi-Factor Adaptive Difficulty Module

The adaptive difficulty system dynamically scales cognitive challenge based on patient performance to stimulate neuroplasticity without causing cognitive frustration.

### 1. Data Preprocessing & Feature Extraction (`feature_extractor.py`)
- **Rolling Accuracy**: Mean accuracy over the last 3–5 attempts.
- **Average Response Latency**: Response time in milliseconds.
- **Latency Variance / Standard Deviation**: Measures consistency and cognitive fatigue.
- **Mistake Rate**: Ratio of incorrect attempts to total questions.
- **Performance Streak**: Consecutive successes ($\ge 80\%$) vs. struggles ($< 50\%$).
- **Linear Trend Slope**: Rate of improvement or decline over time ($\frac{\Delta \text{Accuracy}}{\Delta \text{Sessions}}$).

### 2. Heuristic Rule Engine (`adaptive_rules.py`)
- **Increase Difficulty (+1, max 5)**: When rolling accuracy $\ge 85\%$ or ($\ge 75\%$ with positive streak $\ge 2$) and stable latency.
- **Decrease Difficulty (-1, min 1)**: When accuracy $< 50\%$, negative streak $\le -2$, or steep negative slope.
- **Maintain Difficulty**: When patient is in optimal consolidation zone ($50\% - 80\%$).

### 3. ML Architecture Separation (`ml_pipeline.py`)
- Fully separated **Data Preprocessing**, **Feature Extraction**, **Model Interface**, and **Prediction Engine** allowing plug-and-play machine learning classifiers or reinforcement learning algorithms.

---

## 🌐 Multilingual / North Eastern Language Support

Native support for **9 languages** with localized prompt matrices and cultural object vocabulary:
1. **Assamese (`as`)**: অসমীয়া (Native scripts & cultural prompts)
2. **Bengali (`bn`)**: বাংলা (Tripura & Barak Valley regional prompts)
3. **Manipuri / Meitei (`mni`)**: মৈতৈলোন্ / ꯃꯤꯇꯩꯂꯣꯟ
4. **Bodo (`brx`)**: बर'
5. **Mizo (`lus`)**: Mizo ṭawng
6. **Khasi (`kha`)**: Ka Ktien Khasi
7. **Garo (`grt`)**: A·chik
8. **Hindi (`hi`)**: हिन्दी
9. **English (`en`)**: English

---

## 🎙️ Voice & Text-To-Speech (TTS) Service

- **Endpoint**: `POST /api/voice/synthesize`
- Generates speech audio for cognitive instructions in regional Indian phonetics using `gTTS` with local disk caching and base64 streaming.
- Graceful offline fallback when external network connectivity is unavailable.

---

## 🩺 AI Progress Reports & Clinical Intelligence

- **Endpoint**: `GET /api/reports/patient/{patient_id}/progress-report`
- Aggregates actual stored performance data, domain scores, consistency rating, and latency trajectories.
- Synthesizes a structured, doctor-ready JSON report containing:
  - Clinical Summary narrative
  - Domain breakdown across all 5 cognitive areas
  - Identified strengths and areas to watch
  - Caregiver actionable suggestions
  - Adherence and consistency score

> **Medical Disclaimer**: SMRITHI progress reports provide progress-assistance analytics for caregivers and healthcare facilitators. They are **NOT** medical diagnostic devices and do not replace clinical neuropsychological evaluation.

---

## ⚙️ Installation & Running the Server

### Prerequisites
- Python 3.10+
- (Optional) MongoDB server running locally or MongoDB Atlas connection string.

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Configure Environment
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

### Step 3: Run the Backend Server
```bash
python app.py
```
Or with Uvicorn directly:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Server will start on: **`http://127.0.0.1:8000`**

---

## 📖 Interactive API Documentation

Once started, open your browser to access the full interactive OpenAPI documentation:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Automated Testing

Run the comprehensive Pytest test suite:
```bash
pytest backend/tests/test_backend_api.py -v
```

All 12 critical test suites verify:
- Health checks
- Authentication & JWT token security
- Patient & Caregiver lifecycle and association
- 5 Cognitive games session generation & answer submissions
- Adaptive difficulty progression logic
- Multi-domain analytics and trajectory indicators
- Multilingual content retrieval and translation
- Voice TTS synthesis
- Reminder CRUD operations
- AI progress reports
- Error handling and input validation

---

## 📮 Postman Collection

Import `Smrithi_Backend.postman_collection.json` directly into Postman. It includes pre-configured variables:
- `{{base_url}}`: `http://127.0.0.1:8000`
- `{{patient_id}}`: `P001` (seeded demo patient)
- `{{caregiver_id}}`: `cg_demo_001` (seeded demo caregiver)

### Key Postman Endpoints Overview
1. **Health**: `GET /health`
2. **Register**: `POST /api/auth/register`
3. **Login**: `POST /api/auth/login`
4. **Create Patient**: `POST /api/patients/`
5. **Get Patient**: `GET /api/patients/P001`
6. **List Games**: `GET /api/games/`
7. **Start Game**: `POST /api/games/start`
8. **Submit Game Result**: `POST /api/games/submit-result`
9. **Get History**: `GET /api/games/attempts/P001`
10. **Adaptive Difficulty**: `POST /api/adaptive/evaluate`
11. **Multi-Domain Analytics**: `GET /api/analytics/P001`
12. **Languages**: `GET /api/languages`
13. **Voice TTS**: `POST /api/voice/synthesize`
14. **Create Reminder**: `POST /api/reminders`
15. **Generate AI Progress Report**: `GET /api/reports/patient/P001/progress-report?days=30`

---

## 🛡️ Honesty & Transparency Disclosure

- **Adaptive Difficulty**: Features a clear, production-grade statistical feature extractor and heuristic rule engine, alongside an ML pipeline scaffold. It does not make false claims of opaque black-box AI.
- **Clinical AI Summary**: Built-in deterministic clinical intelligence engine generates structured progress summaries directly from stored game attempts, with optional integration for Google Gemini via `GEMINI_API_KEY`.
- **Database**: Full MongoDB database integration with an automatic zero-config in-memory fallback for instant local evaluation.