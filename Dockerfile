FROM python:3.8-alpine
LABEL Author ="CharaD7" 
LABEL version ="19.03.2"

# Avoide python buffering
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install https://download.lfd.uci.edu/pythonlibs/g5apjq5m/mysqlclient-1.4.4-cp38-cp38-win32.whl && pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Creating a user for the docker image
RUN adduser -D user
USER user