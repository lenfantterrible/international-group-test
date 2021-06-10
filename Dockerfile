# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0


COPY . .

# install dependencies
WORKDIR /app/international-group-test

RUN pip install -r requirements.txt

# copy project


# run gunicorn
CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT