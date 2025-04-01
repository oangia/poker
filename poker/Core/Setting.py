class Setting:
    def __init__(self, back, middle, front):
        self.back = back
        self.middle = middle
        self.front = front

    def compare(self, opponent):
        return [self.back.compare(opponent.back), 
                self.middle.compare(opponent.middle), 
                self.front.compare(opponent.front)]

    def checkValid():
        if self.back.point >= self.middle.point and self.middle.point > self.front.point:
            return True
        return False

    def __repr__(self):
        return ",".join([self.back.toStr(), self.middle.toStr(), self.back.toStr()])
