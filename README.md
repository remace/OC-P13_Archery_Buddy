# OC P13 ArcheryBuddy

production address: Not yet deployed

WIP:
* [Conception](docs/user_stories/user_stories.md)

## short description

this is a studies final project on helping archers on 3 manners:

- helping them choose between arrows for competitions
- recording practice data and "do the math"
- recording data on the equipment

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

WIP

## test procedure

same procedure than for development installation, then end with:
```bash
./manage.py test
```


### linting and formatting options

I use mainly pylint to lint this project, and black.

command to execute pylint at the root of the project:
```bash
pylint --rcfile=.pylintrc
```
it mainly disables "missing docstring" warnings.

To format my code, I use black with default parameters:

```bash
black ArcheryBuddy
```
