FROM python:3.10.1-slim-buster

RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean \

WORKDIR /api

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ARG API_DB_URL
ENV DATABASE_URL=$API_DB_URL

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0"]
