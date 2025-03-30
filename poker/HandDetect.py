class HandDetect:
    ZITCH = 0
    ONEPAIR = 1
    TWOPAIR = 2
    THREEKIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULLHOUSE = 6
    FOURKIND = 7
    STRAIGHT_FLUSH = 8
    MAX_POWER = 4097
    MAX_ZITCH_POWER = 7937

    def __init__(self):
        pass

    def detect(self, cards):
        self.cards = cards
        self.handType = 0
        self.zitch_point = 0
        self.handType = self.detectHand()
        self.point = self.calculatePoint()
        return self.handType * 10 + self.point

    def detectHand(self):
        ranks = [card.rank for card in self.cards]
        count = len(set(ranks))

        if count < 5:
            if count == 4:
                return self.ONEPAIR

            if count == 3:
                if ranks[0] == ranks[2] or ranks[1] == ranks[3] or ranks[2] == ranks[4]:
                    return self.THREEKIND
                return self.TWOPAIR

            if count == 2:
                if ranks[1] == ranks[3]:
                    return self.FOURKIND
                return self.FULLHOUSE

        suits = [card.suit for card in self.cards]
        self.power = sum([card.power for card in self.cards])
        self.flush = len(set(suits)) == 1
        self.straight = self.power in [4111, 31, 62, 124, 248, 496, 992, 1984, 3968, 7936]
        self.straightFlush = False

        if self.straight and self.flush:
            return self.STRAIGHT_FLUSH

        if self.straight:
            return self.STRAIGHT

        if self.flush:
            return self.FLUSH

        return self.ZITCH

    def calculatePoint(self):
        if self.handType in [self.ZITCH, self.FLUSH, self.STRAIGHT, self.STRAIGHT_FLUSH]:
            return self.power/self.MAX_ZITCH_POWER

        if self.handType in [self.THREEKIND, self.FULLHOUSE, self.FOURKIND]:
            return self.cards[2].point

        if self.handType == self.ONEPAIR:
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

        if self.handType == self.TWOPAIR:
            if self.cards[0].rank != self.cards[1].rank:
                self.zitch_point = self.cards[0].power/self.MAX_POWER
            elif self.cards[3].rank != self.cards[4].rank:
                self.zitch_point = self.cards[4].power/self.MAX_POWER
            else:
                self.zitch_point = self.cards[2].power/self.MAX_POWER

            return (self.cards[1].power + self.cards[3].power)/self.MAX_ZITCH_POWER
