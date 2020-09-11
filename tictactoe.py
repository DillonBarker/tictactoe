class Board:
    def __init__(self):
        self.the_board = [["-","-","-"],
                          ["-","-","-"],
                          ["-","-","-"]]

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
        
    def player_move(self, player, x, y):
        self.is_game_over()
        
        if self.board.the_board[x][y] == "-":
            self.board.the_board[x][y] = player.name
    
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
    
    def __init__(self, game):
        self.player_1 = game.player_1
        self.player_2 = game.player_2
        self.board = game.board.the_board

    def row_win(self, player): 
        for x in range(len(self.board)): 
            self.win = player.name
            
            for y in range(len(self.board)): 
                if self.board[x][y] != player.name: 
                    self.win = 0    
                    continue

            if self.win == player.name: 
                return(self.win) 
        return(self.win) 

    def col_win(self, player): 
        for x in range(len(self.board)): 
            self.win = player.name
            
            for y in range(len(self.board)): 
                if self.board[y][x] != player.name: 
                    self.win = 0
                    continue

            if self.win == player.name: 
                return(self.win) 
        return(self.win) 
  
    def diag_win(self, player): 
        self.win = player.name
        
        for x in range(len(self.board)): 
            if self.board[x][x] != player.name: 
                self.win = 0
        return(self.win) 

    def is_it_won(self, player):
        self.row_win(player)
        if self.win != 0:
            return(self.win)
        self.col_win(player)
        if self.win != 0:
            return(self.win)
        self.diag_win(player)
        if self.win != 0:
            return(self.win)
        
            