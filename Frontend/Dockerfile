FROM python:3.9-slim

WORKDIR /app

COPY Frontend/ /app/Frontend/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "Frontend/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
