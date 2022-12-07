FROM python:3.7-slim

WORKDIR /backend

COPY requirements.txt /backend

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY ./ /backend

CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000
