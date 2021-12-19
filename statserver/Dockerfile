FROM ubuntu:latest

ADD stats_server.py /server/
ADD db.json /server/

WORKDIR /server/

EXPOSE 6400

RUN apt-get update -y

RUN apt-get install -y python3
RUN apt-get install -y python3-pip

RUN pip3 install pika
RUN pip3 install tinydb

CMD [ "python3", "/server/stats_server.py" ]
