import logging
from concurrent import futures

import grpc
from spelling_bee_pb2 import GameResponse, CheckWordResponse, NewMultiplayerGameResponse, JoinMultiplayerGameResponse, CheckWordMultiplayerResponse, NewMultiplayerGameResponse
from spelling_bee_pb2_grpc import SpellingBeeServicer, add_SpellingBeeServicer_to_server
from app.game_registry import GameRegistry
from app.factories import object_factory, standard_game_builder, easy_game_builder, multiplayer_game_builder


class GameServer(SpellingBeeServicer):
    def __init__(self):
        self.registry = GameRegistry.get_instance()
        self.factory = object_factory.ObjectFactory()
        self.factory.register_builder('standard', standard_game_builder.StandardGameBuilder())
        self.factory.register_builder('easy', easy_game_builder.EasyGameBuilder())
        self.factory.register_builder('multiplayer', multiplayer_game_builder.MultiplayerGameBuilder())

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
        newGame = self.factory.create('multiplayer')
        newGame.add_player(request.userName)
        self.registry.add_game(newGame)
        return NewMultiplayerGameResponse(
            gameID=newGame.gameID,
            scores=newGame.playerScores,
            letters=str().join(newGame.letters),
            middleLetter=newGame.middleLetter,
            shareCode=newGame.shareCode,
            timeLimit=newGame.timeLimit
        )

    def JoinMultiplayerGame(self, request, context):
        gameID = ""
        scores = []
        letters = ""
        middleLetter = ""
        timeLimit = 0
        errorMessage = ""
        status, game = self.registry.get_game_by_sharecode(request.shareCode)
        if not status:
            errorMessage = "No game found for that code"
        elif game.playerScores[0].get("playerName") == request.userName:
            errorMessage = "Username already in use for that game"
        elif len(game.playerScores) > 1:
            errorMessage = "Game full"
        else:
            game.add_player(request.userName)
            gameID = game.gameID
            scores = game.playerScores
            letters = game.letters
            middleLetter = game.middleLetter
            timeLimit = game.timeLimit

        return JoinMultiplayerGameResponse(
            gameID=gameID,
            scores=scores,
            letters=str().join(letters),
            middleLetter=middleLetter,
            timeLimit=timeLimit,
            errorMessage=errorMessage
        )

    def CheckWordMultiplayer(self, request, context):
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
