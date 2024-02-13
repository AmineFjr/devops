FROM python:3

WORKDIR /usr/src/app

COPY .. .

RUN pip3 install mysql-connector-python

CMD ["python3", "main.py"]