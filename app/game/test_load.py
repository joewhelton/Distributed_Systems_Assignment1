import json
from os import path


def run():
    with open(path.relpath("../dictionaries/pangrams.json"), "r") as pangram_file:
        pangrams = json.load(pangram_file)

        print(pangrams)


if __name__ == '__main__':
    run()