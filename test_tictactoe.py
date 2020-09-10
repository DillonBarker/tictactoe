import pytest
from tictactoe import *


def test_board_class():
    board = Board()
    assert board.the_board == ["-","-","-",
                                "-","-","-",
                                "-","-","-"]
