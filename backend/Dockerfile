FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# -----------------------------
# Dépendances système
# -----------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    libffi-dev \
    libssl-dev \
    shared-mime-info \
    fonts-dejavu-core \
    fonts-liberation \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Dépendances Python
# -----------------------------
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# -----------------------------
# Code projet
# -----------------------------
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
