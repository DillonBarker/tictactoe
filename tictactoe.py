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
    def __init__(self, board):
        self.board = Board()

