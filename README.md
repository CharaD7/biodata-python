# biodata-python
**An Biodata app with MDB bootstrap  written in python==3.8 and Djanago==2.2**

This app runs on a docker container with celery and rabbitmq handling some taks/services within the app. To fully delpoy and use the app, simply follow the guidelines below.

## Getting Started

- First, clone the repo [here](https://github.com/CharaD7/biodata-python.git)
- Extract data and change into the cloned directory. Now open the directory with your prefered text editor or IDE. You can as well do so by just opening the extracted folder with any prefered editor or IDE of your choice.
- Download and install [docker](https://hub.docker.com/) based on your OS platform. Be sure to have a minimum RAM of 4gb to be able to run docker. Read the OS-based [documentation](https://docs.docker.com/) here to be able to fully run docker on your system.
-  Build the docker file by running the `docker build .` command in the root directory. This will build and install all necessary dependencies needed to run the app in the docker image.
-  Install the custom mysql client in the root directory by running `docker-compose run "pip install mysqlclient-1.4.4-cp38-cp38-win32.whl"`
-  Download any MySQL database server for running on the system 