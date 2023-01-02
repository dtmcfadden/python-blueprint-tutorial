# From medium article

https://medium.com/thedevproject/flask-blueprints-complete-tutorial-to-fully-understand-how-to-use-it-767f7433a02e

# Repository

https://github.com/felipeflorencio/StartingWithBlueprintTutorial

# BaseFlaskProject

This is the basic Flask project that I use to start my projects, here I have the basic setup to work with flask

## Before start add these to a .env file

FLASK_APP=app.py
APP_SETTINGS=config.DevelopmentConfig
FLASK_DEBUG=True

# Virtual Environment Setup With Windows

python -m venv .venv

.venv\Scripts\activate.bat

'deactivate' to exit

# pip functions

## install packages from requirements.txt

pip install -r requirements.txt

## Check for outdated packages

pip list -o

## Update package

pip install [package_name] --upgrade

## Update requirements.txt file

pip freeze > requirements.txt

# flask-sqlalchemy

https://flask-migrate.readthedocs.io/en/latest/

## initialize - only done once

flask db init

## migrate - add migration entry

flask db migrate -m "Initial migration"

## upgrade - apply changes

flask db upgrade

## help

flask db --help
