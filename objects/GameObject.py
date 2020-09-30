from abc import ABC


class GameObject(ABC):

    def __init__(self, x, y, color):
        self.__x = x
        self.__y = y
        self.__color = color

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getGridSize(self):
        return self.__gridSize

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getColor(self):
        return self.__color

    def isColliding(self, other):
        if other.getX() == self.getX() and\
                other.getY() == self.getY():
                return True
        return False

    def doOneFrame(self):
        pass

    def display(self, surface):
        pass

    def notifyCollided(self, other):
        pass
