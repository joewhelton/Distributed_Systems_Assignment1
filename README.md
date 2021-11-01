#Distributed Systems Programming
##Assignment 1

###Running
1. Run app/server.py
2. Run client/client_main.py

###Patterns Used
####Singleton
The Game Registry uses a singleton pattern to ensure that only one instance of the GameRegistry class will ever be created.  The Game Registry is responsible for tracking all games created by the Server so it is important that these all be located in one place.  This will become vital if/when the system is expanded upon to allow multiple concurrent users.
```
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
```
Note - this code is not thread safe.  This will be added if multiple users becomes possible in a leter version.
####Factory
The Factory pattern has been implemented to manage the different game types (currently Standard and Easy).
* The Object Factory is initialised in the constructor of the GameServer and the builder classes are registered with it
```
        self.factory = object_factory.ObjectFactory()
        self.factory.register_builder('standard', standard_game_builder.StandardGameBuilder())
        self.factory.register_builder('easy', easy_game_builder.EasyGameBuilder())
``` 
* When the StartGame method is called, the gameType parameter of the GameRequest message is used to create a new game of the appropriate type 
`newGame = self.factory.create(request.gameType)`
* The GameTemplate class is used as a base class for the different game types.  Code common to all game types is handled in the constructor method, while subsequent methods are declared as Abstract, as their implementations may differ between types of game
* The two types of game are Standard (standard rules) and Easy (minimum number of letters is three instead of four, and there is no middle letter which has to be used)