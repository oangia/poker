from itertools import combinations
from poker.Core.Card import Card
from poker.Core.Hand import Hand
from poker.Core.Setting import Setting

class Player:
    def __init__(self, cards):
        self.cards = [Card(card) for card in cards]
        self.algo = BruteForce(self.cards)
        self.settings = self.algo.getAllSettings()
        
    def getStrongestSetting(self): 
        return self.settings[0]

    def getWeakestSetting(self): 
        return self.settings[-1]

    def getBestFitSetting(self, opponent):
        opponentBestSetting = opponent.getStrongestSetting()
        for setting in self.settings:
            if setting.compare(opponentBestSetting) == 1:
                return setting

class BruteForce:
    def __init__(self, cards):
        self.cards = cards
        self.generateAllHands()
        self.generateAllSettings()
        
    def getAllSettings(self):
        newSettings = [self.settings[0]]
        settingsLen = len(self.settings)
        for i in range(settingsLen - 1):
            if -1 in newSettings[-1].compare(self.settings[i + 1]):
                newSettings.append(self.settings[i+1])
        return newSettings
         
    def generateAllHands(self):
        hands = [Hand(cards) for cards in list(combinations(self.cards, 5))]
        self.hands = sorted(hands, key=lambda hand: (hand.point), reverse=True)

    def generateAllSettings(self):
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
