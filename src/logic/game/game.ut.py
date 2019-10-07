import unittest

from game import *

class TestGame(unittest.TestCase):
    def test_get_winner(self):
        g = Game(2,10,['p1','p2'])
        g.player_scores = { 0: 3, 1: 2 }
        self.assertEqual(g.get_winner(), 'p1')
        g.player_scores = { 0: 3, 1: 3 }
        self.assertEqual(g.get_winner(), 'p1, p2')
    
    def test_is_valid_move(self):
        g = Game(2, 10, ['p1', 'p2'])
        g.invalid_cards.add(1)
        self.assertTrue(g.is_valid_move(2))
        self.assertFalse(g.is_valid_move(1))
    
    def test_is_over(self):
        g = Game(2, 10, ['p1', 'p2'])
        g.invalid_cards = set([1,2,3,4,5,6,7,8,9,10])
        self.assertTrue(g.is_over())


if __name__ == '__main__':
    unittest.main()