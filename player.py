from cards import *
import random 

class Player():

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def play_card(self):
        play_card = self.deck.deck[0]
        return play_card


def evaluate_winner(player1_card, player2_card, player_deck1, player_deck2):
    if player1_card > player2_card:
        print("Player 1 wins!")
        player_deck1.deck.append(player2_card)
        player_deck2.deck.remove(player_deck2.deck[0])
        print(f"Player 1 has {len(player_deck1.deck)} cards. Player 2 has {len(player_deck2.deck)} cards.")
        tie = False
    elif player1_card < player2_card:
        print("Player 2 wins!")
        player_deck2.deck.append(player1_card)
        player_deck1.deck.remove(player_deck1.deck[0])
        print(f"Player 1 has {len(player_deck1.deck)} cards. Player 2 has {len(player_deck2.deck)} cards.")
        tie = False
    else:
        tie = True
    
    return tie
