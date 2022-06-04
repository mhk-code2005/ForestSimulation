#DOES NOT NEED MODIFICATION
class coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getManhattanDistance(self, coord2):
        return abs(coord2.getX() - self.x) + abs(coord2.getY() - self.y)
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    def equals(self,coord2):
        x2 = coord2.getX()
        y2 = coord2.getY()
        if self.x == x2 and self.y == y2:
            return True
        return False
