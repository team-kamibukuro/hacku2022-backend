FROM python:3.8

WORKDIR /usr/src/backend/app
COPY ./requirements.txt /usr/src/backend/app

EXPOSE 8099

RUN apt-get update
RUN apt install -y postgresql postgresql-contrib

RUN pip install -r requirements.txt


