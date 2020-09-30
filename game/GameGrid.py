class GameGrid:

    def __init__(self, rows):
        self.__rows = rows
        self.__objects = []

    def doOneFrame(self):
        self.detectCollision()

        for obj in self.__objects:
            obj.doOneFrame()

    def add(self, obj):
        self.__objects.append(obj)

    def display(self, surface):
        for obj in self.__objects:
            obj.display(surface)

    def detectCollision(self):
        for obj1 in self.__objects:
            for obj2 in self.__objects:
                if obj1 != obj2 and obj1.isColliding(obj2):
                        obj1.notifyCollided(obj2)
