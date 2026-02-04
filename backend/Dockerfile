FROM python:3.13-slim

# make sure python output is sent straight to terminal (e.g. for logging)
ENV PYTHONUNBUFFERED=1
# skip writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# System dependencies (for psycopg2/asyncpg, shapely, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Install system deps if needed (curl, gcc, etc.)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]