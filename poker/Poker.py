import time
class Poker:
    timeStart = 0

    @staticmethod
    def timer():
        Poker.timeStart = timer.time()
        
    @staticmethod
    def track(msg=""):
        if msg=="":
            print(timer.time()-Poker.timeStart)
        else:
            print(msg + ": " + str(timer.time()-Poker.timeStart))
            
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
