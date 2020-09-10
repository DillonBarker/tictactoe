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
        self.game_over = False
        
    def player_move(self, player, position):
        self.is_game_over()
        
        if self.board.the_board[position] == "-":
            self.board.the_board[position] = player.name
    
    def is_game_over(self):
        x = "-"
        if x in self.board.the_board:
            pass
        else:
            self.game_over = True

class TurnControl():
    def __init__(self):
        self.generator = [1,2]
        self.turn = 1
    
    def current_player(self):
        self.turn = self.generator[0]
        self.generator.pop(0)
        self.generator.append(self.turn)

class WinningConditions():
    
    def __init__(self, board):
        self.board = board
       
