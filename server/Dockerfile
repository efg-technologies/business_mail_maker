FROM python:3.7.1-slim

RUN apt-get update -qq
RUN apt-get install -y mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8 build-essential g++ python-dev wget bzip2 swig && \
        rm -rf /var/lib/apt/lists/*

RUN pip install typed-ast mecab-python3

ADD ./lib/CRF++-0.58.tar.gz /tmp/
ADD ./lib/cabocha-0.69.tar.bz2 /tmp/
RUN cd /tmp/CRF++-0.58 && ./configure && make && make install && ldconfig
RUN cd /tmp/cabocha-0.69 && ./configure --with-charset=utf8 --enable-utf8-only && make && make install && ldconfig
RUN cd /tmp/cabocha-0.69/python && python setup.py install
RUN rm -rf /tmp/*

WORKDIR /app

RUN pip install flask flask-cors flask-sqlalchemy Flask-Migrate sqlalchemy psycopg2 uwsgi
