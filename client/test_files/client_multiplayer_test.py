import grpc

import spelling_bee_pb2_grpc as spelling_bee_pb2_grpc
import spelling_bee_pb2 as spelling_bee_pb2


def run():
    channel = grpc.insecure_channel('127.0.0.1:58008')
    stub = spelling_bee_pb2_grpc.SpellingBeeStub(channel)

    testResponse = stub.NewMultiplayerGame(spelling_bee_pb2.NewMultiplayerGameRequest(userName="Joe"))

    print(testResponse)


if __name__ == '__main__':
    run()