import pytest
from tictactoe import *

class Helpers:
    def add_players_and_start_game(self):
        board = Board()
        player_1 = Player("X")
        player_2 = Player("O")
        self.game = Game(board, player_1, player_2)