from poker.Card import Card
from poker.Hand import Hand
from poker.Setting import Setting
from itertools import combinations

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

    def brute(self):
        hands = [Hand(cards, detect="V1") for cards in list(combinations(self.cards, 5))]
        self.hands = sorted(hands, key=lambda hand: (hand.point), reverse=True)
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
