#!/bin/bash

# Service Health Check

# script to check DB availability before starting django
# from: https://howchoo.com/g/y2y1mtkznda/getting-started-with-docker-compose-and-django

# wait for mysql to be ready
nc -z mysql 3306
n=$?
while [ $n -ne 0 ]; do
    sleep 1
    nc -z mysql 3306
    n=$?
done

python manage.py runserver 0.0.0.0:8000