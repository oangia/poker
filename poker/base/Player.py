from poker.base.Card import Card
from poker.base.BruteForce import BruteForce

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
