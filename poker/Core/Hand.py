class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.handType = HandType.detect(self.cards)
        self.point = self.handType * 10 + HandDetect.detect(self.handType, self.cards)
        
    def compare(self, opponent):
        if self.point > opponent.point:
            return 1
        if self.point < opponent.point:
            return -1
        return 0

    def toStr(self):
        return ",".join(card.toStr() for card in self.cards)
        
class HandDetect:
    @staticmethod
    def detect(handType, cards):
        if handType in [HandType.ZITCH, HandType.FLUSH, HandType.STRAIGHT, HandType.STRAIGHT_FLUSH]:
            return sum([card.power for card in cards]) * 10 / 7937

        if handType in [HandType.THREEKIND, HandType.FULLHOUSE, HandType.FOURKIND]:
            return cards[2].point / 1.3

        if handType == HandType.ONEPAIR:
            if cards[0].rank == cards[1].rank:
                zitch_point = cards[2].power + cards[3].power + cards[4].power
                return cards[0].point / 1.3 + zitch_point / 7169
            if cards[1].rank == cards[2].rank:
                zitch_point = cards[0].power + cards[3].power + cards[4].power
                return cards[2].point / 1.3 + zitch_point / 7169
            if cards[2].rank == cards[3].rank:
                zitch_point = cards[0].power + cards[1].power + cards[4].power
                return cards[3].point / 1.3 + zitch_point / 7169
            if cards[3].rank == cards[4].rank:
                zitch_point = cards[0].power + cards[1].power + cards[2].power
                return cards[4].point / 1.3 + zitch_point / 7169

        if handType == HandType.TWOPAIR:
            if cards[0].rank != cards[1].rank:
                zitch_point = cards[0].power
            elif cards[3].rank != cards[4].rank:
                zitch_point = cards[4].power
            else:
                zitch_point = cards[2].power

            return (cards[1].power + cards[3].power) * 9 / 6145 + zitch_point / 4097
        
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

    @staticmethod
    def detect(cards):
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
