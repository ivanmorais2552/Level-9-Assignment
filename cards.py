# Ivan and Noah
import random


class Card:
    faces = ["♦️", "❤️", "♠️", "♣️"]
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    def __init__(self, face, number):
        self.face = face
        self.number = number


class Deck:
    def __init__(self):
        faces = Card.faces
        numbers = Card.numbers
        self.deck = []
        for i in faces:
            for j in numbers:
                self.deck.append(Card(i, j))
        random.shuffle(self.deck)
        for card in self.deck:
            print(card.face, card.number)


Deck()
