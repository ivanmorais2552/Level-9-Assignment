# Ivan and Noah
import random


class card:
    faces = ["♦️", "❤️", "♠️", "♣️"]
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']


class deck:
    def __init__(self):
        faces = card.faces
        numbers = card.numbers
        deck = []
        for i in faces:
            for j in numbers:
                deck.append(f"{i} {j}")
        random.shuffle(deck)
