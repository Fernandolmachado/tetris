
import pygame


class Group(object):
    def __init__(self):
        self.size = int
        self.posx = int
        self.posy = int
        self.centerx = self.size - self.posx
        self.centery = self.size - self.posy
        self.gap = int
        self.blocks = list()
        self.surface = None
        self.color = pygame.Color(0, 0, 0, 0)

    def getSize(self) -> int:
        return self.size

    def setSize(self, size: int):
        self.size = size
        self.__redefineCenter()

    def getPosition(self) -> list:
        return (self.posx, self.posy)

    def setPosition(self, posx: int, posy: int):
        self.posx = posx
        self.posy = posy
        self.__redefineCenter()

    def getCenter(self) -> list:
        return (self.centerx, self.centery)

    def getGap(self) -> int:
        return self.gap

    def getBlocks(self) -> list:
        return self.blocks

    def getSurface(self) -> pygame.Surface():
        return self.surface

    def move(self, horiz: int, vert: int):
        self.posx += horiz
        self.posy += vert
        self.__redefineCenter()

    def rotate(self):
        pygame.transform.rotate(self.surface, -90)

    def update(self):
        self.surface.fill(self.color)

    def __redefineCenter(self):
        self.centerx = self.size - self.posx
        self.centery = self.size - self.posy
