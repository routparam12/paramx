# Paramx – Ask About Me

An AI-powered portfolio feature that allows visitors to ask questions about me and receive accurate answers generated strictly from my personal data (experience, projects, skills).

This project is built with **React, Django, LangChain, and Docker**, following production-grade architecture and best practices.

---

## 🎯 Project Goal

To create an interactive “Ask About Me” feature for my portfolio where:
- Visitors can ask natural language questions
- Answers are generated **only** from my own information
- No login or personal data collection is required
- The system is secure, scalable, and explainable

---

## 🧱 Tech Stack

### Frontend
- React (Vite)
- JavaScript
- Fetch API
- Responsive, mobile-first UI

### Backend
- Django
- Django REST Framework (DRF)
- Python

### AI Layer (planned)
- LangChain
- Retrieval-Augmented Generation (RAG)
- Vector store (FAISS / Chroma)

### DevOps
- Docker
- Docker Compose
- Environment variables (`.env`)

---

## 🏗️ System Architecture

Browser (React)
|
| HTTPS / JSON
v
Django REST API
|
| LangChain (RAG)
v
Personal Knowledge Base



### Design Principles
- Frontend is UI-only (no secrets)
- Backend handles AI logic securely
- AI answers only from verified personal data
- Stateless APIs (no user login, no tracking)

---

## 📁 Project Structure

portfolio-ai/
│
├── backend/
│ ├── core/ # Django project
│ ├── api/ # DRF API app
│ ├── rag/ # LangChain logic (planned)
│ ├── knowledge/ # Personal data (planned)
│ ├── Dockerfile
│ ├── requirements.txt
│ └── manage.py
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ ├── pages/
│ │ └── api.js
│ ├── Dockerfile (planned)
│ └── vite.config.js
│
├── docker-compose.yml
├── .env
└── README.md


---

## 🔌 API Endpoints (Current)

### Health Check
GET /api/health/


Response:
```json
{ "status": "ok" }

Echo Test (Connectivity Check)
POST /api/echo/


Request:

{ "message": "Hello from React" }


Response:

{ "message": "Hello from React" }

