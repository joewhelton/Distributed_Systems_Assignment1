from os import path
from random import randint
import json
import uuid


class Game:

    def __init__(self):
        self.score = 0
        with open(path.abspath("dictionaries/pangrams.json"), "r") as pangram_file:
            pangrams = json.load(pangram_file)
            rand_num = randint(0, len(pangrams))
            self.pangram = list(pangrams.keys())[rand_num]
        self.letters = set(self.pangram)
        self.middleLetter = self.letters.pop()
        self.gameID = uuid.uuid4().hex
        self.guessedWords = []

        # Generate a list of valid words
        self.validWords = {}
        with open(path.abspath("dictionaries/words_dictionary.json"), "r") as dictionary_file:
            words = json.load(dictionary_file)

            for word in words:
                if set(word).issubset(self.letters.union(set(self.middleLetter)))\
                        and word.find(self.middleLetter) >= 0\
                        and len(word) > 3:
                    self.validWords[word] = ""

    def check_word(self, word):
        if len(word) < 4:
            return False, "Word is too short"
        if self.middleLetter not in word:
            return False, "Middle letter not used"
        if word not in list(self.validWords.keys()):
            return False, "Invalid word"
        if word in self.guessedWords:
            return False, "Word already used"

        self.score += self.calculate_score(word)
        self.guessedWords.append(word)
        return True, "Good stuff"

    def calculate_score(self, word):
        score = 1
        if len(word) > 4:
            score = len(word)
        if set(word) == self.letters.union(set(self.middleLetter)):
            score += 7  # Pangram bonus

        return score

