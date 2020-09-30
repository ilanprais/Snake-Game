from objects import Block
import random


class Apple(Block.Block):

    def __init__(self, x, y, size, gridSize):
        super(Apple, self).__init__(x, y, "red", size)
        self.__gridSize = gridSize
        self.__timesEaten = 0

    def doOneFrame(self):
        pass

    def notifyCollided(self, other):
        self.setX(int(random.random()*self.__gridSize/self.getSize())*self.getSize())
        self.setY(int(random.random()*self.__gridSize/self.getSize())*self.getSize())
        self.__timesEaten = self.__timesEaten + 1

    def getTimesEaten(self):
        return self.__timesEaten



