import unittest
from unittest.mock import patch
from dice_game1 import Dice, Player, DiceHand, Histogram, Intelligence, HighScores, Game


class TestDice(unittest.TestCase):
    def test_roll(self):
        dice = Dice()
        roll = dice.roll()
        self.assertIn(roll, range(1, 7))


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Test")

    def test_update_score(self):
        self.player.update_score(5)
        self.assertEqual(self.player.score, 5)

    def test_reset_score(self):
        self.player.score = 10
        self.player.reset_score()
        self.assertEqual(self.player.score, 0)


class TestDiceHand(unittest.TestCase):
    def setUp(self):
        self.dice_hand = DiceHand()

    def test_add_and_total_roll(self):
        self.dice_hand.add_roll(4)
        self.dice_hand.add_roll(3)
        self.assertEqual(self.dice_hand.total(), 7)

    def test_reset(self):
        self.dice_hand.add_roll(5)
        self.dice_hand.reset()
        self.assertEqual(self.dice_hand.total(), 0)


class TestHistogram(unittest.TestCase):
    def setUp(self):
        self.histogram = Histogram()

    def test_add_and_display(self):
        self.histogram.add(3)
        self.histogram.add(3)
        self.histogram.add(2)
        self.assertEqual(self.histogram.data, {3: 2, 2: 1})


class TestIntelligence(unittest.TestCase):
    def test_should_roll_again(self):
        intelligence = Intelligence("easy")
        self.assertTrue(intelligence.should_roll_again(0, 10))


class TestHighScores(unittest.TestCase):
    @patch("os.path.exists")
    @patch("builtins.open")
    @patch("json.load")
    @patch("json.dump")
    def test_save_and_load_scores(self, mock_dump, mock_load, mock_open, mock_exists):
        mock_exists.return_value = True
        mock_load.return_value = {"Test": 100}

        high_scores = HighScores("test_scores.json")
        high_scores.save_score("Test", 150)

        mock_dump.assert_called()
        self.assertEqual(high_scores.scores["Test"], 150)


class TestGame(unittest.TestCase):
    @patch(
        "builtins.input", side_effect=["4", "Player1", "Player2", "Player3", "Player4"]
    )
    def test_setup_multiple_players(self, mocked_input):
        game = Game()
        self.assertEqual(len(game.players), 4)

    @patch("builtins.input", side_effect=["1", " ", "y", "easy"])
    @patch("dice_game1.Intelligence")
    def test_setup_single_player_with_ai(self, mock_intelligence, mocked_input):
        game = Game()
        self.assertEqual(len(game.players), 2)
        self.assertEqual(game.players[0].name, " ")
        self.assertEqual(game.players[1].name, "Computer")
        mock_intelligence.assert_called_with(level="easy")


if __name__ == "__main__":
    unittest.main()
