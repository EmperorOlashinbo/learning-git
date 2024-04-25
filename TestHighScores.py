import unittest
import unittest.mock
import os
from HighScores import HighScores


class TestHighScores(unittest.TestCase):
    def setUp(self):
        self.filename = "test_highscores.json"
        with open(self.filename, "w") as file:
            file.write('{"Player1": 100, "Player2": 90}')

    def tearDown(self):
        os.remove(self.filename)

    def test_load_scores_existing_file(self):
        high_scores = HighScores(self.filename)
        self.assertEqual(high_scores.load_scores(), {"Player1": 100, "Player2": 90})

    def test_load_scores_nonexistent_file(self):
        high_scores = HighScores("nonexistent_file.json")
        self.assertEqual(high_scores.load_scores(), {})

    def test_save_score_new_score(self):
        high_scores = HighScores(self.filename)
        high_scores.save_score("Player3", 95)
        self.assertEqual(
            high_scores.scores, {"Player1": 100, "Player2": 90, "Player3": 95}
        )

    def test_save_score_existing_score(self):
        high_scores = HighScores(self.filename)
        high_scores.save_score("Player1", 110)
        self.assertEqual(high_scores.scores, {"Player1": 110, "Player2": 90})


if __name__ == "__main__":
    unittest.main()
