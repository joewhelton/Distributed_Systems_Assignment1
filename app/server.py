import logging
from concurrent import futures

import grpc
from spelling_bee_pb2 import GameResponse
from spelling_bee_pb2_grpc import SpellingBeeServicer, add_SpellingBeeServicer_to_server
from app.game.game import Game
from app.game_registry import GameRegistry


class GameServer(SpellingBeeServicer):
    def __init__(self):
        self.registry = GameRegistry.get_instance()

    def StartGame(self, request, context):
        newGame = Game()
        self.registry.add_game(newGame)
        return GameResponse(
            gameID=newGame.gameID,
            score=newGame.score,
            letters=str().join(newGame.letters),
            middleLetter=newGame.middleLetter
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_SpellingBeeServicer_to_server(GameServer(), server)
    server.add_insecure_port('[::]:58008')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
