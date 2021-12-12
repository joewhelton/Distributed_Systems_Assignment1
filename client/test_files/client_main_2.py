from client.client_game import ClientGame

gameTypes = {
    1: "standard",
    2: "easy",
    3: "multiplayer"
}


def setup_menu():
    name = input("Enter a username - ")
    gameType = input("(1) - Standard    (2) - Easy    (3) - Multiplayer ")
    return name, gameTypes[int(gameType)]


def multiplayer_menu():
    shareCode = ""
    newOrJoin = input("Start (N)ew game or (J)oin existing?")
    if newOrJoin == "J":
        shareCode = input("Enter your sharecode")
    return newOrJoin, shareCode


def game_menu(game):
    print(game.display_letters())
    newWord = input("Enter word - ")
    print("{} - Total {}".format(game.check_word(newWord), game.clientGame["score"]))


def run():
    name, gameType = setup_menu()
    game = ClientGame(name)
    if gameType != "multiplayer":
        game.start_game(gameType)
    else:
        status = False
        while not status:
            newOrJoin, shareCode = multiplayer_menu()
            if newOrJoin == "N":
                game.new_multiplayer_game()
                status = True
                print("Game created, your share code is {}", game.clientGame.get('shareCode'))
            else:
                status, message = game.join_multiplayer_game(shareCode)
                print(message)
    while True:
        game_menu(game)


if __name__ == '__main__':
    run()