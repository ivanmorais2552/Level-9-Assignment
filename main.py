from cards import *
from player import *

print("Welcome to War")
player_won = False
# Loop to continue the game play
while True:
    # make 2 decks, make 2 players, assign the decks to the players
    player_deck1 = Deck()
    player_deck2 = Deck()
    player1 = Player("player1", player_deck1)
    player2 = Player("player2", player_deck2)
    # Main game loop
    while player_won == False:
        # gets a card for each player
        player1_card = player1.play_card()
        player2_card = player2.play_card()
        print(
            f"Player 1 played {player1_card} . Player 2 played {player2_card} .")
        player_won = evaluate_winner(
            player1_card, player2_card, player_deck1, player_deck2)
        input("Press Enter for the next card")
    # if the user would like they can play another round
    next_round = input("Start another game (yes/no): ").strip().lower()
    if next_round == "no":
        break
    elif next_round == "yes":
        player_won = False
