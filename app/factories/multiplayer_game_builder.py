from os import path
import json
import threading
import datetime
from app.factories.game_template import GameTemplate


class MultiplayerGame(GameTemplate):
    min_word_length = 4
    max_players = 2
    timeLimit = 180  # Time in seconds
    game_started = False
    game_ended = False

    def __init__(self):
        super().__init__()
        self.players = []
        self.end_time = datetime.datetime.now()
        self.playerScores = []
        self.shareCode = self.gameID[-5:]
        self.lock = threading.Lock()
        self.result = ""

    def generate_valid_words(self):
        self.letters = set(self.pangram)
        self.middleLetter = self.letters.pop()

        # Generate a list of valid words
        with open(path.abspath("dictionaries/words_dictionary.json"), "r") as dictionary_file:
            words = json.load(dictionary_file)

            for word in words:
                if set(word).issubset(self.letters.union(set(self.middleLetter))) \
                        and word.find(self.middleLetter) >= 0 \
                        and len(word) >= self.min_word_length:
                    self.validWords[word] = ""

    def check_word(self, word, username):
        if not self.game_started:
            return False, "Waiting for other player to join"
        if self.game_ended:
            return False, "Game has ended - {}".format(self.result)
        if self.get_remaining_time() == 0:
            self.finish_game()
            return False, "Game has ended - {}".format(self.result)
        if len(word) < self.min_word_length:
            return False, "Word is too short"
        if self.middleLetter not in word:
            return False, "Middle letter not used"
        if word not in list(self.validWords.keys()):
            return False, "Invalid word"

        self.lock.acquire()  # Make the critical section as short as possible for efficiency
        if word in self.guessedWords:
            return False, "Word already used"
        self.guessedWords.append(word)
        self.lock.release()

        wordScore = self.calculate_score(word)
        playerIndex = self.get_player_index(username)
        if playerIndex > -1:
            self.playerScores[playerIndex]["score"] += wordScore
            self.playerScores[playerIndex]["wordList"].append(word)
            self.record_statistics("{} scored {} with {}".format(username, wordScore, word))
            return True, "Scored {} with {}".format(wordScore, word)

    def calculate_score(self, word):
        score = 1
        if len(word) > self.min_word_length:
            score = len(word)
        if set(word) == self.letters.union(set(self.middleLetter)):
            score += 7  # Pangram bonus

        return score

    def add_player(self, playerName):
        self.lock.acquire()
        if len(self.playerScores) < 2:
            self.playerScores.append({
                "playerName": playerName,
                "score": 0,
                "wordList": []
            })
            self.record_statistics("{} joined game".format(playerName))
        if len(self.playerScores) == 2:
            self.record_statistics("Game started")
            self.game_started = True
            self.end_time = datetime.datetime.now() + datetime.timedelta(0, self.timeLimit)
        self.lock.release()

    def get_player_index(self, playerName):
        for index, item in enumerate(self.playerScores):
            if item.get("playerName") == playerName:
                return index
        return -1

    def get_remaining_time(self):
        if not self.game_started:
            return self.timeLimit
        if self.game_ended:
            return 0
        remaining_time = round((self.end_time - datetime.datetime.now()).total_seconds())
        if remaining_time <= 0:
            self.finish_game()
            return 0
        return remaining_time

    def finish_game(self):
        self.game_ended = True
        if self.playerScores[0]["score"] == self.playerScores[1]["score"]:
            self.result = "Game drew with {} points each".format(self.playerScores[0]["score"])
        elif self.playerScores[0]["score"] > self.playerScores[1]["score"]:
            self.result = "{} won with {} points to {}".format(self.playerScores[0]["playerName"],
                                                               self.playerScores[0]["score"],
                                                               self.playerScores[1]["score"])
        else:
            self.result = "{} won with {} points to {}".format(self.playerScores[1]["playerName"],
                                                               self.playerScores[1]["score"],
                                                               self.playerScores[0]["score"])
        self.record_statistics("Game ended - {}".format(self.result))


class MultiplayerGameBuilder:

    def __init__(self):
        pass

    def __call__(self):
        return MultiplayerGame()