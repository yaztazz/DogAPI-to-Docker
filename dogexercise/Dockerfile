
FROM python:3.9-slim


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /code


RUN apt-get update \
    && apt-get install -y postgresql-client postgresql-server-dev-all gcc python3-dev libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt /code/
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt


COPY . /code/


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "dogexercise.wsgi:application"]
