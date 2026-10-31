from cards import *
from player import *

print("Welcome to War")
#make 2 decks, make 2 players, assign the decks to the players
player_deck1 = Deck()
player_deck2 = Deck()
player1 = Player("player1", player_deck1)
player2 = Player("player2", player_deck2)



tie = True
player_won = False
ties = []
while player_won == False:
    player1_card = player1.play_card()
    player2_card = player2.play_card()

    print(f"Player 1 played {player1_card.face} {player1_card.number}. Player 2 played {player2_card.face} {player2_card.number}")

    result = evaluate_winner(player1_card, player2_card, player_deck1, player_deck2, ties)


  
#they play cards, if one is higher, that player gets both the cards
while True:
    evaluate_winner()
#continue playing until one player has all the cards
