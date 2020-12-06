FROM python:3.8-slim

RUN mkdir /app

WORKDIR /app

COPY . .

RUN cp forms/server_settings.py forms/local_settings.py

RUN pip install -r requirements.txt

#CMD python manage.py runserver 0.0.0.0:8000