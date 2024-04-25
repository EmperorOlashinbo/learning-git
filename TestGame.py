import unittest
from unittest.mock import MagicMock, patch
import builtins
from Game1 import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.mock_input = MagicMock()
        builtins.input = self.mock_input

    def test_setup_two_players(self):
        self.mock_input.side_effect = ["2", "Player1", "Player2", "n"]

        game = Game()
        self.assertEqual(len(game.players), 2)

    def test_setup_single_player_without_ai(self):
        self.mock_input.side_effect = ["1", " ", "n"]

        game = Game()
        self.assertEqual(len(game.players), 1)
        self.assertNotIn("Computer", [player.name for player in game.players])

    @patch("builtins.print")
    def test_player_turns(self, mock_print):
        game = Game()
        for _ in range(10):
            current_player = game.players[game.current_player_index]
            initial_score = current_player.score
            game.play_turn(current_player)
            if initial_score + current_player.score >= 100:
                self.assertTrue(game.current_player_index == True)
            else:
                self.assertTrue(game.current_player_index == False)

    @patch("builtins.input")
    @patch("builtins.print")
    def test_play_game_termination(self, mock_print, mock_input):
        mock_input.side_effect = ["2", "Player1", "Player2", "n"]

        game = Game()

        game.players[0].score = 95
        game.players[1].score = 90

        with patch.object(Game, "play_turn", autospec=True) as mock_play_turn:

            def side_effect_play_turn(self, player):
                player.score += 5

            mock_play_turn.side_effect = side_effect_play_turn

            game.play_game()

        self.assertTrue(any(player.score >= 100 for player in game.players))

        winning_player = next(player for player in game.players if player.score >= 100)
        mock_print.assert_any_call(
            f"\n{winning_player.name} wins with a score of {winning_player.score}!"
        )

        mock_print.assert_any_call("\nHigh Scores:")
        mock_print.assert_any_call("\nDice Roll Histogram:")


if __name__ == "__main__":
    unittest.main()
