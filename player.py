from cards import *
import random

class Player():

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def play_card(self):
        played_card = self.deck.deck[0]
        return played_card



def evaluate_winner(player1_card, player2_card, player_deck1, player_deck2, ties):
    tie = False
    if player1_card.number > player2_card.number:
        print("Player 1 wins!")
        player_deck1.deck.extend([player2_card, player1_card])
        player_deck1.deck.remove(player_deck1.deck[0])
        player_deck2.deck.remove(player_deck2.deck[0])
        if len(ties) > 0:
            player_deck1.deck.extend(ties)
        print(f"Player 1 has {len(player_deck1.deck)} cards. Player 2 has {len(player_deck2.deck)} cards.")
        ties.clear()
    elif player1_card.number < player2_card.number:
        print("Player 2 wins!")
        player_deck2.deck.extend([player1_card, player2_card])
        player_deck1.deck.remove(player_deck1.deck[0])
        player_deck2.deck.remove(player_deck2.deck[0])
        if len(ties) > 0:
            player_deck2.deck.extend(ties)
        print(f"Player 1 has {len(player_deck1.deck)} cards. Player 2 has {len(player_deck2.deck)} cards.")
        ties.clear()
    else:
        print("Its a tie! Begin the war!")
        ties.extend([player_deck1.deck[0], player_deck2.deck[0]])
        player_deck1.deck.remove(player_deck1.deck[0])
        player_deck2.deck.remove(player_deck2.deck[0])
        tie = True
    
    return tie
