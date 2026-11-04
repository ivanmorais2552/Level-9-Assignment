from cards import *
import random


class Player():  # creates a player class

    def __init__(self, name, deck):
        self.name = name  # player has a name
        self.deck = deck  # player has a deck object

    def play_card(self):
        """Returns the top card in the deck"""
        played_card = self.deck.cards[0]
        return played_card


def evaluate_game(player1_deck, player2_deck):
    """Evaluates if either player has enough cards to win the game"""
    has_won = False
    if len(player1_deck.cards) == 104 or len(player2_deck.cards) == 0:
        has_won = True
        print("Player 1 won the game!")
    elif len(player2_deck.cards) == 104 or len(player1_deck.cards) == 0:
        has_won = True
        print("Player 2 won the game")
    return has_won


def war(player_deck1, player_deck2, ties):
    """Starts a war. Each player puts down 3 cards and then the last card decides the war"""
    player_won = False
    print("Its a tie! Begin the war!")
    print("Each player puts 3 cards facedown")
    # first check player 1 to see if they have enough cards
    if len(player_deck1.cards) < 4 and len(player_deck1.cards) >= 2:
        player_1_new_card = player_deck1.cards[0]
        player_deck1.cards.remove(player_deck1.cards[0])
        ties.extend(player_deck1.cards)
        player_deck1.cards.clear()
    elif len(player_deck1.cards) >= 4:
        for i in range(3):
            ties.append(player_deck1.cards[0])
            player_deck1.cards.remove(player_deck1.cards[0])
        player_1_new_card = player_deck1.cards[0]
    # This is so if there's not enough cards it won't break the game
    elif len(player_deck1.cards) <= 1:
        return player_deck1, player_deck2, ties, True
    # next check player 2 to see if they have enough cards
    if len(player_deck2.cards) < 4 and len(player_deck2.cards) >= 2:
        player_2_new_card = player_deck2.cards[0]
        player_deck2.cards.remove(player_deck2.cards[0])
        ties.extend(player_deck2.cards)
        player_deck2.cards.clear()
    elif len(player_deck2.cards) >= 4:
        for i in range(3):
            ties.append(player_deck2.cards[0])
            player_deck2.cards.remove(player_deck2.cards[0])
        player_2_new_card = player_deck2.cards[0]
    # This is so if there's not enough cards it won't break the game
    elif len(player_deck2.cards) <= 1:
        return player_deck1, player_deck2, ties, True
    # This is the main comparison block. Cards will have been added to ties already
    if player_1_new_card.number > player_2_new_card.number:  # compares the cards player1 to player2
        print(
            f"Player 1 played {player_1_new_card}. Player 2 played {player_2_new_card}. Player 1 won the war!")
        player_deck1.cards.extend(ties)
        player_deck1.cards.extend([player_2_new_card, player_1_new_card])
        if len(player_deck1.cards) > 0:
            player_deck1.cards.remove(player_deck1.cards[0])
        else:
            return player_deck1, player_deck2, ties, True
        if len(player_deck2.cards) > 0:
            player_deck2.cards.remove(player_deck2.cards[0])
        else:
            return player_deck1, player_deck2, ties, True
        player_won = True
    elif player_1_new_card.number < player_2_new_card.number:
        print(
            f"Player 1 played {player_1_new_card}. Player 2 played {player_2_new_card}. Player 2 won the war!")
        player_deck2.cards.extend(ties)
        player_deck2.cards.extend([player_2_new_card, player_1_new_card])
        if len(player_deck1.cards) > 0:
            player_deck1.cards.remove(player_deck1.cards[0])
        if len(player_deck2.cards) > 0:
            player_deck2.cards.remove(player_deck2.cards[0])
        player_won = True
    # starts a new war if the last card is the same
    elif player_1_new_card.number == player_2_new_card.number:
        player_deck1, player_deck2, ties, player_won = war(
            player_deck1, player_deck2, ties)
    print(
        f"Player 1 has {len(player_deck1.cards)} cards. Player 2 has {len(player_deck2.cards)} cards.")
    return player_deck1, player_deck2, ties, player_won


def evaluate_winner(player1_card, player2_card, player_deck1, player_deck2):
    """Main game method. Does all the playing. Returns whether or not the game is over."""
    # If player 1 has a higher card, it adds both cards to the back of the deck, and removes them from the front
    if player1_card.number > player2_card.number:
        print("Player 1 wins!")
        player_deck1.cards.extend([player2_card, player1_card])
        player_deck1.cards.remove(player_deck1.cards[0])
        player_deck2.cards.remove(player_deck2.cards[0])
        print(
            f"Player 1 has {len(player_deck1.cards)} cards. Player 2 has {len(player_deck2.cards)} cards.")
        player_won = False
    # If player 2 has a higher card, it adds both cards to the back of the deck, and removes them from the front
    elif player1_card.number < player2_card.number:
        print("Player 2 wins!")
        player_deck2.cards.extend([player1_card, player2_card])
        player_deck1.cards.remove(player_deck1.cards[0])
        player_deck2.cards.remove(player_deck2.cards[0])
        print(
            f"Player 1 has {len(player_deck1.cards)} cards. Player 2 has {len(player_deck2.cards)} cards.")
        player_won = False
    else:
        player_deck1, player_deck2, ties, player_won = war(
            player_deck1, player_deck2, [])
    return evaluate_game(player_deck1, player_deck2)
