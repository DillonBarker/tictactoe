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
        game = Game()
        assert game.board.the_board == [["-","-","-"],
                                        ["-","-","-"],
                                        ["-","-","-"]]
        assert isinstance(game.board, Board)

    def test_game_class_has_player(self):
        game = Game()
        assert isinstance(game.player_1, Player)

    def test_game_class_player_move(self):
        game = Game()
        game.player_move(0, 0)
        assert game.board.the_board == [["X","-","-"],
                                        ["-","-","-"],
                                        ["-","-","-"]]

    def test_game_class_player_cant_overwrite(self):
        game = Game()
        game.player_move(0, 0)
        assert game.board.the_board == [["X","-","-"],
                                        ["-","-","-"],
                                        ["-","-","-"]]
        game.player_move(0, 0)
        assert game.board.the_board == [["X","-","-"],
                                        ["-","-","-"],
                                        ["-","-","-"]]   

    def test_game_class_is_game_over(self):
        game = Game()
        game.board.the_board = [["X","X","X"],
                                ["X","X","X"],
                                ["X","X","X"]]
        game.player_move(0, 0)
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
        player_1 = Player("X")
        player_2 = Player("O")
        controller = TurnControl(player_1, player_2)
        assert controller.generator == [player_1, player_2]
    
    def test_turn_control_current_player(self):
        player_1 = Player("X")
        player_2 = Player("O")
        controller = TurnControl(player_1, player_2)
        controller.current_player()
        assert controller.turn == player_1
    
    def test_turn_control_switches(self):
        player_1 = Player("X")
        player_2 = Player("O")
        controller = TurnControl(player_1, player_2)
        controller.current_player()
        assert controller.turn == player_1
        controller.current_player()
        assert controller.turn == player_2

class TestWinningConditions:
    
    def test_column_winning_condition(self):
        print("Harry is a HOE")
        player_1 = Player("X")
        player_2 = Player("O")
        board = Board()
        board.the_board = [["X","-","-"],
                           ["X","-","-"],
                           ["X","-","-"]]
        wc = WinningConditions(board, player_1, player_2)
        wc.is_it_won(player_1)
        assert player_1.score == 1 and player_2.score == 0

    def test_row_winning_condition(self):
        player_1 = Player("X")
        player_2 = Player("O")
        board = Board()
        board.the_board = [["X","X","X"],
                           ["-","-","-"],
                           ["-","-","-"]]
        wc = WinningConditions(board, player_1, player_2)
        wc.is_it_won(player_1)
        assert player_1.score == 1 and player_2.score == 0
    
    def test_diagonal_winning_condition(self):
        player_1 = Player("X")
        player_2 = Player("O")
        board = Board()
        board.the_board = [["X","-","-"],
                           ["-","X","-"],
                           ["-","-","X"]]
        wc = WinningConditions(board, player_1, player_2)
        wc.is_it_won(player_1)
        assert player_1.score == 1 and player_2.score == 0

    def test_o_wins_by_diag(self):
        player_1 = Player("X")
        player_2 = Player("O")
        board = Board()
        board.the_board = [["O","-","-"],
                           ["-","O","-"],
                           ["-","-","O"]]
        wc = WinningConditions(board, player_1, player_2)
        wc.is_it_won(player_2)
        assert player_1.score == 0 and player_2.score == 1