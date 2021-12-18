import socket
import json

SERVER = "127.0.0.1"
PORT = 64001


def display_results(response_data):
    response_json = json.loads(response_data)
    for line in response_json:
        print("{} - Game {} - {}".format(line['timestamp'],
                                         line['gameID'],
                                         line['message']))


def stat_client_menu():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    records = int(input("Fetch how many most recent log entries? "))
    message = {"fetchRecords": records}
    payload = json.dumps(message)
    client.connect((SERVER, PORT))
    client.sendall(bytes(payload, 'UTF-8'))
    in_data = client.recv(1024)
    display_results(in_data)
    client.close()


def run():
    while True:
        stat_client_menu()


if __name__ == '__main__':
    run()