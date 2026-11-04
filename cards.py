# Ivan and Noah
import random


class Card:
    faces = ["♦️", "❤️", "♠️", "♣️"]
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    card_names = {
        11: 'Jack',
        12: 'Queen',
        13: 'King',
        14: 'Ace'
    }

    def __init__(self, face, number):
        self.face = face
        self.number = number

    def __repr__(self):
        display_name = self.card_names.get(self.number, self.number)
        return f"{display_name} of {self.face}"


class Deck:
    def __init__(self):
        faces = Card.faces
        numbers = Card.numbers
        self.cards = []
        for i in faces:
            for j in numbers:
                self.cards.append(Card(i, j))
        random.shuffle(self.cards)
