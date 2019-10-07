import unittest

from display import *

class TestDisplay(unittest.TestCase):
    def test_rows(self):
        d = Display(5, [0]*7)
        self.assertEqual(d.rows, 2)
        #self.assertTrue(True)
    
    def test_refresh(self):
        d = Display(5, [0]*7)
        self.assertEqual(d.grid[0], [0]*5)
        self.assertEqual(d.grid[1], [0]*2)


if __name__ == '__main__':
    unittest.main()