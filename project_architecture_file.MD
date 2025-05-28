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


