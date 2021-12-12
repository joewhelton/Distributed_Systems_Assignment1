import grpc

import spelling_bee_pb2_grpc as spelling_bee_pb2_grpc
import spelling_bee_pb2 as spelling_bee_pb2


def run():
    channel = grpc.insecure_channel('127.0.0.1:58008')
    stub = spelling_bee_pb2_grpc.SpellingBeeStub(channel)

    testResponse = stub.JoinMultiplayerGame(spelling_bee_pb2.JoinMultiplayerGameRequest(userName="Dave", shareCode="7ed11"))

    print(testResponse)


if __name__ == '__main__':
    run()