import logging
from concurrent import futures

import grpc
from spelling_bee_pb2 import GameResponse, CheckWordResponse
from spelling_bee_pb2_grpc import SpellingBeeServicer, add_SpellingBeeServicer_to_server
from app.game_registry import GameRegistry
from app.factories import object_factory, standard_game_builder, easy_game_builder, multiplayer_game_builder


class GameServer(SpellingBeeServicer):
    def __init__(self):
        self.registry = GameRegistry.get_instance()
        self.factory = object_factory.ObjectFactory()
        self.factory.register_builder('standard', standard_game_builder.StandardGameBuilder())
        self.factory.register_builder('easy', easy_game_builder.EasyGameBuilder())

    def StartGame(self, request, context):
        # newGame = Game()
        newGame = self.factory.create(request.gameType)
        self.registry.add_game(newGame)
        return GameResponse(
            gameID=newGame.gameID,
            score=newGame.score,
            letters=str().join(newGame.letters),
            middleLetter=newGame.middleLetter
        )

    def CheckWord(self, request, context):
        game = self.registry.get_game(request.gameID)
        status, message = game.check_word(request.word)
        return CheckWordResponse(
            status=status,
            message=message,
            score=game.score
        )

    def NewMultiplayerGame(self, request, context):
        pass

    def JoinMultiplayerGame(self, request, context):
        pass

    def GetMultiplayerStatus(self, request, context):
        pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_SpellingBeeServicer_to_server(GameServer(), server)
    server.add_insecure_port('[::]:58008')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
