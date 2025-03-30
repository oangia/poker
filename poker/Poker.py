from itertools import combinations
import random
from poker import Card, Hand, Setting

class Poker:
    CARDS = ['1s', '1c', '1d', '1h', '2s', '2c', '2d', '2h', '3s', '3c', '3d', '3h', '4s', '4c', '4d', '4h', '5s', '5c', '5d', '5h', '6s', '6c', '6d', '6h', '7s', '7c', '7d', '7h', '8s', '8c',
         '8d', '8h', '9s', '9c', '9d', '9h', '10s', '10c', '10d', '10h', '11s', '11c', '11d', '11h', '12s', '12c', '12d', '12h', '13s', '13c', '13d', '13h']
    HANDS = ['ZITCH', 'ONE PAIR', 'TWO PAIR', 'THREE KIND', 'STRAIGHT', 'FLUSH', 'FULL HOUSE', 'FOUR KIND', 'STRAIGHT FLUSH']

    def __init__(self):
        pass

    def compareTwoSettings(player1, player2):
        player1 = [Card(card) for card in player1]
        player2 = [Card(card) for card in player2]
        p1Back = Hand(player1[:5])
        p2Back = Hand(player1[:5])
        p1Middle= Hand(player1[5:10])
        p2Middle= Hand(player2[5:10])
        p1Front= Hand(player1[10:])
        p2Front= Hand(player2[10:])
        s1 = Setting(p1Back, p1Middle, p1Front)
        s2 = Setting(p2Back, p2Middle, p2Front)
        return s1.compare(s2)

    @staticmethod
    def randomCards(count = 5):
        return sorted(random.sample(Poker.CARDS, count), key=lambda x: int(x[:-1]))

    @staticmethod
    def testHand(pokerClass, handType, loop = 5):
        poker = pokerClass()
        count = 1
        for i in range(loop):
            cards = Poker.randomCards()
            point = poker.detect(cards)
            while handType != poker.getHandType(point):
                count += 1
                cards = Poker.randomCards()
                point = poker.detect(cards)
            print(poker.getHandType(point), cards, count, point)

    @staticmethod
    def testHands(pokerClass):
        for handType in Poker.HANDS:
            Poker.testHand(pokerClass, handType, 1)
