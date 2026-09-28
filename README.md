# LegalEase ⚖️ - AI Legal Document Generator

> Making legal documents simple for everyone!

### What is this?
LegalEase is an AI tool that generates legal documents like Rental Agreements, NDA, Employment Letters in seconds!

### How to Run?
**Backend:**
cd LegalEaseAPI
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000

**Frontend:**
cd frontend
python -m http.server 5500
Then open http://localhost:5500 in browser

### Tech Stack:
- Backend: FastAPI + Uvicorn
- AI Model: Gemini 1.5 Pro for long context legal generation
- Frontend: HTML, CSS, JavaScript

### Team: Mydhrayani
Built for Meta AI Hackathon 2026
