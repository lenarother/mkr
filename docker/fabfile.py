
import os

def bash():
    os.system('docker-compose run django bash')

def freeze():
    os.system('docker-compose run -w /code/hello_world/ django pip freeze')

def load():
    os.system('docker-compose run -w /code/hello_world/ django python manage.py load_quotes --file_name ../quotes.txt')

def shell():
    os.system('docker-compose run -w /code/hello_world/ django python manage.py shell')

def test():
    os.system('docker-compose run -w /code/hello_world/ django python manage.py test')
