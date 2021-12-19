import socket
import threading
import pika
import json
from tinydb import TinyDB, Query


def ConsumerCallback(ch, method, properties, body):
    print("Logging message ", body)
    log_entry = json.loads(body)
    db.insert(log_entry)


def MessageConsumeThread():
    conn = pika.BlockingConnection(pika.ConnectionParameters('host.docker.internal'))
    channel = conn.channel()
    channel.queue_declare(queue='spelling_bee_logs')
    channel.basic_consume(queue='spelling_bee_logs',
                          auto_ack=True,
                          on_message_callback=ConsumerCallback
                          )
    channel.start_consuming()


def GetLastXEntries(x):
    entries = []
    od = sorted(db.all(), key=lambda k: k['timestamp'])
    for j in range((x*-1), 0):
        entries.append(od[j])
    return entries


class ClientThread(threading.Thread):

    def __init__(self, client_address, client_socket):
        threading.Thread.__init__(self)
        self.c_socket = client_socket

    def run(self):
        print("Connection from : ", clientAddress)
        data = self.c_socket.recv(2048).decode()
        request = json.loads(data)
        response_json = GetLastXEntries(request['fetchRecords'])
        response_payload = json.dumps(response_json)
        self.c_socket.send(bytes(response_payload, 'UTF-8'))
        print("Sent ", request['fetchRecords'], " records to", clientAddress)


HOST = '0.0.0.0'
PORT = 6400

print("Server starting...")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
print("Server started")

print("MQ Consumer service starting...")
messageListenerThread = threading.Thread(target=MessageConsumeThread, args=())
messageListenerThread.start()
print("MQ Consumer service started")

print("Initialising data store...")
db = TinyDB('db.json')  # If I had more time I'd use a DAO here
print("Data store initialised")

print("Waiting for client request..")

while True:
    server.listen(1)
    my_socket, clientAddress = server.accept()
    new_thread = ClientThread(clientAddress, my_socket)
    new_thread.start()