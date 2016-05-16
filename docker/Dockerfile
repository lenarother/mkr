# 
# instructions to build the mkr_django Docker image
#
FROM python:2.7
MAINTAINER Kristian Rother <krother@academis.eu>
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN apt-get --yes update
RUN apt-get --yes install netcat
