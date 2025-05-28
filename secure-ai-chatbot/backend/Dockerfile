FROM python:3.10-slim

WORKDIR /app

COPY run_code.py script_template.py /app/

RUN pip install --no-cache-dir matplotlib pandas numpy

CMD ["python", "run_code.py"]