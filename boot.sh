#!/bin/sh
venv/bin/activate
flask translate compile
exec gunicorn -b :5000 --access-logfile - --error-logfile - web:app