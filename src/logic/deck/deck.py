import sys
sys.path.append("../../")

import random

from logic.card import *

DECK_SIZE = 52

class Deck(object):
    """Represents a deck of cards

    Attributes:
        cards: list of Card objects
    """

    def __init__(self, size=52):
        self.cards = []
        for rank in Rank:
            for suit in Suit:
                card = Card(suit, rank)
                self.cards.append(card)
        num_cards_to_remove = DECK_SIZE - size
        self.cards = self.cards[:size]
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)
