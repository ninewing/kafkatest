FROM python:3.8

RUN pip install --no-cache-dir kafka-python==2.0.2

WORKDIR /usr/app/src
COPY . .

CMD [ "python", "./producer.py"]