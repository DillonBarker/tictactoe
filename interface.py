from tictactoe import Game

class PlayGame:
    def __init__(self):
        self.game = Game()
    
    def start_game(self):
        while True:
            print("Welcome to TicTacToe by Dillon Barker")
            print(*self.game.board.the_board, sep="\n")
            print("Make a move " + str(self.game.turncontrol.turn.name))
            for num in [1,2,3,4,5,6,7,8,9]:
                y = input("Enter an y coord: ")
                x = input("Enter an x coord: ")
                self.game.player_move(int(y), int(x))
                if self.game.game_over == True:
                    break
                    print(str(self.game.winningconditions.win) + " Wins!!"
                # else:
                #     print(*self.game.board.the_board, sep="\n")
                #     print("Make a move " + str(self.game.turncontrol.turn.name))
               
                
