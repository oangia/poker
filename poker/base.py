class Card:
    def __init__(self, card):
        self.rank = int(card[:-1])
        self.suit = card[-1]
        self.point = self.rank - 2 if self.rank != 1 else 12
        self.power = 2 ** self.point

    def __repr__(self):
        return f"'{self.rank}{self.suit}'"

from poker.HandDetectV2 import HandDetectV2
from poker.HandDetect import HandDetect

class Hand:
    def __init__(self, cards, detect="V2"):
        self.cards = cards
        if detect == "V2":
            handDetect = HandDetectV2()
        else:
            handDetect = HandDetect()
        self.point = handDetect.detect(self.cards)

    def compare(self, opponent):
        if self.point > opponent.point:
            return 1
        if self.point < opponent.point:
            return -1
        return 0
      
class Setting:
    def __init__(self, back, middle, front):
        self.back = back
        self.middle = middle
        self.front = front

    def compare(self, opponent, resType="detail"):
        if resType == "detail":
            return [self.back.compare(opponent.back), self.middle.compare(opponent.middle), self.front.compare(opponent.front)]
        elif resType == "sum":
            return sum([self.back.compare(opponent.back), self.middle.compare(opponent.middle), self.front.compare(opponent.front)])

    def checkValid():
        if self.back.point >= self.middle.point and self.middle.point > self.front.point:
            return True
        return False
