# backend/app/api/endpoints/generate_code.py
from fastapi import APIRouter, Request
from app.services.replicate_service import generate_code_from_prompt

router = APIRouter()

@router.post("/generate-code")
async def generate_code(request: Request):
    body = await request.json()
    file_path = body.get(r"C:\Users\aimar\OneDrive\Desktop\interview\secure-ai-chatbot\shared\uploads\sample_data.csv")
    task = body.get("task")
    
    code = generate_code_from_prompt(file_path, task)
    return {"code": code}
