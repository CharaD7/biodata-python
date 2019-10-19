FROM python:3.8-buster
LABEL Author ="CharaD7" 
LABEL version ="19.03.2"

# Avoide python buffering
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Creating a user for the docker image
RUN adduser -D user
USER user