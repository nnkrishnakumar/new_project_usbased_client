# backend/app/api/endpoints/upload.py
from fastapi import APIRouter, UploadFile, File
from app.services.file_service import save_uploaded_file

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    print(file)
    file_path = save_uploaded_file(file)
    return {"message": "File uploaded successfully", "path": file_path}