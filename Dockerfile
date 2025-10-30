# Use a slim python base with GPU optional (this is CPU-only)
FROM python:3.10-slim

# OS deps for image libraries if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libglib2.0-0 libsm6 libxrender1 libxext6 \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# copy requirements first to leverage cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy app and templates
COPY . .

ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py
ENV MODEL_PATH=/app/model/mangonet.h5
ENV UPLOAD_FOLDER=/app/static/uploads

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "3", "--threads", "2", "--timeout", "120"]
