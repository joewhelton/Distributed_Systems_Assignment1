import grpc
import spelling_bee_pb2_grpc as spelling_bee_pb2_grpc
import spelling_bee_pb2 as spelling_bee_pb2
from random import shuffle


class ClientGame:

    def __init__(self):
        self.username = "Joe"
        self.clientGame = None
        self.channel = grpc.insecure_channel('127.0.0.1:58008')
        self.stub = spelling_bee_pb2_grpc.SpellingBeeStub(self.channel)

    def start_game(self):
        response = self.stub.StartGame(spelling_bee_pb2.GameRequest(userName="Joe"))
        self.clientGame = {
            "gameID": response.gameID,
            "score": response.score,
            "letters": list(response.letters),
            "middleLetter": response.middleLetter
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

    def display_letters(self):
        display_string = ""
        for i in range(len(self.clientGame["letters"])):
            if i == len(self.clientGame["letters"])/2:
                display_string += "[{}] ".format(self.clientGame["middleLetter"])
            display_string += "{} ".format(self.clientGame["letters"][i])
        return display_string

    def shuffle_letters(self):
        shuffle(self.clientGame["letters"])

