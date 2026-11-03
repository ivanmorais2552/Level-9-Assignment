from cards import *
from player import *

print("Welcome to War")
#make 2 decks, make 2 players, assign the decks to the players
player_won = False
while True:
    player_deck1 = Deck()
    player_deck2 = Deck()
    player1 = Player("player1", player_deck1)
    player2 = Player("player2", player_deck2)
    while player_won == False:
        player1_card = player1.play_card()
        player2_card = player2.play_card()
        print(f"Player 1 played {player1_card.face} {player1_card.number}. Player 2 played {player2_card.face} {player2_card.number}")
        player_won = evaluate_winner(player1_card, player2_card, player_deck1, player_deck2)
    next_round = input("Start another game (yes/no): ").strip().lower()
    if next_round == "no":
        break
    elif next_round == "yes":
        player_won = False
