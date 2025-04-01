from poker.base import Card, Hand, Setting, Player, Deck
import time
class Poker:
    timeStart = 0
    def __init__(self):
        pass

    @staticmethod
    def time():
        Poker.timeStart = time.time()
        
    @staticmethod
    def track(msg=""):
        if msg=="":
            print(time.time()-Poker.timeStart)
        else:
            print(msg + ": " + str(time.time()-Poker.timeStart))
            
    @staticmethod
    def testFunc(func, loop = 10):
        results = []
        for i in range(loop):
            start = time.time()
            func()
            results.append(time.time()-start)
        print(results, sum(results)/len(results))
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

poker = Poker
