import unittest
from Histogram import Histogram


class TestHistogram(unittest.TestCase):
    def setUp(self):
        self.histogram = Histogram()

    def test_add_and_display(self):
        self.histogram.add(3)
        self.histogram.add(3)
        self.histogram.add(2)
        self.assertEqual(self.histogram.data, {3: 2, 2: 1})


if __name__ == "__main__":
    unittest.main()
