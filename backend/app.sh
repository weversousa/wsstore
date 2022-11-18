#!/bin/sh

pip install --upgrade pip
pip install -r ./requirements.txt
flask create-tables
flask --app=./app/ --debug run --host='0.0.0.0' --port=5000