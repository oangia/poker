from poker.base.Hand.HandType import HandType
from poker.base.Hand.TypeDetect import TypeDetect

class Hand:
    def __init__(self, cards, handDetect):
        self.cards = cards
        self.point = handDetect.detect(self.cards)
        
    def compare(self, opponent):
        if self.point > opponent.point:
            return 1
        if self.point < opponent.point:
            return -1
        return 0

    def toStr(self):
        return ",".join(card.toStr() for card in self.cards)
