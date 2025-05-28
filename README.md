secure-ai-chatbot/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── endpoints/
│   │   │   │   ├── upload.py          # Upload data files
│   │   │   │   ├── generate_code.py   # Interact with Gemini API
│   │   │   │   ├── execute_code.py    # Run code securely in Docker/E2B
│   │   │   │   └── status.py          # Optional: status updates
│   │   │   └── __init__.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py              # Settings, Gemini API keys, etc.
│   │   │   └── utils.py               # Common functions (e.g., validate files)
│   │   │
│   │   ├── services/
│   │   │   ├── gemini_service.py      # Gemini API logic
│   │   │   ├── docker_service.py      # Docker/E2B execution logic
│   │   │   └── file_service.py        # File handling logic
│   │   │
│   │   ├── main.py                    # FastAPI entry point
│   │   └── requirements.txt
│   │
│   ├── Dockerfile                     # Backend Dockerfile (optional)
│   └── .env                           # Environment variables (secret keys etc.)
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Chatbot.jsx            # Chat UI with prompts
│   │   │   ├── FileUpload.jsx         # File upload interface
│   │   │   └── PlotDisplay.jsx        # Display generated plots
│   │   ├── services/
│   │   │   ├── api.js                 # Axios config for backend calls
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   └── .env                           # Frontend API URLs etc.
│
├── sandbox/
│   ├── Dockerfile                     # Dockerfile for sandbox
│   ├── script_template.py             # Template script Gemini fills
│   └── run_code.py                    # Executes Gemini-generated code safely
│
├── shared/
│   └── uploads/                       # Temporarily stored user files
│
├── docker-compose.yml                 # Compose for backend, frontend, and sandbox
└── README.md






CODE PLAN:

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
