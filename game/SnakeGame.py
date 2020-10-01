from game import GameGrid, Game
import pygame
import random
from util import Color
from objects import Score, Snake, Block, Apple


class SnakeGame(Game.Game):

    def __init__(self, rows):
        pygame.init()
        pygame.font.init()
        height = 500
        width = 500
        self._rows = rows
        self.__grid = GameGrid.GameGrid(rows)
        self.__wn = pygame.display.set_mode((height, width))

        blockSize = height/rows
        block1 = Block.Block(rows / 2 * blockSize, rows / 2 * blockSize, "white", blockSize)
        block2 = Block.Block(rows / 2 * blockSize + blockSize, rows / 2 * blockSize, "white", blockSize)
        snakeBlocks = [block1, block2]
        self.__snake = Snake.Snake(snakeBlocks, width)
        self.__apple = Apple.Apple(int(random.random() * width / blockSize) * blockSize,
                                   int(random.random()*width/blockSize) * blockSize, blockSize, width)
        self.__score = Score.Score(width - blockSize*1.5, 0, "black")

    def initialize(self):
        pygame.display.set_caption("Snake")
        icon = pygame.image.load("resources/logo.png")
        pygame.display.set_icon(icon)
        self.__grid.add(self.__snake)
        self.__grid.add(self.__apple)
        self.__grid.add(self.__score)

    def run(self):

        running = True
        clock = pygame.time.Clock()

        while running and self.__snake.isAlive():

            self.__wn.fill(Color.Color.green())  # green background
            self.__grid.doOneFrame()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.getKeyPress(event)

            self.__score.set(self.__apple.getTimesEaten())
            self.__grid.display(self.__wn)
            pygame.display.update()
            pygame.time.wait(300)
            clock.tick(10)

    def getKeyPress(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.__snake.turnLeft()
            elif event.key == pygame.K_RIGHT:
                self.__snake.turnRight()
            elif event.key == pygame.K_DOWN:
                self.__snake.turnDown()
            elif event.key == pygame.K_UP:
                self.__snake.turnUp()
