from client.client_game import ClientGame

gameTypes = {
    1: "standard",
    2: "easy"
}

def setup_menu():
    name = input("Enter a username - ")
    gameType = input("(1) - Standard    (2) - Easy ")
    return name, gameTypes[int(gameType)]


def game_menu(game):
    print(game.display_letters())
    newWord = input("Enter word - ")
    print("{} - Total {}".format(game.check_word(newWord), game.clientGame["score"]))


def run():
    name, gameType = setup_menu()
    game = ClientGame(name)
    game.start_game(gameType)
    while True:
        game_menu(game)


if __name__ == '__main__':
    run()