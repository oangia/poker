class Card:
    def __init__(self, card):
        self.rank = int(card[:-1])
        self.suit = card[-1]
        self.point = self.rank - 2 if self.rank != 1 else 12
        self.power = 2 ** self.point

    def toStr(self):
        return f"{self.rank}{self.suit}"
    def __repr__(self):
        return f"{self.rank}{self.suit}"

class HandType:
    ZITCH = 0
    ONEPAIR = 1
    TWOPAIR = 2
    THREEKIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULLHOUSE = 6
    FOURKIND = 7
    STRAIGHT_FLUSH = 8
    
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

    def __repr__(self):
        return ",".join([self.back.toStr(), self.middle.toStr(), self.back.toStr()])

class Player:
    def __init__(self, cards):
        self.cards = [Card(card) for card in cards]
        self.algo = BruteForce(self.cards)

    def getStrongestSetting(self):
        self.settings = self.algo.getAllSettings()
        return self.settings[0]

    def getBestFitSetting(self, opponent):
        opponentBestSetting = opponent.getStrongestSetting()
        self.settings = self.algo.getAllSettings()
        for setting in self.settings:
            if setting.compare(opponentBestSetting) == 1:
                return setting

from itertools import combinations
from poker.HandDetect import HandDetect
class BruteForce:
    def __init__(self, cards):
        self.cards = cards

    def getAllSettings(self):
        self.generateAllHands()
        self.generateAllSettings()
        newSettings = [self.settings[0]]
        settingsLen = len(self.settings)
        for i in range(settingsLen - 1):
            if -1 in newSettings[-1].compare(self.settings[i + 1]):
                newSettings.append(self.settings[i+1])
        return newSettings
         
    def generateAllHands(self):
        handDetect = HandDetect()
        hands = [Hand(cards, handDetect=handDetect) for cards in list(combinations(self.cards, 5))]
        self.hands = sorted(hands, key=lambda hand: (hand.point), reverse=True)

    def generateAllSettings(self):
        print(self.hands[0].cards, self.hands[0].point)
        self.settings = []
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
                self.settings.append(Setting(back, middle, middle))
    
   
