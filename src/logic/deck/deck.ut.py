import unittest

from deck import *

class TestDeck(unittest.TestCase):
    def test_deck_size(self):
        d = Deck(10)
        d2 = Deck()
        self.assertEqual(len(d.cards), 10)
        self.assertEqual(len(d2.cards), DECK_SIZE)


if __name__ == '__main__':
    unittest.main()



