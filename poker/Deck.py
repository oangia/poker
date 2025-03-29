class Deck:
    def __init__(self):
        suits = ['s', 'c', 'd', 'h']
        ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.cards = [f"{rank}{suit}" for rank in ranks for suit in suits]

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
