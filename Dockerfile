FROM python:3.9-slim

RUN adduser gis

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m venv venv 
RUN chmod +x venv/bin/activate

RUN python -m pip install --upgrade pip 
RUN pip install -r requirements.txt 
RUN pip install gunicorn

COPY web web
COPY parser parser
COPY boot.sh web.py config.py ./

RUN chown -R gis:gis ./
RUN chmod +x boot.sh
USER gis

# ENV FLASK_APP web.py
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
