FROM python:3.9-alpine3.16

COPY  requirements.txt /temp/requirements.txt
COPY service /service
WORKDIR /servise
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

# Upgrade pip
RUN /usr/local/bin/python -m pip install --upgrade pip


RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password servise-user

USER servise-user

