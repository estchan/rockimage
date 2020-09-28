FROM tiangolo/meinheld-gunicorn-flask:python3.7

COPY ./ /app
COPY ./app.py /app/main.py
