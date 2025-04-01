from poker.base import HandType
from poker.Algo.HandDetect.TypeDetect import TypeDetect

class HandDetect:
    MAX_POWER = 4097
    MAX_ZITCH_POWER = 7937

    def __init__(self):
        pass

    def detect(self, cards):
        self.cards = cards
        self.power = sum([card.power for card in self.cards])
        self.handType = 0
        self.zitch_point = 0
        self.handType = TypeDetect.detect(self.cards)
        self.point = self.calculatePoint()
        return self.handType * 10 + self.point
        
    def calculatePoint(self):
        if self.handType in [HandType.ZITCH, HandType.FLUSH, HandType.STRAIGHT, HandType.STRAIGHT_FLUSH]:
            return self.power/self.MAX_ZITCH_POWER

        if self.handType in [HandType.THREEKIND, HandType.FULLHOUSE, HandType.FOURKIND]:
            return self.cards[2].point

        if self.handType == HandType.ONEPAIR:
            if self.cards[0].rank == self.cards[1].rank:
                self.zitch_point = (self.cards[2].power + self.cards[3].power + self.cards[4].power)/self.MAX_ZITCH_POWER
                return self.cards[0].point
            if self.cards[1].rank == self.cards[2].rank:
                self.zitch_point = (self.cards[0].power + self.cards[3].power + self.cards[4].power)/self.MAX_ZITCH_POWER
                return self.cards[2].point
            if self.cards[2].rank == self.cards[3].rank:
                self.zitch_point = (self.cards[0].power + self.cards[1].power + self.cards[4].power)/self.MAX_ZITCH_POWER
                return self.cards[3].point
            if self.cards[3].rank == self.cards[4].rank:
                self.zitch_point = (self.cards[0].power + self.cards[1].power + self.cards[2].power)/self.MAX_ZITCH_POWER
                return self.cards[4].point

        if self.handType == HandType.TWOPAIR:
            if self.cards[0].rank != self.cards[1].rank:
                self.zitch_point = self.cards[0].power/self.MAX_POWER
            elif self.cards[3].rank != self.cards[4].rank:
                self.zitch_point = self.cards[4].power/self.MAX_POWER
            else:
                self.zitch_point = self.cards[2].power/self.MAX_POWER

            return (self.cards[1].power + self.cards[3].power)/self.MAX_ZITCH_POWER
