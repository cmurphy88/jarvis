FROM node:18

RUN apt-get update
RUN apt-get install -y openssl

WORKDIR /app

COPY . .

RUN npm install

ARG API_DB_URL
ENV DATABASE_URL=$API_DB_URL

CMD ["npm start"]
