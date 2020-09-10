class Board:
    def __init__(self):
        self.the_board = ["-","-","-",
                          "-","-","-",
                          "-","-","-"]

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class Game():
    def __init__(self, board, player_1, player_2):
        self.board = Board()
        self.player_1 = Player("X")
        self.player_2 = Player("O")

