FROM python:3.7.4-slim-buster

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
#sudo docker-compose exec web_scraper_app bash
#ENTRYPOINT "python manage.py makemigrations web_scraper_app" && "python manage.py migrate"