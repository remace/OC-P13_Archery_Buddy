# OC P13 ArcheryBuddy

production address: [www.archerybuddy.tech](www.archerybuddy.tech)

## short description

this is a studies final project on helping archers on 3 manners:

- helping them choose between arrows for competitions
- recording practice data and "do the math"
- recording data on the equipment

* [user stories](docs/user_stories/user_stories.md)

## dependancies

[poetry dependancies](/pyproject.toml)

## setup and configuration 


### for a local development installation

```bash
# download this project and mandatory dependencies
"git clone" this project
install sqlite, nodejs and npm with your packet manager
install pipx with your packet manager
pipx install poetry
# install virtual environment and dependencies
cd OC-P13_ArcheryBuddy/ArcheryBuddy
poetry install
poetry shell
# migrations
./manage.py makemigrations accounts equipment records
./manage.py migrate
# for tailwind dev server
./manage.py tailwind install
./manage.py tailwind start &
# run the django server
./manage.py runserver

```

### for deployment

on a debian server VPS:
- update distribution and stuff
- install and configure postgresql server
- install poetry
```bash
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="/home/debian/.local/bin:$PATH"
    poetry config virtualenvs.in-project true
```
- télécharger le projet depuis github
- se placer dans le répertoire du projet, installer son environnement et ses dépendances: 
```bash
poetry install
./manage.py tailwind install
```
- don't forget to configure DJANGO_SETTINGS_MODULE and create the production settings file in settings package
``` python
# prod.py
from . import *

'''
Keys to give:
SECRET_KEY
ALLOWED_HOSTS
INTERNAL_IPS
DATABASES = {
    "default":{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':
        'USER':
        'PASSWORD':
        'HOST': '127.0.0.1',
        'PORT': '5432',
        }
    }
```
- collecter les fichiers statiques
```bash
./manage.py tailwind build
./manage.py collectstatic
```
- installer un serveur HTTP (ex: nginx)
- installer gunicorn puis le configurer: ```poetry add gunicorn```
- installer supervisr puis le configurer```sudo apt install supervisor```

## test procedure

same procedure than for development installation, then end with:
```bash
./manage.py test
```
to view code coverage, you can install coverage and use it: 
``` bash 
    poetry add coverage
    poetry run coverage run ./manage.py test
    poetry run coverage < out-protocol > -d < output path >
```



### linting and formatting options

I use mainly pylint to lint this project.

command to execute pylint at the root of the project:
```bash
pylint --rcfile=.pylintrc
```
it mainly disables "missing docstring" warnings.
