Set up a Django backend with Django REST Framework and an api app.

Added two endpoints: GET /api/health/ (status check) and POST /api/echo/ (simple echo of a message).

Created a Vite + React frontend and wired it to call POST /api/echo/ via fetch, showing “Hello from React” in the UI.

Configured CORS in Django using django-cors-headers so the React dev server (port 5174) can call the backend (port 8000) without errors.

Confirmed full-stack connectivity: browser → React → Django API → JSON response.

README.md (copy-paste into your project root)
text
# Portfolio AI – “Ask About Me”

An AI-ready portfolio project where visitors can ask questions about me, and the system answers using my own data only.  
Current stack: **React (Vite) + Django REST Framework + Docker (backend-ready)**, with LangChain/RAG planned next.

---

## 🎯 Project Goal

Build a production-grade “Ask About Me” feature for my portfolio:

- Users can ask natural-language questions about my skills, projects, and experience.
- Answers are generated from my personal knowledge base (no hallucinations).
- No login or forced forms; fast, low-friction experience.
- Secure backend for any AI/LLM integrations (no API keys in frontend).

---

## 🧱 Tech Stack

### Frontend

- React (Vite)
- JavaScript / Fetch API
- Simple test UI (will evolve into chat UI)

### Backend

- Django
- Django REST Framework (DRF)
- `django-cors-headers` for CORS

### AI Layer (planned)

- LangChain
- Retrieval-Augmented Generation (RAG)
- Vector store (FAISS / Chroma)
- LLM provider (e.g., OpenAI / Groq), configured via environment variables

### DevOps

- Docker (backend image)
- Docker Compose (service orchestration – planned to run full stack)
- `.env` for secrets and config

---

## 🧩 System Design

High-level architecture:

```text
[ Browser (React) ]
        |
        |  HTTPS / JSON
        v
[ Django REST API ]
        |
        |  LangChain (RAG)  <-- (planned)
        v
[ Personal Knowledge Base ]
 (Markdown / text files)
Design principles:

Frontend: UI only, no secrets, just calls APIs.

Backend: owns business logic, AI calls, and security.

AI layer: constrained to my own data (no “I don’t know” fakery).

APIs: stateless; no login required for visitors.

📁 Project Structure
Planned & current structure (some folders are “future” and will be added later):

text
portfolio-ai/
│
├── backend/
│   ├── core/            # Django project (settings, URLs, wsgi)
│   ├── api/             # DRF app with endpoints
│   │   ├── views.py     # health, echo, (later) ask
│   │   ├── urls.py
│   │   └── ...
│   ├── knowledge/       # (planned) personal content for RAG
│   │   ├── about_me.md
│   │   ├── projects.md
│   │   └── experience.md
│   ├── Dockerfile       # backend container
│   ├── requirements.txt
│   └── manage.py
│
├── frontend/
│   ├── src/
│   │   ├── api.js       # API helpers (echoMessage, later askQuestion)
│   │   ├── App.jsx      # current test UI
│   │   └── ...
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
├── docker-compose.yml   # (current: backend service; later: full stack)
├── .env                 # environment variables (not committed)
└── README.md
🔌 Current API Design
Health Check
Simple endpoint to verify backend is alive.

Method: GET

URL: /api/health/

Response:

json
{
  "status": "ok"
}
Echo (Connectivity Test)
Used to validate React ↔ Django communication.

Method: POST

URL: /api/echo/

Request body:

json
{
  "message": "Hello backend"
}
Response body:

json
{
  "message": "Hello backend"
}
Planned main endpoint (not implemented yet):

Ask About Me (planned)
Method: POST

URL: /api/ask/

Request (planned):

json
{
  "question": "What tools does Param use in data analytics?",
  "visitor_type": "recruiter",
  "name": "Optional"
}
Response (planned):

json
{
  "answer": "Param primarily works with SQL, Power BI, Python, and Excel..."
}
🔄 Frontend–Backend Flow (Current)
Current flow (connectivity test):

text
[ React (Vite) UI ]
      |
      |  POST /api/echo/
      v
[ Django + DRF ]
      |
      |  Returns { "message": "Hello backend" }
      v
[ React shows "Hello from React" in UI ]
Implementation:

frontend/src/api.js:

js
export async function echoMessage(message) {
  const response = await fetch("http://localhost:8000/api/echo/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });
  return response.json();
}
frontend/src/App.jsx (temporary test UI):

jsx
import { useState } from "react";
import { echoMessage } from "./api";

function App() {
  const [response, setResponse] = useState("");

  const handleClick = async () => {
    const data = await echoMessage("Hello from React");
    setResponse(data.message);
  };

  return (
    <div className="app">
      <h1>Backend Echo Test</h1>
      <button onClick={handleClick}>Test Backend</button>
      <p>Response: {response}</p>
    </div>
  );
}

export default App;
🌐 CORS Setup (Local Dev)
To allow the React dev server (port 5174) to call the Django API (port 8000), the project uses django-cors-headers.

In backend/core/settings.py:

python
INSTALLED_APPS = [
    # ...
    "corsheaders",
    "rest_framework",
    "api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    # ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5174",
]
🐳 Docker (Backend)
Backend Dockerfile (simplified example):

text
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
Example docker-compose.yml (root):

text
version: "3.9"

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    env_file:
      - .env
    volumes:
      - ./backend:/app
Run:

bash
docker compose up --build
🚀 How to Run (Local Dev)
Backend (Django)
bash
cd backend
python -m venv venv
# Windows:
venv\Scripts\activate
# Install deps:
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Backend will be available at: http://127.0.0.1:8000/.

Frontend (React + Vite)
bash
cd frontend
npm install
npm run dev
Vite will show a URL, e.g.: http://localhost:5174/.

Open that in the browser, click “Test Backend”, and you should see:

text
Response: Hello from React
📌 Roadmap
 Create /knowledge/about_me.md, /knowledge/projects.md, /knowledge/experience.md.

 Add /api/ask/ endpoint using LangChain RAG.

 Build chat-style UI in React (message bubbles, loading, error states).

 Add streaming responses (optional).

 Dockerize frontend and run full stack via docker compose up.

 Deploy: backend (Render/Railway) + frontend (Vercel) under a public domain.

🤝 About This Project
This project is part of my portfolio to demonstrate:

Full-stack skills (React + Django + Docker).

Practical AI integration (LangChain, RAG).

Clean architecture and developer-quality documentation.

text

If you’d like, next I can:

- Add an ASCII sequence diagram of the future `/api/ask` RAG flow, or  
- Tailor a short “How to present this in an interview” section for the README.