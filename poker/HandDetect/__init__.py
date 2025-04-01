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

class HandDetect:
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

        suits = [card.suit for card in cards]
        flush = int(len(set(suits)) == 1)
        straight = int(sum([card.power for card in self.cards]) in [4111, 31, 62, 124, 248, 496, 992, 1984, 3968, 7936])

        return straight * HandType.STRAIGHT + flush * HandType.FLUSH - flush * straight
        if straight and flush:
            return HandType.STRAIGHT_FLUSH

        if straight:
            return HandType.STRAIGHT

        if flush:
            return HandType.FLUSH

        return HandType.ZITCH
