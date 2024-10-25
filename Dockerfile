
FROM python:3.9-slim


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /code


RUN apt-get update \
    && apt-get install -y postgresql-client


COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY . /code/


CMD [ "gunicorn", "--bind" "0.0.0.0:8000", "DogExercise.wsgi:application"]
