#  Flask Networking Failure

FROM python:3.10

WORKDIR /usr/src/app

# HINT:
# Is this COPY order optimal for caching?
COPY . .

RUN pip install -r requirements.txt

ENV PORT=9000

# HINT:
# Does EXPOSE support variables reliably everywhere?
EXPOSE $PORT

# HINT:
# Shell form vs exec form
CMD python api.py
