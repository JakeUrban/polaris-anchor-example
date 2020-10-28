FROM python:3.7-slim-buster

RUN apt-get update && apt-get install -y build-essential
WORKDIR /home
RUN mkdir /home/data
COPY app /home/app/
COPY .env requirements.txt /home/

RUN pip install -r requirements.txt && python /home/app/manage.py collectstatic --no-input

CMD python /home/app/manage.py runserver --nostatic 0.0.0.0:8000
