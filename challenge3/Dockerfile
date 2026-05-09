FROM python:3.11 AS builder

WORKDIR /build

COPY requirements.txt .

# HINT:
# Where are packages installed with --user ?
RUN pip install --user -r requirements.txt

FROM python:3.11-slim

WORKDIR /app

# HINT:
# Does this folder always exist?
COPY --from=builder /root/.local /root/.local

COPY worker.py .

ENV PATH=/root/.local/bin:$PATH

# HINT:
# Does this Python file exist?
CMD ["python", "app.py"]
