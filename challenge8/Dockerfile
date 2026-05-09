# The Invisible Dependency

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# HINT:
# Some Python packages need system dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
