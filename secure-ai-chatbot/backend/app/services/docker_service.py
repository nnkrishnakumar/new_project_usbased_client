# backend/app/services/docker_service.py
import subprocess
import uuid

def execute_code_securely(code):
    file_name = f"temp_{uuid.uuid4().hex}.py"
    with open(file_name, "w") as f:
        f.write(code)
    try:
        result = subprocess.run(["docker", "run", "--rm", "-v", f"{file_name}:/app/script.py", "secure-sandbox-image"], capture_output=True, timeout=30)
        return {"output": result.stdout.decode(), "error": result.stderr.decode()}
    except Exception as e:
        return {"error": str(e)}