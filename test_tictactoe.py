import pytest
from tictactoe import *


def test_board_class():
    board = Board()
    assert board.the_board == ["-","-","-",
                               "-","-","-",
                               "-","-","-"]
    assert board.the_board != ["dog","-","-",
                                 "-","-","-",
                                 "-","-","-"]

def test_game_class():
    board = Board()
    game = Game(board)
    assert game.board.the_board == ["-","-","-",
                                    "-","-","-",
                                    "-","-","-"]
    assert isinstance(game.board, Board) 

def test_player_class():
    player_1 = Player("X")
    assert player_1.name == "X"
    player_2 = Player("O")
    assert player_2.name == "O"