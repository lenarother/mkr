
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

## References

* https://docs.docker.com/compose/overview/
* https://docs.docker.com/compose/django/
* https://docs.docker.com/compose/compose-file/
