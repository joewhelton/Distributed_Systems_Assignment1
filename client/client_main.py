from client.client_game import ClientGame


def game_menu(game):
    print(game.display_letters())
    newWord = input("Enter word - ")
    print("{} - Score {}".format(game.check_word(newWord), game.clientGame["score"]))


def run():
    game = ClientGame()
    game.start_game()
    while True:
        game_menu(game)


if __name__ == '__main__':
    run()