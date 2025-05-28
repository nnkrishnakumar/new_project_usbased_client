# README.md
# Secure AI Chatbot for Data Processing

This project is a secure AI chatbot that:
- Accepts data file uploads from users
- Uses Gemini API to generate plotting/fitting Python code
- Executes code in a sandbox (Docker) for security

## Project Structure
- `backend/`: FastAPI backend handling uploads, Gemini, Docker exec
- `frontend/`: React UI to upload, prompt, and display results
- `sandbox/`: Isolated Python execution environment
- `shared/uploads`: Shared volume for user files

## Run Locally with Docker Compose
```bash
docker-compose up --build
```

Access:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/api

## Security Note
- All execution is isolated in the `sandbox` container with no internet access
- Add additional limitations via Docker or E2B for production






How to run the code:

activate virtualenv : new 

backend :(new) C:\Users\aimar\OneDrive\Desktop\interview\secure-ai-chatbot\backend>uvicorn app.main:app --reload

frontend:C:\Users\aimar\OneDrive\Desktop\interview\secure-ai-chatbot\frontend>npm start

Important: need Gemini or any multimodel API key beacuse other multimodel is very heavy in weight