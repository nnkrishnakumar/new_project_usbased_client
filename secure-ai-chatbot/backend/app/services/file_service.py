# backend/app/services/file_service.py
import os
from app.core.config import UPLOAD_FOLDER
from app.core.utils import ensure_dir

def save_uploaded_file(file):
    ensure_dir(r"C:\Users\aimar\OneDrive\Desktop\interview\secure-ai-chatbot\shared\uploads")
    file_path = os.path.join(r"C:\Users\aimar\OneDrive\Desktop\interview\secure-ai-chatbot\shared\uploads", file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return file_path