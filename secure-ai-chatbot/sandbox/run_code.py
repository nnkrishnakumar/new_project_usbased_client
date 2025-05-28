# sandbox/run_code.py
import os
import subprocess
import uuid

CODE_TEMPLATE_PATH = "script_template.py"
TEMP_SCRIPT_PATH = "generated_script.py"
UPLOAD_DIR = "/shared/uploads"
OUTPUT_PATH = "output.png"

code = os.environ.get("CODE")
file_path = os.environ.get("FILE_PATH")

if not code or not file_path:
    print("Missing input")
    exit(1)

with open(CODE_TEMPLATE_PATH, 'r') as f:
    template = f.read()

script = template.format(code=code, file_path=file_path)

with open(TEMP_SCRIPT_PATH, 'w') as f:
    f.write(script)

try:
    result = subprocess.run(["python", TEMP_SCRIPT_PATH], capture_output=True, text=True, timeout=20)
    print("STDOUT:\n", result.stdout)
    print("STDERR:\n", result.stderr)
    if os.path.exists(OUTPUT_PATH):
        print("Plot saved at:", OUTPUT_PATH)
except subprocess.TimeoutExpired:
    print("Execution timed out.")
