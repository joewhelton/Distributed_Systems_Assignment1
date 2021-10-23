from os import path
from random import randint, shuffle
import json
import uuid


class Game():

    def __init__(self):
        self.score = 0
        with open(path.abspath("dictionaries/pangrams.json"), "r") as pangram_file:
            pangrams = json.load(pangram_file)
            rand_num = randint(0, len(pangrams))
            self.pangram = list(pangrams.keys())[rand_num]
        self.letters = list(set(self.pangram))
        shuffle(self.letters)
        self.middleLetter = self.letters.pop(0)
        self.gameID = uuid.uuid4().hex

        # Generate a list of valid words
        self.validWords = {}
        with open(path.abspath("dictionaries/words_dictionary.json"), "r") as dictionary_file:
            words = json.load(dictionary_file)

            for word in words:
                if (set(word)).issubset(set(self.letters).union(set(self.middleLetter)))\
                        and word.find(self.middleLetter) >= 0\
                        and len(word) > 3:
                    self.validWords[word] = ""
