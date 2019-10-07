import unittest

from card import *

class TestCard(unittest.TestCase):
    def test_is_pair(self):
        card1 = Card()
        card2 = Card()
        self.assertTrue(card1.is_pair(card2))
        self.assertTrue(card2.is_pair(card1))


if __name__ == '__main__':
    unittest.main()