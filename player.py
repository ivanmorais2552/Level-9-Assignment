from cards import *
import random

class Player():

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def play_card(self):
        played_card = self.deck.cards[0]
        return played_card

def evaluate_game(player1_deck, player2_deck):
    has_won = False
    if len(player1_deck.cards) == 104:
        has_won = True
        print("Player 1 won the game!")
    elif len(player2_deck.cards) == 104:
        has_won = True
        print("Player 2 won the game")
    return has_won

def war(player_deck1, player_deck2, ties):
    print("Its a tie! Begin the war!")
    print("Each player puts 3 cards facedown")
    if len(player_deck1.cards) < 4 and len(player_deck1.cards) >= 1:
        player_1_new_card = player_deck1.cards[0]
        player_deck1.cards.remove(player_deck1.cards[0])
        ties.extend(player_deck1.cards)
        player_deck1.cards.clear()
    elif len(player_deck1.cards) >= 4:
        for i in range(3):
            ties.append(player_deck1.cards[0])
            player_deck1.cards.remove(player_deck1.cards[0])
        player_1_new_card = player_deck1.cards[0]
    if len(player_deck2.cards) < 4 and len(player_deck2.cards) >= 1:
        player_2_new_card = player_deck2.cards[0]
        player_deck2.cards.remove(player_deck2.cards[0])
        ties.extend(player_deck2.cards)
        player_deck2.cards.clear()
    elif len(player_deck2.cards) >= 4:
        for i in range(3):
            ties.append(player_deck2.cards[0])
            player_deck2.cards.remove(player_deck2.cards[0])
        player_2_new_card = player_deck2.cards[0]
    if player_1_new_card.number > player_2_new_card.number:
        print(f"Player 1 played {player_1_new_card}. Player 2 played {player_2_new_card}. Player 1 won the war!")
        player_deck1.cards.extend(ties)
        player_deck1.cards.extend([player_2_new_card, player_1_new_card])
        if len(player_deck1.cards) > 0:
            player_deck1.cards.remove(player_deck1.cards[0])
        if len(player_deck2.cards) > 0:
            player_deck2.cards.remove(player_deck2.cards[0])
    elif player_1_new_card.number < player_2_new_card.number:
        print(f"Player 1 played {player_1_new_card}. Player 2 played {player_2_new_card}. Player 2 won the war!")
        player_deck2.cards.extend(ties)
        player_deck2.cards.extend([player_2_new_card, player_1_new_card])
        if len(player_deck1.cards) > 0:
            player_deck1.cards.remove(player_deck1.cards[0])
        if len(player_deck2.cards) > 0:
            player_deck2.cards.remove(player_deck2.cards[0])
    elif player_1_new_card.number == player_2_new_card.number:
        player_deck1, player_deck2, ties = war(player_deck1, player_deck2, ties)
    print(f"Player 1 has {len(player_deck1.cards)} cards. Player 2 has {len(player_deck2.cards)} cards.")
    return player_deck1, player_deck2, ties
    
    """
    backuplist1 = []
    backuplist2 = []
    for i in player_deck1.cards:
        backuplist1.append(i)
    for i in player_deck2.cards:
        backuplist2.append(i)
    fix1 = player_deck1.cards[-1]
    fix2 = player_deck2.cards[-1]
    print("Its a tie! Begin the war!")
    print("Each player puts 3 cards facedown")
    try:
        for i in range(3):
            ties.extend([player_deck1.cards[0], player_deck2.cards[0]])
            player_deck1.cards.remove(player_deck1.cards[0])
            player_deck2.cards.remove(player_deck2.cards[0])
        player_1_new_card = player_deck1.cards[0]
        player_2_new_card = player_deck2.cards[0]
    except IndexError:
        if len(backuplist1) < 4 and len(backuplist1) > 1:
            player_deck1.cards = backuplist1
            player_1_new_card = player_deck1.cards[len(player_deck1.cards)]
            player_deck1.cards.pop()
        else:
            player_1_new_card = fix1
        if len(backuplist2) < 4 and len(backuplist2) > 1:
            player_deck2.cards = backuplist2
            player_2_new_card = player_deck2.cards[len(player_deck1.cards)]
            player_deck1.cards.pop()
        ties.extend(player_deck1.cards)
        ties.extend(player_deck2.cards)
        player_deck1.cards.clear()
        player_deck2.cards.clear()
    finally:
        if player_1_new_card.number > player_2_new_card.number:
            print(f"Player 1 played {player_1_new_card}. Player 2 played {player_2_new_card}. Player 1 won the war!")
            player_deck1.cards.extend(ties)
            player_deck1.cards.extend([player_2_new_card, player_1_new_card])
            player_deck1.cards.remove(player_deck1.cards[0])
            player_deck2.cards.remove(player_deck2.cards[0])
        elif player_1_new_card.number < player_2_new_card.number:
            print(f"Player 1 played {player_1_new_card}. Player 2 played {player_2_new_card}. Player 2 won the war!")
            player_deck2.cards.extend(ties)
            player_deck2.cards.extend([player_2_new_card, player_1_new_card])
            player_deck1.cards.remove(player_deck1.cards[0])
            player_deck2.cards.remove(player_deck2.cards[0])
        else:
            war(player_deck1, player_deck2, ties)
        print(f"Player 1 has {len(player_deck1.cards)} cards. Player 2 has {len(player_deck2.cards)} cards.")
"""
        
def evaluate_winner(player1_card, player2_card, player_deck1, player_deck2):
    #If player 1 has a higher card, it adds both cards to the back of the deck, and removes them from the front
    if player1_card.number > player2_card.number:
        print("Player 1 wins!")
        player_deck1.cards.extend([player2_card, player1_card])
        player_deck1.cards.remove(player_deck1.cards[0])
        player_deck2.cards.remove(player_deck2.cards[0])
        print(f"Player 1 has {len(player_deck1.cards)} cards. Player 2 has {len(player_deck2.cards)} cards.")
        player_won = False
    #If player 2 has a higher card, it adds both cards to the back of the deck, and removes them from the front
    elif player1_card.number < player2_card.number:
        print("Player 2 wins!")
        player_deck2.cards.extend([player1_card, player2_card])
        player_deck1.cards.remove(player_deck1.cards[0])
        player_deck2.cards.remove(player_deck2.cards[0])
        print(f"Player 1 has {len(player_deck1.cards)} cards. Player 2 has {len(player_deck2.cards)} cards.")
        player_won = False
    else:
        player_won = war(player_deck1, player_deck2, [])
    return evaluate_game(player_deck1, player_deck2)