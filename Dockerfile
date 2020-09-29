FROM tiangolo/meinheld-gunicorn-flask:python3.7

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY ./ /app
COPY ./app.py /app/main.py
