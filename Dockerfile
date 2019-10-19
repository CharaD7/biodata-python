FROM python:3.8-alpine
MAINTAINER CharaD7

# Avoide python buffering
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN pip install mysqlclient-1.4.4-cp38-cp38-win32.whl

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Creating a user for the docker image
RUN adduser -D user
USER user