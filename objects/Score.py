from objects import GameObject
import pygame
from util import Color


class Score(GameObject.GameObject):

    def __init__(self, x, y, color):
        super(Score, self).__init__(x, y, color)
        self.__score = 0

    def set(self, score):
        self.__score = score

    def display(self, surface):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(str(self.__score), False, Color.Color.getColor(self.getColor()))
        surface.blit(text, (self.getX(), self.getY()))


