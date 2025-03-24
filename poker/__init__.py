class Card:
    def __init__(self, card):
        self.rank = int(card[:-1])
        self.suit = card[-1]
        self.point = self.rank - 2 if self.rank != 1 else 12
        self.power = 2 ** self.point

    def __repr__(self):
        return f"'{self.rank}{self.suit}'"
