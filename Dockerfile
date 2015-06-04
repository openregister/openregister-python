FROM python:3.4.2

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements_test.txt /usr/src/app/
RUN pip install -r requirements_test.txt

COPY . /usr/src/app
