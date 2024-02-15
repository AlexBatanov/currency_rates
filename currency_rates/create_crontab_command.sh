#!/bin/bash

PYTHON_PATH=$(which python3)
PROJECT_DIR=$(pwd)
DJANGO_SETTINGS="export DJANGO_SETTINGS_MODULE='currency_rates_project.settings';"

echo $DJANGO_SETTINGS $PYTHON_PATH $PROJECT_DIR/manage.py update_currency_rates
