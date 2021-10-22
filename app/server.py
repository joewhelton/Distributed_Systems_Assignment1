import logging
from concurrent import futures

import grpc
from spelling_bee_pb2 import GameResponse
from spelling_bee_pb2_grpc import SpellingBeeServicer, add_SpellingBeeServicer_to_server


class GameServer(SpellingBeeServicer):
    def StartGame(self, request, context):
        return GameResponse(gameID="Game created for {}".format(request.userName))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_SpellingBeeServicer_to_server(GameServer(), server)
    server.add_insecure_port('[::]:58008')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
