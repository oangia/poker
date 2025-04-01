class Hand:
    MAX_POWER = 4097
    MAX_ZITCH_POWER = 7809
    
    def __init__(self, cards):
        self.cards = cards
        self.point = self.detect()
        
    def compare(self, opponent):
        if self.point > opponent.point:
            return 1
        if self.point < opponent.point:
            return -1
        return 0

    def toStr(self):
        return ",".join(card.toStr() for card in self.cards)

    def detect(self):
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
    
class TypeDetect:
    @staticmethod
    def detect(self, cards):
        ranks = [card.rank for card in cards]
        count = len(set(ranks))

        if count < 5:
            if count == 4:
                return HandType.ONEPAIR

            if count == 3:
                if ranks[0] == ranks[2] or ranks[1] == ranks[3] or ranks[2] == ranks[4]:
                    return HandType.THREEKIND
                return HandType.TWOPAIR

            if count == 2:
                if ranks[1] == ranks[3]:
                    return HandType.FOURKIND
                return HandType.FULLHOUSE

        flush = int(len(set([card.suit for card in cards])) == 1)
        straight = int(ranks[4] - ranks[0] == 4 or (ranks[0] == 1 and ranks[1] == 10))
        return straight * HandType.STRAIGHT + flush * HandType.FLUSH - flush * straight
