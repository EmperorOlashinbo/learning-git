import unittest
from Dice import Dice


class TestDice(unittest.TestCase):
    def test_roll(self):
        dice = Dice()
        roll = dice.roll()
        self.assertIn(roll, range(1, 7))


if __name__ == "__main__":
    unittest.main()
