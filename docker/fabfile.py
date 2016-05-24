
import os

def test():
    os.system('docker-compose run -w /code/hello_world/ django python manage.py test')

def load():
    os.system('docker-compose run -w /code/hello_world/ django python manage.py load_quotes --file_name ../quotes.txt')
