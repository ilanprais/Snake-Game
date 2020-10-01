from objects import GameObject
import pygame
from util import Color


class Score(GameObject.GameObject):

    def __init__(self, x, y, color, text):
        super(Score, self).__init__(x, y, color)
        self.__score = 0
        self.__text = text

    def set(self, score):
        self.__score = score

    def get(self):
        return self.__score

    def display(self, surface):
        font = pygame.font.SysFont('Comic Sans MS', 23)
        score = font.render(self.__text + str(self.__score), False, Color.Color.getColor(self.getColor()))
        surface.blit(score, (self.getX(), self.getY()))


