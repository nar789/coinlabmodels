FROM ubuntu:bionic
LABEL version='1.0.0'

USER root

WORKDIR /app

COPY . /app

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get autoremove
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade pip

RUN pip3 install --trusted-host pypi.python.org -r ./core/py/requirements.txt