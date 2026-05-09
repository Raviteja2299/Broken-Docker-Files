FROM python:3.11

WORKDIR /app

# HINT:
# Which Docker layer changes most frequently?
COPY . .

# HINT:
# What happens when app.py changes?
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
