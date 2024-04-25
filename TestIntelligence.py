import unittest
from Intelligence import Intelligence


class TestIntelligence(unittest.TestCase):
    def test_should_roll_again_easy(self):
        intelligence = Intelligence("easy")
        self.assertTrue(intelligence.should_roll_again(0, 10))
        self.assertFalse(intelligence.should_roll_again(0, 20))

    def test_should_roll_again_medium(self):
        intelligence = Intelligence("medium")
        self.assertTrue(intelligence.should_roll_again(0, 15))
        self.assertTrue(intelligence.should_roll_again(80, 19))
        self.assertFalse(intelligence.should_roll_again(80, 20))

    def test_should_roll_again_hard(self):
        intelligence = Intelligence("hard")
        self.assertTrue(intelligence.should_roll_again(0, 20))
        self.assertFalse(intelligence.should_roll_again(50, 25))


if __name__ == "__main__":
    unittest.main()
