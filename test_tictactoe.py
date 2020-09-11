import pytest
from tictactoe import *

class TestBoard:
    def test_board_class(self):
        board = Board()
        assert board.the_board == [["-","-","-"],
                                   ["-","-","-"],
                                   ["-","-","-"]]
        assert board.the_board != [["dog","-","-"],
                                    ["-","-","-"],
                                    ["-","-","-"]]

class TestGame:
    def test_game_class(self):
        board = Board()
        player_1 = Player("X")
        player_2 = Player("O")
        game = Game(board, player_1, player_2)
        assert game.board.the_board == [["-","-","-"],
                                        ["-","-","-"],
                                        ["-","-","-"]]
        assert isinstance(game.board, Board)

    def test_game_class_has_player(self):
        player_1 = Player("X")
        player_2 = Player("O")
        board = Board()
        game = Game(board, player_1, player_2)
        assert isinstance(game.player_1, Player)

    def test_game_class_player_move(self):
        player_1 = Player("X")
        player_2 = Player("O")
        board = Board()
        game = Game(board, player_1, player_2)
        game.player_move(player_1, 0, 0)
        assert game.board.the_board == [["X","-","-"],
                                        ["-","-","-"],
                                        ["-","-","-"]]

    def test_game_class_player_cant_overwrite(self):
        player_1 = Player("X")
        player_2 = Player("O")
        board = Board()
        game = Game(board, player_1, player_2)
        game.player_move(player_1, 0, 0)
        assert game.board.the_board == [["X","-","-"],
                                        ["-","-","-"],
                                        ["-","-","-"]]
        game.player_move(player_2, 0, 0)
        assert game.board.the_board == [["X","-","-"],
                                        ["-","-","-"],
                                        ["-","-","-"]]   

    def test_game_class_is_game_over(self):
        player_1 = Player("X")
        player_2 = Player("O")
        board = Board()
        game = Game(board, player_1, player_2)
        game.board.the_board = [["X","X","X"],
                                ["X","X","X"],
                                ["X","X","X"]]
        game.player_move(player_1, 0, 0)
        assert game.game_over == True

class TestPlayer:
    def test_player_class(self):
        player_1 = Player("X")
        assert player_1.name == "X"
        assert player_1.score == 0
        player_2 = Player("O")
        assert player_2.name == "O"
        assert player_2.score == 0

class TestTurnControl:
    def test_turn_control_class(self):
        controller = TurnControl()
        assert controller.generator == [1,2]
    
    def test_turn_control_current_player(self):
        controller = TurnControl()
        controller.current_player()
        assert controller.turn == 1
    
    def test_turn_control_switches(self):
        controller = TurnControl()
        controller.current_player()
        assert controller.turn == 1
        controller.current_player()
        assert controller.turn == 2

class TestWinningConditions:
    
    def test_column_winning_condition(self):
        player_1 = Player("X")
        player_2 = Player("O")
        board = Board()
        game = Game(board, player_1, player_2)
        wc = WinningConditions(game)
        game.player_move(player_1, 0, 0)
        game.player_move(player_1, 1, 0)
        game.player_move(player_1, 2, 0)
        assert wc.win == 0
        wc.col_win(player_1)
        assert wc.win == "X"

    def test_row_winning_condition(self):
        player_1 = Player("X")
        player_2 = Player("O")
        board = Board()
        game = Game(board, player_1, player_2)
        wc = WinningConditions(game)
        game.player_move(player_1, 0, 0)
        game.player_move(player_1, 0, 1)
        game.player_move(player_1, 0, 2)
        assert wc.win == 0
        wc.row_win(player_1)
        assert wc.win == "X"
    
    def test_diagonal_winning_condition(self):
        player_1 = Player("X")
        player_2 = Player("O")
        board = Board()
        game = Game(board, player_1, player_2)
        wc = WinningConditions(game)
        game.player_move(player_1, 0, 0)
        game.player_move(player_1, 1, 1)
        game.player_move(player_1, 2, 2)
        assert wc.win == 0
        wc.diag_win(player_1)
        assert wc.win == "X"

    def test_o_wins_by_diag(self):
        player_1 = Player("X")
        player_2 = Player("O")
        board = Board()
        game = Game(board, player_1, player_2)
        wc = WinningConditions(game)
        game.player_move(player_2, 0, 0)
        game.player_move(player_2, 1, 1)
        game.player_move(player_2, 2, 2)
        assert wc.win == 0
        wc.diag_win(player_2)
        assert wc.win == "O"