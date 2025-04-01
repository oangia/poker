from itertools import combinations
from poker.base.Card import Card
from poker.base.Hand import Hand
from poker.base.Setting import Setting

class Player:
    def __init__(self, cards):
        self.cards = cards

    def applyAlgo(self, algo):
        self.settings = algo(self.cards).getAllSettings()
        
    def getStrongestSetting(self): 
        return self.settings[0]

    def getWeakestSetting(self): 
        return self.settings[-1]

    def getBestFitSetting(self, opponent):
        opponentBestSetting = opponent.getStrongestSetting()
        for setting in self.settings:
            if setting.compare(opponentBestSetting) == 1:
                return setting
