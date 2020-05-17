
class Color:
    def __init__(self, red: int, green: int, blue: int, alpha: int):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def getColor(self):
        return (self.red, self.green, self.blue, self.alpha)
