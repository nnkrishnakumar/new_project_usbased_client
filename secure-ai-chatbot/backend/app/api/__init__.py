# backend/app/api/__init__.py
from fastapi import APIRouter
from app.api.endpoints import upload, generate_code, execute_code, status

api_router = APIRouter()
api_router.include_router(upload.router, prefix="/api")
api_router.include_router(generate_code.router, prefix="/api")
api_router.include_router(execute_code.router, prefix="/api")
api_router.include_router(status.router, prefix="/api")