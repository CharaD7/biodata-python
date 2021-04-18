# biodata
**A Biodata app with MDB bootstrap  written in python==3.7 and Djanago==2.7**

This app runs on a vagrant container with celery and rabbitmq handling some taks/services within the app. To fully delpoy and use the app, simply follow the guidelines below.

## Getting Started

- First, clone the repo [here](https://github.com/CharaD7/biodata.git)
- Extract data and change into the cloned directory. Now open the directory with your prefered text editor or IDE. You can as well do so by just opening the extracted folder with any prefered editor or IDE of your choice.
- To successfully run vagrant, make sure you have hyper-V and virtualization support enabled in your bios where necessary. 
-  Download any MySQL database server for running on the system.



  ***

## Setting up the application run environment

-  Create a database with the below configurations:
  
        'NAME': 'biodata_db',
        'USER': 'biodata_admin',
        'PASSWORD': 'NrfrX2E31tvSZkIi',
        'HOST': 'localhost',
        'PORT': '3306',

- The configuration above is found on _line 95_ of the _settings.py_ file. You may change the values to suit your custom configuration but be certain it tallies with the configuration of your MySQL server.
- Be sure user creatd has inherited permissions of a mySQL root user.
  
  ***

## Running the application

-  Download and install vagrant onto your machine.
- Visit _`https://www.vagrantup.com/intro/getting-started/boxes.html`_ and read on how to get box installed
- Open a new console tab and run `"python manage.py runserver"`
- Fire up a browser and type in the address bar _`127.0.0.1:8000`_ to view the homepage.

***

## Setback Manouvers

1. Should you have problems installing mysql-connector, kindly comment it out in the requirements.txt file,
visit _`https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient`_ to download the wheel file for your python version
and system architecture. Then run in your terminal `pip install mysqlclient-1.4.6-cp<python-version>-cp<python-version>-win_amd<system-architecture>.whl` to get the custom client installed. This should fix the problem with installing the required mysql client for the Django application.

2. If you get this error: `ERROR: Service 'celery_worker' failed to build: unauthorized: authentication required`, then you will need to add `COMPOSE_CONVERT_WINDOWS_PATHS` to your system variables and set the value to 1. Thereafter, open the docker interface and go to shared drives, check the drive in which docker is installed and you should be okay.

3. In a case where build fails, the environment is already set up in the directory so ignore and run `python manage.py runserver` after following the procedures to setting up your database server and docker environment.
   
4. Run `python manage.py createsuperuser` to create an admin user for your django admin panel

5. Run `python manage.py runserver` in the app directory

***


***

 _Kindly send me a mail at <jijakahn6@gmail.com> if you have any issues or suggestions_
 
 ***
 ***
