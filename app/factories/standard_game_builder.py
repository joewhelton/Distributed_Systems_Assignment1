from os import path
from random import randint
import json
import uuid
from app.factories.game_template import GameTemplate


class StandardGame(GameTemplate):
    min_word_length = 4

    def __init__(self):
        super().__init__()

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
        if len(word) < self.min_word_length:
            return False, "Word is too short"
        if self.middleLetter not in word:
            return False, "Middle letter not used"
        if word not in list(self.validWords.keys()):
            return False, "Invalid word"
        if word in self.guessedWords:
            return False, "Word already used"

        wordScore = self.calculate_score(word)
        self.score += wordScore
        self.guessedWords.append(word)
        return True, "Good stuff, word scored {}".format(wordScore)

    def calculate_score(self, word):
        score = 1
        if len(word) > self.min_word_length:
            score = len(word)
        if set(word) == self.letters.union(set(self.middleLetter)):
            score += 7  # Pangram bonus

        return score


class StandardGameBuilder:

    def __init__(self):
        pass

    def __call__(self):
        return StandardGame()