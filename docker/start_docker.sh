
# stop and remove everything
docker-compose stop
docker ps -a | awk '{print $1}' | xargs --no-run-if-empty docker rm

# start the system
docker-compose create
docker-compose start db
docker-compose start django

docker-compose run -w /code/hello_world/ django python manage.py test
if [ $? -ne 0 ]; then
	# exit code of last command != 0
    echo "CRITICAL: django tests broken! Stopping."
    docker-compose stop
else
	# watch logs forever
    docker-compose logs -f
fi

