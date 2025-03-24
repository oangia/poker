import random

class Card:
    def __init__(self, card):
        self.rank = int(card[:-1])
        self.suit = card[-1]
        self.point = self.rank - 2 if self.rank != 1 else 12
        self.power = 2 ** self.point

    def __repr__(self):
        return f"'{self.rank}{self.suit}'"

class Hand:
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

    def __init__(self, cards):
        self.cards = cards
        self.processData()
        self.handType = self.detectHand()
        self.point = self.calculatePoint()

    def processData(self):
        self.handType = 0
        self.zitch_point = 0

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

    def getHandType(self):
        types = ["ZITCH", "ONEPAIR", "TWOPAIR", "THREEKIND", "STRAIGHT", "FLUSH", "FULLHOUSE", "FOURKIND", "STRAIGHT_FLUSH"]
        return types[self.handType]

    def __repr__(self):
        #print({"Hand": ",".join([f"{card.rank}{card.suit}" for card in self.cards]), "type": self.getHandType(), "point": self.point, "zitch point": self.zitch_point})
        return ",".join([f"{card.rank}{card.suit}" for card in self.cards])

class Deck:
    def __init__(self):
        suits = ['s', 'c', 'd', 'h']
        ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.cards = [f"{rank}{suit}") for rank in ranks for suit in suits]

    def dealRemain(self, players):
        cards = []
        for card in self.cards:
            if card in players:
                continue
            cards.append(card)
        return cards

    def getCards(self, cards):
        return [Card(card) for card in cards.split(",")]

    def get_random_cards(self, count = 13):
        return sorted(random.sample(self.cards, count),
                      key=lambda card: card.rank)

    def get_hand(self, type, loop = 1):
        for i in range(loop):
            count = 0
            while True:
                count += 1
                cards = self.get_random_cards(5)
                hand = Hand(cards)
                if hand.getHandType() == type:
                    print(",".join([f"{card.rank}{card.suit}" for card in cards]), {"type": hand.getHandType(), "point": hand.point, "zitch point": hand.zitch_point}, count)
                    break

    def testHands(self):
        self.get_hand("ZITCH")
        self.get_hand("ONEPAIR")
        self.get_hand("TWOPAIR")
        self.get_hand("THREEKIND")
        self.get_hand('STRAIGHT')
        self.get_hand('FLUSH')
        self.get_hand("FULLHOUSE")
        self.get_hand("FOURKIND")
        self.get_hand("STRAIGHT_FLUSH")

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        """Draws a card from the deck. Returns None if the deck is empty."""
        return self.cards.pop() if self.cards else None

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck({self.cards})"

class Poker:
    def __init__(self):
        self.deck = Deck()

    def helper(self):
        print("Generate cards: poker.generateFullHand()")
        print("Generate hand of five: poker.generateHand(5)")
        print("Generate hand of three: poker.generateHand(3)")

    def encirclement(self, cards):
        players = cards.split("|")
        player1 = Player(players[0])
        player2 = Player(players[1])
        player3 = Player(players[2])
        opponentCards = self.deck.dealRemain(players[0].split(",") + players[1].split(",") + players[2].split(","))
        opponent = Player(opponentCards)
        opponent.getStrongestSetting()
        p1Setting = player1.getBestFitSetting(opponent)
        p2Setting = player2.getBestFitSetting(opponent)
        p3Setting = player3.getBestFitSetting(opponent)
        return p1Setting + "|" + p2Setting + "|" + p3Setting
    
    def single(self, cards):
        player1 = Player(cards)
        return player1.getStrongestSetting()

    def generateFullHand(self):
        return self.deck.get_random_cards(13)

    def generateHand(self, cards = 5):
        return self.deck.get_random_cards(cards)
