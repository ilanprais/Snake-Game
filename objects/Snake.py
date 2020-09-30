from objects import Block, GameObject


class Snake(GameObject.GameObject):

    def __init__(self, blocks, gridSize):
        super(Snake, self).__init__(blocks[0].getX(), blocks[0].getY(), blocks[0].getColor())
        self.__blocks = blocks
        self.__direction = "Right"
        self.__gridSize = gridSize


    def doOneFrame(self):
        self.__blocks.pop(len(self.__blocks) - 1)
        if self.__direction == "Up":
            block = Block.Block(self.__blocks[0].getX(), self.__blocks[0].getY() - self.__blocks[0].getSize()
                                , self.__blocks[0].getColor(), self.__blocks[0].getSize())
        elif self.__direction == "Down":
            block = Block.Block(self.__blocks[0].getX(), self.__blocks[0].getY() + self.__blocks[0].getSize()
                                , self.__blocks[0].getColor(), self.__blocks[0].getSize())
        elif self.__direction == "Right":
            block = Block.Block(self.__blocks[0].getX() + self.__blocks[0].getSize(), self.__blocks[0].getY()
                                , self.__blocks[0].getColor(), self.__blocks[0].getSize())
        elif self.__direction == "Left":
            block = Block.Block(self.__blocks[0].getX() - self.__blocks[0].getSize(), self.__blocks[0].getY()
                                , self.__blocks[0].getColor(), self.__blocks[0].getSize())

        if block.getX() < 0 or block.getX() > self.__gridSize:
            block.setX(self.__gridSize - block.getX())
            block.setY(block.getY())

        if block.getY() < 0 or block.getY() > self.__gridSize:
            block.setY(self.__gridSize - block.getY())
            block.setX(block.getX())

        self.__blocks.insert(0, block)

    def notifyCollided(self, other):
        if self.__direction == "Down":
            block = Block.Block(self.__blocks[len(self.__blocks) - 1].getX(), self.__blocks[len(self.__blocks) - 1].getY() - self.__blocks[len(self.__blocks) - 1].getSize()
                                , self.__blocks[len(self.__blocks) - 1].getColor(), self.__blocks[len(self.__blocks) - 1].getSize())
        elif self.__direction == "Up":
            block = Block.Block(self.__blocks[len(self.__blocks) - 1].getX(), self.__blocks[len(self.__blocks) - 1].getY() + self.__blocks[len(self.__blocks) - 1].getSize()
                                , self.__blocks[len(self.__blocks) - 1].getColor(), self.__blocks[len(self.__blocks) - 1].getSize())
        elif self.__direction == "Left":
            block = Block.Block(self.__blocks[len(self.__blocks) - 1].getX() + self.__blocks[len(self.__blocks) - 1].getSize(), self.__blocks[len(self.__blocks) - 1].getY()
                                , self.__blocks[len(self.__blocks) - 1].getColor(), self.__blocks[0].getSize())
        elif self.__direction == "Right":
            block = Block.Block(self.__blocks[len(self.__blocks) - 1].getX() - self.__blocks[len(self.__blocks) - 1].getSize(), self.__blocks[len(self.__blocks) - 1].getY()
                                , self.__blocks[len(self.__blocks) - 1].getColor(), self.__blocks[0].getSize())

        self.__blocks.insert(len(self.__blocks), block)

    def isAlive(self):
        head = self.__blocks[0]
        for block in self.__blocks:
            if block != head and head.isColliding(block):
                return False
        return True

    def display(self, surface):
        for block in self.__blocks:
            block.display(surface)

    def remove(self):
        for block in self.__blocks:
            block.remove()

    def addBlock(self, block):
        self.__blocks.insert(len(self.__blocks) - 1, block)

    def getX(self):
        return self.__blocks[0].getX()

    def getY(self):
        return self.__blocks[0].getY()

    def turnRight(self):
        self.__direction = "Right"

    def turnLeft(self):
        self.__direction = "Left"

    def turnUp(self):
        self.__direction = "Up"

    def turnDown(self):
        self.__direction = "Down"


