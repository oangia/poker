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
