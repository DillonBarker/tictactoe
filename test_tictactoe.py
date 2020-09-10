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
