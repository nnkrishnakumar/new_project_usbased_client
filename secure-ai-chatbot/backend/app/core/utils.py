# backend/app/core/utils.py
import os

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)