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
                                   int(random.random() * width/blockSize) * blockSize, blockSize, width)
        self.__score = Score.Score(width - blockSize*1.2, 0, "black", "")
        self.__highScore = Score.Score(0, 0, "black", "High: ")

    def initialize(self):
        pygame.display.set_caption("Snake")
        icon = pygame.image.load("resources/logo.png")
        pygame.display.set_icon(icon)
        self.__highScore.set(self.readHighScore())
        self.__grid.add(self.__snake)
        self.__grid.add(self.__apple)
        self.__grid.add(self.__score)
        self.__grid.add(self.__highScore)

    def run(self):

        running = True
        clock = pygame.time.Clock()

        while running and self.__snake.isAlive():

            self.__wn.fill(Color.Color.green())  # green background
            self.__grid.doOneFrame()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.writeHighScore(self.__score.get())
                    running = False
                self.getKeyPress(event)
            self.updateScore()
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

    def updateScore(self):
        self.__score.set(self.__apple.getTimesEaten())
        if self.__score.get() > self.__highScore.get():
            self.__highScore.set(self.__score.get())

    def readHighScore(self):
        high = open("data/high.txt", "r")
        highScoreText = high.readline()
        print(highScoreText)
        if highScoreText != "":
            return int(highScoreText)
        else:
            return 0

    def writeHighScore(self, score):
        high = open("data/high.txt", "w")
        highScore = self.__highScore.get()
        high.write(str(highScore))
        high.close()
