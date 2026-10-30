import cards as c


# Player Class
class Player:
    def __init__(self, name):
        self.name = name
        self.deck = c.Deck()

    def play_card(self):
        self.top_card = self.deck.cards[0]
        return self.top_card

    def lose_round(self):
        lost_card = self.deck.cards.pop(0)
        return lost_card

    def win_round(self, won_card):
        self.deck.cards.pop(0)
        self.deck.cards.append(self.top_card)
        self.deck.cards.append(won_card)
        self.deck.cards.extend(ties)

    def tie_round(self, ties, player_1_card, player_2_card):
        ties.extend([player_1_card, player_2_card])


# Main Game
print("Welcome to War")
player1 = Player("John")
player2 = Player("Jake")
ties = []

while len(player1.deck.cards) > 0 and len(player2.deck.cards) > 0:
    print(f"\n{player1.name} has {len(player1.deck.cards)} cards. ---------- {player2.name} has {len(player2.deck.cards)} cards.\n")
    player1.play_card()
    player2.play_card()
    print(
        f"{player1.name} played {player1.top_card}. {player2.name} played {player2.top_card}")
    if player1.top_card.number == player2.top_card.number:
        print("It's a tie!")
        player1.tie_round(ties, player1.lose_round(), player2.lose_round())
    elif player1.top_card.number > player2.top_card.number:
        print(f"{player1.name} wins this round!")
        player1.win_round(player2.lose_round())
        ties.clear()
    else:
        print(f"{player2.name} wins this round!")
        player2.win_round(player1.lose_round())
        ties.clear()

else:
    if len(player2.deck.cards) == 0:
        print(f"\n{player1.name} Wins!")
    else:
        print(f"\n{player2.name} Wins!")
