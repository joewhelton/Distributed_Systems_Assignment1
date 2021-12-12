import threading


class GameRegistry:
    __instance = None

    def __init__(self):
        if GameRegistry.__instance is not None:
            raise Exception("This is a singleton")
        else:
            GameRegistry.__instance = self
        self.lock = threading.Lock()
        self.games = {}
        self.instance = None

    @staticmethod
    def get_instance():
        if GameRegistry.__instance is None:
            with threading.Lock():
                if GameRegistry.__instance is None:
                    GameRegistry()
        return GameRegistry.__instance

    def add_game(self, game):
        self.lock.acquire()
        self.games[game.gameID] = game
        self.lock.release()

    def get_game(self, gameID):
        return self.games[gameID]

    def get_game_by_sharecode(self, shareCode):
        for key, value in self.games.items():
            if value.shareCode == shareCode:
                return True, self.get_game(value.gameID)

        return False, ""

