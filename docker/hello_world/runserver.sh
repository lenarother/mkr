#!/bin/bash

# Service Health Check

# script to check DB availability before starting django
# from: https://howchoo.com/g/y2y1mtkznda/getting-started-with-docker-compose-and-django

# wait for mysql to be ready
nc -z db 5432
n=$?
while [ $n -ne 0 ]; do
    sleep 1
    nc -z db 5432
    n=$?
done

python /code/hello_world/manage.py migrate
python /code/hello_world/manage.py runserver 0.0.0.0:8000