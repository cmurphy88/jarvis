FROM python:3.10

RUN apt-get update

WORKDIR /api

RUN pip install --upgrade pip
RUN pip install -U setuptools
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ARG API_DB_URL
ENV DATABASE_URL=$API_DB_URL

ENTRYPOINT ["sh", "-c"]

CMD ["gunicorn --bind 0.0.0.0:8000 app.main:app -k uvicorn.workers.UvicornWorker"]
