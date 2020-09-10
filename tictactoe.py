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
        self.player_1 = Player("X")
        self.player_2 = Player("O")

    def player_move(self, player, position):
        self.board.the_board[position] = player.name

class Turn():
   def __init__(self, player_1, player_2):
       self.player_1 = player_1
       self.player_2 = player_2 
