# 📌 1. Usar una imagen ligera de Python
FROM python:3.9-slim

WORKDIR /app
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ../app/app.py .  
COPY ../app/src ./src

ENV PYTHONPATH="/app/src"

EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
