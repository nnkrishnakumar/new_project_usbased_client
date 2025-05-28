# backend/app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "shared/uploads")