FROM python:3.10.1-slim-buster

RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean \

WORKDIR /api

RUN pip3 install --upgrade pip
RUN python3.9 -m pip install tensorflow
RUN pip3 install deepface
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0"]