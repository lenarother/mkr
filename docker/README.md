
# Docker command notes

## Terminology

* Dockerfile -> recipe to create an image from another image
* image -> does nothing by itself, you can create many instances (containers) from it.

## Build a container from scratch using a Dockerfile

    docker build -t krother/mkr_django:v1 .

## Starting Docker container in interactive mode

    docker run -i -t ubuntu /bin/bash

## Starting service on Docker container 

    docker run -d -P training/webapp python app.py

## Set default command for startup in a Dockerfile:

    CMD python app.py

## Run commands via docker-compose, so that changes apply to local file system

    docker-compose run django django-admin startproject hello_world
    docker-compose run -w /code/hello_world django python manage.py startapp hello
    docker-compose run -w /code/hello_world django python manage.py makemigrations
    docker-compose run -w /code/hello_world django python manage.py migrate
    docker-compose run -w /code/hello_world django python manage.py shell
    

## References

* https://docs.docker.com/compose/overview/
* https://docs.docker.com/compose/django/
* https://docs.docker.com/compose/compose-file/
