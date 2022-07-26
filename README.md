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
git clone this project
install sqlite
install pipx with your packer manager
pipx install poetry
cd OC-P13_ArcheryBuddy/ArcheryBuddy
poetry install
poetry shell
./manage.py migrate
```

### for deployment

WIP

## test procedure

same procedure than for development installation, then end with:
```bash
./manage.py test
```