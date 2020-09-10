import pytest
from tictactoe import *


class TestBoard:
    def test_board_class(self):
        board = Board()
        assert board.the_board == ["-","-","-",
                                "-","-","-",
                                "-","-","-"]
        assert board.the_board != ["dog","-","-",
                                    "-","-","-",
                                    "-","-","-"]

class TestGame:
    def test_game_class(self):
        board = Board()
        game = Game(board)
        assert game.board.the_board == ["-","-","-",
                                        "-","-","-",
                                        "-","-","-"]
        assert isinstance(game.board, Board)

    def test_game_class_has_player(self):
        board = Board()
        game = Game(board)
        assert isinstance(game.player_1, Player)

    def test_game_class_player_move(self):
        board = Board()
        game = Game(board)
        game.player_move(game.player_1, 0)
        assert game.board.the_board == ["X","-","-",
                                        "-","-","-",
                                        "-","-","-"]

class TestPlayer:
    def test_player_class(self):
        player_1 = Player("X")
        assert player_1.name == "X"
        assert player_1.score == 0
        player_2 = Player("O")
        assert player_2.name == "O"
        assert player_2.score == 0

