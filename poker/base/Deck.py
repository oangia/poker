from poker.base.Card import Card
from itertools import combinations
import random

class Deck:
    CARDS = ['1s', '1c', '1d', '1h', '2s', '2c', '2d', '2h', '3s', '3c', '3d', '3h', '4s', '4c', '4d', '4h', '5s', '5c', '5d', '5h', '6s', '6c', '6d', '6h', '7s', '7c', '7d', '7h', '8s', '8c',
         '8d', '8h', '9s', '9c', '9d', '9h', '10s', '10c', '10d', '10h', '11s', '11c', '11d', '11h', '12s', '12c', '12d', '12h', '13s', '13c', '13d', '13h']
    
    def __init__(self):
        self.cards = [Card(card) for card in self.CARDS]

    def dealRemain(self, players):
        cards = []
        for card in self.cards:
            if card in players:
                continue
            cards.append(card)
        return cards

    def getAllPosibleHands(self):
        return list(combinations(self.cards, 5))
        
    def getCards(self, cards):
        return [Card(card) for card in cards.split(",")]

    def get_random_cards(self, count = 13):
        return sorted(random.sample(self.cards, count),
                      key=lambda card: card.rank)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        """Draws a card from the deck. Returns None if the deck is empty."""
        return self.cards.pop() if self.cards else None

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck({self.cards})"
