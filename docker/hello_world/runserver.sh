#!/bin/bash

# check whether postgres is ready
bash /code/hello_world/wait_for_db.sh

python /code/hello_world/manage.py migrate
python /code/hello_world/manage.py runserver 0.0.0.0:8000