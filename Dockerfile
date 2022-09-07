FROM python:3.10-slim-buster

WORKDIR /code/
COPY . /code/

RUN pip install -r requirements.txt
