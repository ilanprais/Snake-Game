from objects import GameObject
import pygame
from util import Color


class Block(GameObject.GameObject):

    def __init__(self, x, y, color, size):
        super(Block, self).__init__(x, y, color)
        self.__size = size

    def display(self, surface):
        pygame.draw.rect(surface, Color.Color.getColor(self.getColor()), (self.getX(), self.getY(), self.__size, self.__size))

    def getSize(self):
        return self.__size

    def notifyCollided(self, other):
        pass



