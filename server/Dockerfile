FROM python:3.7.1-slim

RUN apt-get update -qq
RUN apt-get install -y mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8 build-essential g++ python-dev wget bzip2 swig && \
        rm -rf /var/lib/apt/lists/*

RUN pip install typed-ast mecab-python3

WORKDIR /app

RUN pip install flask flask-cors flask-sqlalchemy Flask-Migrate sqlalchemy psycopg2 uwsgi
