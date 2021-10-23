from client.client_game import ClientGame


def game_menu(game):
    game.display_letters()
    newWord = input("Enter word - ")


def run():
    game = ClientGame()
    game.start_game()
    while True:
        game_menu(game)


if __name__ == '__main__':
    run()