# biodata-python
**An Biodata app with MDB bootstrap  written in python==3.8 and Djanago==2.2**

This app runs on a docker container with celery and rabbitmq handling some taks/services within the app. To fully delpoy and use the app, simply follow the guidelines below.

## Getting Started

- First, clone the repo [here](https://github.com/CharaD7/biodata-python.git)
- Extract data and change into the cloned directory. Now open the directory with your prefered text editor or IDE. You can as well do so by just opening the extracted folder with any prefered editor or IDE of your choice.
- Download and install [docker](https://hub.docker.com/) based on your OS platform. Be sure to have a minimum RAM of 4gb to be able to run docker. Read the OS-based [documentation](https://docs.docker.com/) here to be able to fully run docker on your system.
-  Download any MySQL database server for running on the system.



  ***

## Setting up the application run environment

-  Create a database with the below configurations:
  
        'NAME': 'biodata_db',
        'USER': 'biodata_admin',
        'PASSWORD': 'NrfrX2E31tvSZkIi',
        'HOST': 'localhost',
        'PORT': '3306',

- The configuration above is found on _line 79_ of the _settings.py_ file. You may change the values to suit your custom configuration but be certain it tallies with the configuration of your MySQL server.
- Be sure user creatd has inherited permissions of a mySQL root user.
  
  ***

## Running the application

-  Build the docker file by running the `docker build .` command in the root directory. This will build and install all necessary dependencies needed to run the app in the docker image.
- Run `docker-compose exec python python manage.py makemigrations` after successfully configuring your server
- Next, run `docker-compose exec python python manage.py migrate` to apply changes
- Create django-superuser by running the command `docker-compose run app sh -c "python manage.py createsuperuser"`. Follow the triggers to create a superuser. Kindly desist from using admin as username for admin user.
- Run `docker-compose up` to start the runserver in docker container.
- Open up a browser and type in the address bar _`127.0.0.1:8000`_ to view the homepage.

***

## Setback Manouvers

1. In a case where you try to build docker and it fails because you have compatibility issues, visit the [docker documentation](https://docs.docker.com/) and carefully follow the setup and run procedures to successfully run the build for docker.

2. Should you have problems installing mysql-connector, kindly comment it out in the requirements.txt file and run in your terminal `pip install mysqlclient-1.4.4.whl` to get the custom client installed. This should fix the problem with installing the required mysql client for the Django application.

3. In a case where build fails, the environment is already set up in the directory so ignore and run `python manage.py runserver` after following the procedures to setting up your database server and docker environment.

***


***

 _Kindly send me a mail at <jijakahn6@gmail.com> if you have any issues or suggestions_
 
 ***
 ***