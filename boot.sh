#!/bin/sh
#venv/bin/activate
NUM_WORKERS=3
TIMEOUT=600
flask translate compile
#exec gunicorn -b :5000 --access-logfile - --error-logfile - web:app
exec gunicorn -b :5000 --access-logfile - --error-logfile - web:app \
--workers $NUM_WORKERS \
--timeout $TIMEOUT
