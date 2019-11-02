FROM python:3.8
LABEL Author ="CharaD7" 
LABEL version ="19.03.2"

# Avoide python buffering
ENV PYTHONUNBUFFERED 1

COPY ./app /app
WORKDIR /app
COPY ./app/requirements.txt /requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

# COPY ./entrypoint.sh /entrypoint.sh

# RUN chmod +x /entrypoint.sh

# ENTRYPOINT ["/entrypoint.sh"]

# RUN mkdir /app


# Creating a user for the docker image
# RUN adduser -D user
# USER user