class Card:
    def __init__(self, card):
        self.rank = int(card[:-1])
        self.suit = card[-1]
        self.point = self.rank - 2 if self.rank != 1 else 12
        self.power = 2 ** self.point

    def __repr__(self):
        return f"'{self.rank}{self.suit}'"

class Hand:
    def __init__(self, cards, handDetect=handDetect):
        self.cards = cards
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

    def compare(self, opponent):
        return [self.back.compare(opponent.back), 
                self.middle.compare(opponent.middle), 
                self.front.compare(opponent.front)]

    def checkValid():
        if self.back.point >= self.middle.point and self.middle.point > self.front.point:
            return True
        return False

from itertools import combinations
from poker.HandDetect import HandDetect

class Player:
    def __init__(self, cards):
        self.cards = [Card(card) for card in cards]

    def getStrongestSetting(self, algo="brute"):
        settings = self.brute()
        return settings[0]

    def getBestFitSetting(self, opponent):
        opponentBestSetting = opponent.getStrongestSetting()
        settings = self.brute()
        for setting in settings:
            if setting.compare(opponentBestSetting) == 1:
                return setting

    def generateAllHands(self):
        handDetect = HandDetect()
        hands = [Hand(cards, handDetect=handDetect) for cards in list(combinations(self.cards, 5))]
        self.hands = sorted(hands, key=lambda hand: (hand.point), reverse=True)

    def brute(self):
        self.generateAllHand()
        settings = []
        handsLen = len(self.hands)
        for i in range(handsLen):
            if self.hands[i].point < 10:
                break
            back = self.hands[i]
            for j in range(i+1, handsLen):
                middle = self.hands[j]
                dup = False
                for card in middle.cards:
                    if card in back.cards:
                        dup = True
                        break
                if dup:
                    continue
                front = [None] * 3
                j = 0
                for card in self.cards:
                    if card not in back.cards and card not in middle.cards:
                        front[j] = card
                        j += 1
                settings.append(Setting(back, middle, middle))
        return settings
