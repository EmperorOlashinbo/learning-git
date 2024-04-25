import unittest
from Player import Player


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


if __name__ == "__main__":
    unittest.main()
