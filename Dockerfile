FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies needed for some Python packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy app
COPY . /app

# Use Uvicorn worker for async support
CMD ["sh", "-c", "gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:${PORT:-8000} app.server:app"]
