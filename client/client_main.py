from client.client_game import ClientGame

gameTypes = {
    1: "standard",
    2: "easy",
    3: "multiplayer"
}


def format_multiplayer_scores(playerScores):
    # print(playerScores)
    # print(playerScores[0])
    for player in playerScores:
        print("{}'s total: {}".format(player.playerName, player.score))


def print_multiplayer_status(playerScores):
    pass


def setup_menu():
    name = input("Enter a username - ")
    gameType = input("(1) - Standard    (2) - Easy    (3) - Multiplayer ")
    return name, gameTypes[int(gameType)]


def multiplayer_menu():
    shareCode = ""
    newOrJoin = input("Start (N)ew game or (J)oin existing? ")
    if newOrJoin == "J":
        shareCode = input("Enter your sharecode - ")
    return newOrJoin, shareCode


def game_menu(game):
    print(game.display_letters())
    newWord = input("Enter word - ")
    if newWord == "1":
        pass
    else:
        if game.clientGame["gameType"] == "multiplayer":
            message = game.check_word_multiplayer(newWord)
            print(message)
            format_multiplayer_scores(game.clientGame["scores"])
        else:
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

    if gameType == "multiplayer":
        print("Enter (1) at any time to see game status")

    while True:
        game_menu(game)


if __name__ == '__main__':
    run()