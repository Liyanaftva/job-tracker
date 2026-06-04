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
| Auth | JWT (coming soon) |

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

## 📁 Project Structure

```
job-tracker/
├── backend/
│   └── app/
│       ├── main.py        ← 🚪 Front door. Starts the app, registers all routes
│       ├── database.py    ← 🔌 Database connection setup. One file, used everywhere
│       ├── models/        ← 🗄️  What your DATABASE tables look like
│       ├── schemas/       ← 📋 What your API requests/responses look like
│       ├── routers/       ← 🛣️  URL endpoints. Decides WHAT happens at each route
│       └── services/      ← 🧠 Business logic. DB queries + AI calls
└── frontend/              ← React app (coming soon)
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
- [ ] Phase 2 — FastAPI CRUD endpoints
- [ ] Phase 3 — Groq AI integration
- [ ] Phase 4 — React frontend
- [ ] Phase 5 — Connect everything + polish

---

## 👩‍💻 Author

**Liyana Fathima Thasneem V A**  
Full Stack Developer  
[LinkedIn](https://linkedin.com/in/liyanafathimathasneemva) 
[GitHub](https://github.com/Liyanaftva)