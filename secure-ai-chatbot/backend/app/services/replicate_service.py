# backend/app/services/replicate_service.py
import os
import replicate

# You can hardcode this or load from .env for security
os.environ["REPLICATE_API_TOKEN"] = ""

def generate_code_from_prompt(file_path: str, task: str) -> str:
    prompt = f"You are given the file `{file_path}`. Your task is: {task}.\nGenerate the code accordingly."

    input = {
        "top_p": 1,
        "prompt": prompt,
        "temperature": 0.75,
        "max_new_tokens": 800
    }

    try:
        output = replicate.run("meta/llama-2-7b-chat", input=input)
        return "".join(output)
    except Exception as e:
        return f"Error generating code: {e}"
