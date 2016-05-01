

docker-compose run -w /code/hello_world django python manage.py migrate

docker-compose run -w /code/hello_world django python manage.py createsuperuser --username root --email root@testsrv.er 

docker-compose up
