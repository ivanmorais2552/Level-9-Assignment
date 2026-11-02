from cards import *
import random

class Player():

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def play_card(self):
        played_card = self.deck.cards[0]
        return played_card

def war(player1_card, player2_card, player_deck1, player_deck2):
    ties = []
    print("Its a tie! Begin the war!")
    print("Each player puts 3 cards facedown")
    try:
        for i in range(3):
            ties.extend([player_deck1.cards[0], player_deck2.cards[0]])
            player_deck1.cards.remove(player_deck1.cards[0])
            player_deck2.cards.remove(player_deck2.cards[0])
        player_1_new_card = player_deck1.cards[0]
        player_2_new_card = player_deck2.cards[0]
    except:
        if len(player_deck1.cards) < 4:
            pass
        elif len(player_deck2.cards) < 4:
            pass
        if player_1_new_card.number > player_2_new_card.number:
            print("Player 1 won the war")
            player_deck1.cards.extend(ties)
            player_deck1.cards.extend([player2_card, player1_card])
        elif player_1_new_card.number < player_2_new_card.number:
            print("Player 2 won the war")
            player_deck1.cards.extend(ties)
            player_deck1.cards.extend([player2_card, player1_card])
        else:
            war(player1_card, player2_card, player_deck1, player_deck2)
        
def evaluate_winner(player1_card, player2_card, player_deck1, player_deck2):
    #If player 1 has a higher card, it adds both cards to the back of the deck, and removes them from the front
    if player1_card.number > player2_card.number:
        print("Player 1 wins!")
        player_deck1.cards.extend([player2_card, player1_card])
        player_deck1.cards.remove(player_deck1.cards[0])
        player_deck2.cards.remove(player_deck2.cards[0])
        print(f"Player 1 has {len(player_deck1.cards)} cards. Player 2 has {len(player_deck2.cards)} cards.")
    #If player 2 has a higher card, it adds both cards to the back of the deck, and removes them from the front
    elif player1_card.number < player2_card.number:
        print("Player 2 wins!")
        player_deck2.cards.extend([player1_card, player2_card])
        player_deck1.cards.remove(player_deck1.cards[0])
        player_deck2.cards.remove(player_deck2.cards[0])
        print(f"Player 1 has {len(player_deck1.cards)} cards. Player 2 has {len(player_deck2.cards)} cards.")
    else:
        war(player1_card, player2_card, player_deck1, player_deck2)

def evaluate_game(player1, player2):
    has_won = False
    if len(player1.deck.cards) == 104:
        has_won = True
        print("Player 1 won the game!")
    elif len(player2.deck.cards) == 104:
        has_won = True
        print("Player 2 won the game")
    return has_won