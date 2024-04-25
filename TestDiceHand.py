import unittest
from DiceHand import DiceHand


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


if __name__ == "__main__":
    unittest.main()
