FROM python:3.11-slim

WORKDIR /app

RUN useradd -m appuser

# HINT:
# Who owns copied files/directories?
USER appuser

COPY . .

CMD ["python", "app.py"]
