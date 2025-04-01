from poker.base import HandType

class HandDetect:
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
        straight = int(ranks[4] - ranks[1] == 4 or (ranks[0] == 1 and ranks[2] == 10))
        return straight * HandType.STRAIGHT + flush * HandType.FLUSH - flush * straight
