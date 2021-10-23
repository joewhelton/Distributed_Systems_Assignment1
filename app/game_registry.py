class GameRegistry:
    __instance = None

    def __init__(self):
        if GameRegistry.__instance is not None:
            raise Exception("This is a singleton")
        else:
            GameRegistry.__instance = self
        self.games = {}
        self.instance = None

    @staticmethod
    def get_instance():
        if GameRegistry.__instance is None:
            GameRegistry()
        return GameRegistry.__instance

    def add_game(self, game):
        self.games[game.gameID] = game

    def get_game(self, gameID):
        return self.games[gameID]
