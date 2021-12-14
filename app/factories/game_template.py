from os import path
from random import randint
import json
import uuid
import pika
import datetime
from abc import ABC, abstractmethod


class GameTemplate(ABC):
    @property
    def min_word_length(self):
        pass

    def __init__(self):
        self.gameID = uuid.uuid4().hex
        self.score = 0
        self.validWords = {}
        self.guessedWords = []
        self.letters = ()
        self.middleLetter = ""

        with open(path.abspath("dictionaries/pangrams.json"), "r") as pangram_file:
            pangrams = json.load(pangram_file)
            rand_num = randint(0, len(pangrams))
            self.pangram = list(pangrams.keys())[rand_num]

        self.generate_valid_words()
        self.record_statistics("Game created")

    @abstractmethod
    def generate_valid_words(self):
        pass

    @abstractmethod
    def check_word(self, word, username):
        pass

    @abstractmethod
    def calculate_score(self, word):
        pass

    def record_statistics(self, message):
        log = {
            'timestame': datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S"),
            'gameID': self.gameID,
            'message': message
        }
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='spelling_bee_logs')
        channel.basic_publish(exchange='', routing_key='spelling_bee_logs', body=json.dumps(log))
        connection.close()

