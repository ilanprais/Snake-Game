
class Color:

    @staticmethod
    def white():
        return 255, 255, 255

    @staticmethod
    def red():
        return 255, 0, 0

    @staticmethod
    def green():
        return 0, 255, 0

    @staticmethod
    def black():
        return 0, 0, 0

    @staticmethod
    def getColor(color):
        if color == "white":
            return Color.white()
        if color == "red":
            return Color.red()
        if color == "green":
            return Color.green()
        if color == "black":
            return Color.black()

        return Color.white()



