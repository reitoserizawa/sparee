FROM python:3.13-slim

WORKDIR /app

# System dependencies (for psycopg2/asyncpg, shapely, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Install system deps if needed (curl, gcc, etc.)
RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your code
COPY . .

# Default command (can be overridden in docker-compose)
CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]