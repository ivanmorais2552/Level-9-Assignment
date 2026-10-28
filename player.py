from cards import *
import random 
class player():

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def play_card(self, deck):
        pass

    def shuffle_cards(self, deck):
        random.shuffle(deck)