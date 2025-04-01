from poker.base import Card, Hand, Setting, Player
from poker.helper import Deck, Poker
import time
def testFunc(func, loop = 10):
    results = []
    for i in range(loop):
        start = time.time()
        func()
        results.append(time.time()-start)
    print(results, sum(results)/len(results))
