FROM python:3.12

WORKDIR /code

# HINT:
# Think about Docker layer caching efficiency
COPY . /code

RUN pip install -r requirements.txt

EXPOSE 8000

# HINT:
# Check the Python filename/module name
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
