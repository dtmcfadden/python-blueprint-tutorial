# From medium article

https://medium.com/thedevproject/flask-blueprints-complete-tutorial-to-fully-understand-how-to-use-it-767f7433a02e

# Repository

https://github.com/felipeflorencio/StartingWithBlueprintTutorial

# BaseFlaskProject

This is the basic Flask project that I use to start my projects, here I have the basic setup to work with flask

## Before start export this variables when on test or production according to your environment

export FLASK_APP=app.py
export APP_SETTINGS=config.DevelopmentConfig

# Virtual Environment Setup With Windows

python -m venv .venv

.venv\Scripts\activate.bat

# pip functions

## install packages from requirements.txt

pip install -r requirements.txt

## Check for outdated packages

pip list -o

## Update package

pip install [package_name] --upgrade

## Update requirements.txt file

pip freeze > requirements.txt
