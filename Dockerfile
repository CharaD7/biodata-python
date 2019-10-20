FROM python:3.8
LABEL Author ="CharaD7" 
LABEL version ="19.03.2"

# Avoide python buffering
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./mysqlclient-1.4.4.whl /mysqlclient-1.4.4.whl
COPY ./entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh
RUN pip install mysqlclient-1.4.4.whl && -r requirements.txt

ENTRYPOINT ["/entrypoint.sh"]

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Creating a user for the docker image
RUN adduser -D user
USER user