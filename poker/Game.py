from poker.Deck import Deck
from poker.base import Player

class Game:
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
