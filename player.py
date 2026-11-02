from cards import *
import random

class Player():

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def play_card(self):
        played_card = self.deck.cards[0]
        return played_card

#evaluates the winner of each card played

def evaluate_winner(player1_card, player2_card, player_deck1, player_deck2, ties):
    tie = False
    
    #If player 1 has a higher card, it adds both cards to the back of the deck, and removes them from the front
    if player1_card.number > player2_card.number:
        print("Player 1 wins!")
        player_deck1.cards.extend([player2_card, player1_card])
        player_deck1.cards.remove(player_deck1.cards[0])
        player_deck2.cards.remove(player_deck2.cards[0])
        if len(ties) > 0:
            player_deck1.cards.extend(ties)
        print(f"Player 1 has {len(player_deck1.cards)} cards. Player 2 has {len(player_deck2.cards)} cards.")
        ties.clear()
    #If player 2 has a higher card, it adds both cards to the back of the deck, and removes them from the front
    elif player1_card.number < player2_card.number:
        print("Player 2 wins!")
        player_deck2.cards.extend([player1_card, player2_card])
        player_deck1.cards.remove(player_deck1.cards[0])
        player_deck2.cards.remove(player_deck2.cards[0])
        if len(ties) > 0:
            player_deck2.cards.extend(ties)
        print(f"Player 1 has {len(player_deck1.cards)} cards. Player 2 has {len(player_deck2.cards)} cards.")
        ties.clear()
    #If it is a tie, it adds both the cards to a waiting list, and removes both cards from the front of the deck
    else:
        print("Its a tie! Begin the war!")
        ties.extend([player_deck1.cards[0], player_deck2.cards[0]])
        player_deck1.cards.remove(player_deck1.cards[0])
        player_deck2.cards.remove(player_deck2.cards[0])
        tie = True
    
    return tie
