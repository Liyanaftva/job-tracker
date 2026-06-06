# 🎯 Job Application Tracker

A full-stack AI-powered job application tracker that helps you manage every job you apply to — and tells you exactly what skills you're missing for each role.

---

## 💡 What It Does

1. You fill a form → title, company, paste the job description
2. You click Submit
3. Frontend sends that data to the backend
4. Backend receives it → validates it (is everything filled? correct types?)
5. Backend saves it to the database
6. Backend sends the job description to Groq AI
7. Groq reads it and returns → summary, required skills, skill gaps
8. Backend saves the AI response to the same job in the database
9. Backend sends everything back to the frontend
10. You see the job card with AI analysis on screen

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React.js + Tailwind CSS |
| Backend | FastAPI (Python) |
| Database | PostgreSQL + SQLAlchemy |
| AI | Groq API (Llama 3) |

---

## 🏗️ Architecture

```
User (Browser)
     ↕  HTTP requests (GET, POST, etc.)
FastAPI Backend
     ↕  SQL queries
PostgreSQL Database
     ↕  API calls
Groq AI
```

---

## 🤖 How Groq AI Works

```
You paste a job description
        ↓
Your backend sends it to Groq with a prompt
"Here is a job description. Extract the required skills..."
        ↓
Groq's Llama 3 model reads it and responds
        ↓
Your backend saves the response to the database
        ↓
Those null fields are now filled ✅
```

---

## 🔁 Request Flow

Every request follows this exact path:

```
FRONTEND    →  sends "POST /jobs" with job data
ENDPOINT    →  the URL that receives it (/jobs)
ROUTER      →  sees it came in, sends it to the right service
SERVICE     →  saves to database, calls Groq, returns result
ROUTER      →  takes the result, sends it back as response
FRONTEND    →  receives it and shows it on screen
```

---

## 🛣️ API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/jobs` | Create a new job |
| GET | `/jobs` | Get all jobs |
| GET | `/jobs/{id}` | Get one job by ID |
| PATCH | `/jobs/{id}` | Update job status or notes |
| DELETE | `/jobs/{id}` | Delete a job |

---

## 📁 Project Structure

```
job-tracker/
├── README.md
├── .gitignore
├── backend/
│   ├── requirements.txt
│   └── app/
│       ├── main.py              ← 🚪 Front door. Starts the app, registers all routes
│       ├── database.py          ← 🔌 Database connection setup. One file, used everywhere
│       ├── models/
│       │   ├── __init__.py
│       │   └── job.py           ← 🗄️  What your DATABASE tables look like
│       ├── schemas/
│       │   ├── __init__.py
│       │   └── job.py           ← 📋 What your API requests/responses look like
│       ├── routers/
│       │   ├── __init__.py
│       │   └── jobs.py          ← 🛣️  URL endpoints. Decides WHAT happens at each route
│       └── services/
│           ├── __init__.py
│           ├── job_service.py   ← 🧠 DB queries for jobs
│           └── ai_service.py    ← 🤖 Groq AI calls
└── frontend/                    ← ⚛️  React app (coming soon)
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- PostgreSQL 18
- Node.js (for frontend, coming soon)
- Groq API key → [console.groq.com](https://console.groq.com)

### Backend Setup

```bash
# Clone the repo
git clone https://github.com/Liyanaftva/job-tracker.git
cd job-tracker/backend

# Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows
# source venv/bin/activate    # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Create .env file and fill in your credentials
# DATABASE_URL and GROQ_API_KEY

# Run the server
uvicorn app.main:app --reload
```

### Environment Variables

Create a `.env` file inside `backend/`:

```
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/job_tracker
GROQ_API_KEY=gsk_your_key_here
```

### Database Setup

```bash
psql -U postgres
CREATE DATABASE job_tracker;
\q
```

Tables are created automatically when you run the server.

---

## 📌 Roadmap

- [x] Phase 1 — Project setup + database design
- [x] Phase 2 — FastAPI CRUD endpoints
- [x] Phase 3 — Groq AI integration
- [ ] Phase 4 — React frontend
- [ ] Phase 5 — Connect everything + polish

---

## 👩‍💻 Author

**Liyana Fathima Thasneem V A**  
Full Stack Developer  
[LinkedIn](https://linkedin.com/in/liyanafathimathasneemva) · [GitHub](https://github.com/Liyanaftva)