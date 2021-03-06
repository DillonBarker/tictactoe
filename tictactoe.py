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
    def __init__(self):
        self.board = Board()
        self.player_1 = Player("X")
        self.player_2 = Player("O")
        self.game_over = False
        self.turncontrol = TurnControl(self.player_1, self.player_2)
        self.winningconditions = WinningConditions(self.board, self.player_1, self.player_2)
        
    def player_move(self, x, y):
        self.is_game_over()
        
        if self.board.the_board[x][y] == "-":
            self.board.the_board[x][y] = self.turncontrol.turn.name
            self.winningconditions.is_it_won(self.turncontrol.turn)
            self.turncontrol.current_player()
    
    def is_game_over(self):
        blank = "-"
        if blank in self.board.the_board:
            pass
        elif self.winningconditions.win == "X" or self.winningconditions.win == "O":
            self.game_over = True
        

class TurnControl():
    def __init__(self, player_1, player_2):
        self.generator = [player_1, player_2]
        self.turn = player_1
    
    def current_player(self):
        self.turn = self.generator[0]
        self.generator.pop(0)
        self.generator.append(self.turn)
        self.turn = self.generator[0]

class WinningConditions():
    def __init__(self, board, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = board.the_board
        self.win = 0

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
            self.gain_point(player)
        self.col_win(player)
        if self.win != 0:
            self.gain_point(player)
        self.diag_win(player)
        if self.win != 0:
            self.gain_point(player)
        
    def gain_point(self, player):
        player.score += 1
        return(self.win)

