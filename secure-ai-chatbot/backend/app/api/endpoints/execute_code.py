# backend/app/api/endpoints/execute_code.py
from fastapi import APIRouter, Request
from app.services.docker_service import execute_code_securely

router = APIRouter()

@router.post("/execute")
async def execute(request: Request):
    body = await request.json()
    code = body.get("code")
    result = execute_code_securely(code)
    return result