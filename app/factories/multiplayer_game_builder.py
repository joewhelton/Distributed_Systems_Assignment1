from os import path
import json
from app.factories.game_template import GameTemplate


class MultiplayerGame(GameTemplate):
    min_word_length = 4
    max_players = 2
    time_limit = 180  # Time in seconds

    def __init__(self):
        super().__init__()
        self.players = []
        self.start_time = ""

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

    def check_word(self, word):
        pass

    def calculate_score(self, word):
        score = 1
        if len(word) > self.min_word_length:
            score = len(word)
        if set(word) == self.letters.union(set(self.middleLetter)):
            score += 7  # Pangram bonus

        return score


class MultiplayerGameBuilder:

    def __init__(self):
        pass

    def __call__(self):
        return MultiplayerGame()