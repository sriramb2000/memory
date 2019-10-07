import sys
sys.path.append("../..")
from math import ceil

from logic.deck import *
from logic.card import Background
from colorama import Back

CARD_WIDTH = 8

def join_lines(strings):
    """
    Stack strings horizontally.
    This doesn't keep lines aligned unless the preceding lines have the same length.
    :param strings: Strings to stack
    :return: String consisting of the horizontally stacked input
    """
    liness = [string.splitlines() for string in strings]
    return '\n'.join(''.join(lines) for lines in zip(*liness))

def ascii_version_of_card(*cards):
    """
    Instead of a boring text version of the card we render an ASCII image of the card.
    :param cards: One or more card objects
    :return: A string, the nice ascii version of cards
    """

    return join_lines(map(lambda c: c.__str__(), cards))

class Display(object):
    """Represents a display of cards

    Attributes:
        cols: Number of cols
        deck: List of Objects which are being displayed
    """
    def __init__(self, cols, deck):
        self.cols = cols
        self.rows = ceil(len(deck)/cols)
        self.deck = deck
        self.grid = [[]] * self.rows
        self.status = ""
        self.refresh()

    def refresh(self):
        for i in range(self.rows):
            self.grid[i] = self.deck[i*self.cols:min((i+1)*self.cols, len(self.deck))]
    
    def display(self):
        rowNum = 0
        for row in self.grid:
            print(ascii_version_of_card(*row))
            #print index nums
            print(self.index_str(row, rowNum))
            rowNum += 1
        print(self.status)
    
    def index_str(self, row, rownum):
        res = []
        for i in range(len(row)):
            if row[i].selected:
                index = ":{}:".format((rownum*self.cols)+i+1)
            elif row[i].matched:
                index = "|{}|".format((rownum*self.cols)+i+1)
            else:
                index = "[{}]".format((rownum*self.cols)+i+1)
            res.append(index.center(CARD_WIDTH))
        return ''.join(res)
        
# deck = Deck(19)
# card = deck.cards[3]
# card.color = Back.RED
# card.matched = True
# card.selected = False
# deck.cards[4].selected = False
# d = Display(10, deck.cards)

# #print(d.index_str(d.grid[0], 0))
# d.display()