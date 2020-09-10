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
        

    def player_move(self, player, position):
        self.board.the_board[position] = player.name

class TurnControl():
    def __init__(self):
        self.generator = [1,2]
        self.turn = 1
    
    def current_player(self):
        self.turn = self.generator[0]
        self.generator.pop(0)
        self.generator.append(self.turn)