FROM python:3.10

RUN apt-get update
RUN apt-get install -y openssl

WORKDIR /api

COPY . .

RUN pip install

ARG API_DB_URL
ENV DATABASE_URL=$API_DB_URL

ENTRYPOINT ["sh", "-c"]

CMD ["flask run --host=0.0.0.0"]
