from poker.base.Card import Card
from poker.Algo.BruteForce import BruteForce

class Player:
    def __init__(self, cards):
        self.cards = [Card(card) for card in cards]
        
    def getStrongestSetting(self): 
        self.settings = BruteForce(self.cards).getAllSettings()
        return self.settings[0]

    def getWeakestSetting(self): 
        self.settings = BruteForce(self.cards).getAllSettings()
        return self.settings[-1]

    def getBestFitSetting(self, opponent):
        opponentBestSetting = opponent.getStrongestSetting()
        self.settings = BruteForce(self.cards).getAllSettings()
        for setting in self.settings:
            if setting.compare(opponentBestSetting) == 1:
                return setting
