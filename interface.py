from tictactoe import *

class PlayGame:
    def __init__(self):
        self.game = Game()
    
    def start_game(self):
        while self.game.game_over == False:
            print("Welcome to TicTacToe by Dillon Barker")
            print(self.game.board.the_board)
            print("Make a move " + str(self.game.turncontrol.turn.name))
            for x in [1,2,3,4,5,6,7,8,9]:
                x = input("Enter an x coord: ")
                y = input("Enter an y coord: ")
                self.game.player_move(int(x), int(y))
                print(self.game.board.the_board)
                print("Make a move " + str(self.game.turncontrol.turn.name))
                if self.game.game_over == True:
                    break
                
