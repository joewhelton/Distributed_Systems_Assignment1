import grpc
import spelling_bee_pb2_grpc as spelling_bee_pb2_grpc
import spelling_bee_pb2 as spelling_bee_pb2
from random import shuffle


class ClientGame:

    def __init__(self, username):
        self.username = username
        self.clientGame = None
        self.channel = grpc.insecure_channel('127.0.0.1:58008')
        self.stub = spelling_bee_pb2_grpc.SpellingBeeStub(self.channel)

    def start_game(self, gameType):
        response = self.stub.StartGame(spelling_bee_pb2.GameRequest(userName=self.username, gameType=gameType))
        self.clientGame = {
            "gameID": response.gameID,
            "score": response.score,
            "letters": list(response.letters),
            "middleLetter": response.middleLetter,
            "gameType": gameType
        }
        self.shuffle_letters()

    def check_word(self, word):
        response = self.stub.CheckWord(spelling_bee_pb2.CheckWordRequest(
            gameID=self.clientGame["gameID"],
            word=word
        ))
        if response.status:
            self.clientGame["score"] = response.score
        return response.message

    def new_multiplayer_game(self):
        response = self.stub.NewMultiplayerGame(spelling_bee_pb2.NewMultiplayerGameRequest(userName=self.username))
        self.clientGame = {
            "gameID": response.gameID,
            "scores": response.scores,
            "letters": list(response.letters),
            "middleLetter": response.middleLetter,
            "shareCode": response.shareCode,
            "timeLimit": response.timeLimit,
            "gameType": 3
        }
        self.shuffle_letters()

    def join_multiplayer_game(self, shareCode):
        response = self.stub.JoinMultiplayerGame(spelling_bee_pb2.JoinMultiplayerGameRequest(userName=self.username, shareCode=shareCode))
        if response.errorMessage != "":
            return False, response.errorMessage
        self.clientGame = {
            "gameID": response.gameID,
            "scores": response.scores,
            "letters": list(response.letters),
            "middleLetter": response.middleLetter,
            "timeLimit": response.timeLimit,
            "gameType": 3
        }
        return True, "Game joined"

    def display_letters(self):
        display_string = ""
        for i in range(len(self.clientGame["letters"])):
            if i == len(self.clientGame["letters"])/2 and self.clientGame["middleLetter"] != "":
                display_string += "[{}] ".format(self.clientGame["middleLetter"])
            display_string += "{} ".format(self.clientGame["letters"][i])
        return display_string

    def shuffle_letters(self):
        shuffle(self.clientGame["letters"])


