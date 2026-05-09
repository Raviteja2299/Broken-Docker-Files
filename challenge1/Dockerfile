FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# HINT:
# Is this the correct pip syntax?
RUN pip install requirements.txt

COPY . .

EXPOSE 5000

# HINT:
# Does this file actually exist?
CMD ["python", "main.py"]
