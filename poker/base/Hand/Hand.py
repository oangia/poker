from poker.base.Hand.HandDetect import HandDetect

class Hand:
    def __init__(self, cards):
        self.cards = cards
        handDetect = HandDetect()
        self.point = HandDetect.detect(self.cards)
        
    def compare(self, opponent):
        if self.point > opponent.point:
            return 1
        if self.point < opponent.point:
            return -1
        return 0

    def toStr(self):
        return ",".join(card.toStr() for card in self.cards)
