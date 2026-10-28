# Ivan and Noah
import random


class card:
    face = ["♦️", "❤️", "♠️", "♣️"]
    number = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    cardFace = random.choice(face)
    cardNumber = random.choice(number)

    def __init__(self, name):
        self.name = name
        print(self.cardFace)
        print(self.cardNumber)


class deck:
    def __init__(self):
        pass


card("card1")
