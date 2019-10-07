import sys
sys.path.append("../..")
from colorama import Back

from logic.deck import *
from logic.display import *

COLORS = [Back.RED, Back.BLUE, Back.MAGENTA, Back.CYAN]

class Game():
    def __init__(self, num_players, deck_size, player_names=[]):
        self.num_players = num_players
        self.deck_size = deck_size
        self.deck = Deck(deck_size)
        self.display = Display(deck_size//3, self.deck.cards)
        #self.deck = self.display.deck
        self.player_scores = {}
        self.player_names = player_names
        self.player_colors = {}
        self.invalid_cards = set()
        self.selected_card = None
        c_i = 0
        for p in range(num_players):
            self.player_colors[p] = COLORS[c_i]
            c_i += 1
            self.player_scores[p] = 0

    def take_turn(self, player_num=0, index=-1):
        in_turn = not (self.selected_card is None)

        if in_turn:
            self.deck.cards[index].selected = True
            self.display_game()
            #wait for user to see
            input("Hit Enter once you've taken a look at the cards:")
        
        #If move is a match, return 1, if first select, return 0, if no match, return -1
        if in_turn and self.deck.cards[self.selected_card].is_pair(self.deck.cards[index]):
            #Match found
            self.deck.cards[self.selected_card].color = self.player_colors[player_num]
            self.deck.cards[index].color = self.player_colors[player_num]
            self.deck.cards[self.selected_card].matched = True
            self.deck.cards[index].matched = True
            self.player_scores[player_num] += 1
            #Reset for next turn
            self.invalid_cards.add(index)
            self.selected_card = None
            return 1
        elif in_turn and not self.deck.cards[self.selected_card].is_pair(self.deck.cards[index]):
            #No Match
            self.deck.cards[self.selected_card].selected = False
            self.deck.cards[index].selected = False
            #Reset for next turn
            self.invalid_cards.remove(self.selected_card)
            self.selected_card = None
            return -1
        else:
            #First pick
            self.selected_card = index
            self.invalid_cards.add(index)
            self.deck.cards[self.selected_card].selected = True
            return 0
    
    def is_valid_move(self, index):
        return not (index in self.invalid_cards)
    
    def is_over(self):
        print(len(self.invalid_cards))
        return len(self.invalid_cards) == self.deck_size

    def display_game(self):
        self.display.status = self.player_score_str()
        self.display.refresh()
        self.display.display()
    
    def player_score_str(self):
        string = ""
        for p in self.player_scores:
            string += "{} Score: {}\n".format(self.player_names[p], self.player_scores[p])
        return string
    
    def get_winner(self):
        max_score = -1
        winners = []
        for p in self.player_scores:
            if self.player_scores[p] > max_score:
                max_score = self.player_scores[p]
                winners = [self.player_names[p]]
            elif self.player_scores[p] == max_score:
                winners.append(self.player_names[p])
        return ", ".join(winners)
        


