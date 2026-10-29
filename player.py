from cards import *
import random 
class Player():

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def play_card(self):
        play_card = self.deck.deck[0]
        return play_card
        