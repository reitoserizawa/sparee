FROM python:3.13-slim

WORKDIR /app

# Install system deps if needed (curl, gcc, etc.)
RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your code
COPY . .

CMD ["python", "worker.py"]