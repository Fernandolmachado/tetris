
import random

from classes.Color import Color


class Brick:
    colors = (
        Color(255, 255, 0),
        Color(255, 0, 0),
        Color(255, 0, 255),
        Color(0, 255, 0),
        Color(255, 203, 219),
        Color(255, 165, 0),
        Color(255, 255, 255)
    )

    positions = (
        (   # stick
            ((0, 1), (0, -1), (0, -2)),
            ((1, 0), (-1, 0), (-2, 0)),
            ((0, 1), (0, -1), (0, -2)),
            ((1, 0), (-1, 0), (-2, 0))
        ),
        (   # square
            ((1, 0), (0, -1), (1, -1)),
            ((1, 0), (0, -1), (1, -1)),
            ((1, 0), (0, -1), (1, -1)),
            ((1, 0), (0, -1), (1, -1))
        ),
        (   # pyramide  PAREI AQUI
            ((1, 0), (0, -1), (1, -1)),
            ((1, 0), (0, -1), (1, -1)),
            ((1, 0), (0, -1), (1, -1)),
            ((1, 0), (0, -1), (1, -1))
        ),
        (
            ((1, 0), (0, -1), (1, -1)),
            ((1, 0), (0, -1), (1, -1)),
            ((1, 0), (0, -1), (1, -1)),
            ((1, 0), (0, -1), (1, -1))
        ),
        (
            ((1, 0), (0, -1), (1, -1)),
            ((1, 0), (0, -1), (1, -1)),
            ((1, 0), (0, -1), (1, -1)),
            ((1, 0), (0, -1), (1, -1))
        ),
        (
            ((1, 0), (0, -1), (1, -1)),
            ((1, 0), (0, -1), (1, -1)),
            ((1, 0), (0, -1), (1, -1)),
            ((1, 0), (0, -1), (1, -1))
        ),
        (
            ((1, 0), (0, -1), (1, -1)),
            ((1, 0), (0, -1), (1, -1)),
            ((1, 0), (0, -1), (1, -1)),
            ((1, 0), (0, -1), (1, -1))
        )
    )

    def __ini__(self):
        self.generate()

    def generate(self):
        self.id = random.randint(0, 6)
        self.position = random.randint(0, 3)
        self.color = Brick.colors[self.id]
        self.center = list(4, -2)

    def turn(self):
        self.position = (self.position + 1) % 4

    def getBlocks(self):
        return Brick.positions[self.id][self.position]

    def getColor(self):
        return self.color

    def fall(self):
        self.center[1] += 1

    def toLeft(self):
        if not self.onWallLeft():
            self.center[0] -= 1

    def toRight(self):
        if not self.onWallRight():
            self.center[0] += 1
