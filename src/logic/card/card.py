from enum import Enum
from colorama import init, Fore, Back, Style
from termcolor import colored

#use Colorama to make Termcolor work on Windows too
init(autoreset=True)

class Suit(Enum):
    CLUBS = 0
    DIAMONDS = 1
    HEART = 2
    SPADES = 3

class Rank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

CARD = """\
┌──────┐
│{}    │
│  {}  │
│    {}│
└──────┘
""".format('{rank: <2}', '{suit: <2}', '{rank: >2}')

HIDDEN_CARD = """\
┌──────┐
│░░░░░░│
│░░░░░░│
│░░░░░░│
└──────┘
"""

# we will use this to prints the appropriate icons for each card
name_to_symbol = {
    Suit.SPADES:   '♠',
    Suit.DIAMONDS: '♦',
    Suit.HEART:   '♥',
    Suit.CLUBS:    '♣',
}

rank_to_str = {
    Rank.ACE: 'A',
    Rank.TWO: '2',
    Rank.THREE: '3',
    Rank.FOUR:'4',
    Rank.FIVE: '5',
    Rank.SIX: '6',
    Rank.SEVEN: '7',
    Rank.EIGHT: '8',
    Rank.NINE: '9',
    Rank.TEN: '10',
    Rank.JACK: 'J',
    Rank.QUEEN: 'Q',
    Rank.KING: 'K',
}

def prepend_color(fg, bg, card_str):
    res = []
    for line in card_str.splitlines():
        line = fg + bg + line + Back.RESET
        res.append(line)
    return '\n'.join(res)

class Background(Enum):
    RED = 'on_red'
    BLUE = 'on_blue'
    MAGENTA = 'on_magenta'
    BLACK = 'reset'

class Card(object):
    """Represents a standard playing card
    
    Attributes:
        suit: integer 0-3
        rank: integer 1-13
    """

    def __init__(self, suit=Suit.CLUBS, rank=Rank.TWO):
        self.suit = suit
        self.rank = rank
        self.matched = False
        self.selected = False
        self.color = None
    
    def __str__(self):
        if self.matched:
            return prepend_color(Fore.WHITE, self.color, CARD.format(rank=rank_to_str[self.rank], suit=name_to_symbol[self.suit]))
        elif self.selected:
            #return actual card
            return prepend_color(Fore.GREEN, Back.RESET, CARD.format(rank=rank_to_str[self.rank], suit=name_to_symbol[self.suit]))
            #return colored(CARD.format(rank=rank_to_str[self.rank], suit=name_to_symbol[self.suit]), 'green')
        else:
            #return face down
           return prepend_color(Fore.WHITE, Back.RESET, HIDDEN_CARD)
    
    def is_pair(self, card):
        try:
            return self.rank == card.rank
        except Exception as e:
            print(card, 'is not of type Card')
            return False
