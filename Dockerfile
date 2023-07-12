FROM python:3.9-slim

RUN adduser web

WORKDIR /app

# COPY requirements.txt requirements.txt
# RUN python -m venv venv
# RUN chmod +x venv/bin/activate

COPY Pipfile Pipfile.lock ./
RUN apt-get update
RUN apt-get update \
 && apt-get install unixodbc -y \
 && apt-get install unixodbc-dev -y \
 && apt-get install freetds-dev -y \
 && apt-get install freetds-bin -y \
 && apt-get install tdsodbc -y \
 && apt-get install --reinstall build-essential -y

# RUN apt-get install -y build-essential libpq-dev libxml2 libxml2-dev libxslt1.1 libxslt1-dev libffi-dev libz-dev

RUN python -m pip install --upgrade pip
RUN pip install -U pip
RUN pip install pipenv
RUN pipenv install --system --dev

# RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY web web
COPY alfin alfin
COPY boot.sh web.py config.py ./

USER web

# RUN chown -R web:web ./
# RUN chmod +x boot.sh

# ENV FLASK_APP web.py
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
