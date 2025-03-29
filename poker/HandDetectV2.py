import numpy as np

class HandDetectV2:
    def __init__(self):
        pass

    def detect(self, cards):
        self.cards = cards
        if len(np.unique(self.cards[:, 0])) < len(self.cards):
            return self.pair()
        return self.zitch()

    def zitch(self):
        power = np.sum(self.cards[:, 3])
        flush = int(np.all(self.cards[:, 1] == self.cards[0, 1]))
        straight = int(power in [31, 62, 124, 248, 496, 992, 1984, 3968, 4111, 7936])
        return float(flush * 50 + straight * 40 + power / 793.7 - straight * flush * 10)

    def pair(self):
        handTypes = {(1, 1): 7,(2, 0): 6,(1, 2): 3,(2, 1): 2,(1, 3): 1}
        unique, counts = np.unique(self.cards[:, 3], return_counts=True)
        duplicates = unique[counts > 1]
        uniques = unique[counts == 1]
        position = handTypes[(duplicates.size, uniques.size)] * 10
        if [duplicates.size, uniques.size] in [[1, 1], [2, 0], [1, 2]]:
              return float(position + self.cards[2][2]/ 1.3)
        return float(position + np.sum(duplicates)/(614.5 + 1) + np.sum(uniques)/71681)
