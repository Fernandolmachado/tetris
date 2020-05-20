
import pygame


class Group(object):
    def __init__(self, posx: int, posy: int, blockSize: int):
        self.posx = posx
        self.posy = posy
        self.blockSize = blockSize
        self.size = blockSize * 3
        self.centerx = self.size - self.posx
        self.centery = self.size - self.posy
        self.blocks = list()
        self.surface = self._createSurface()
        self.color = None
        self.angle = 0

    def getSize(self) -> int:
        return self.size

    def setSize(self, size: int):
        self.size = size
        self.__redefineCenter()

    def getPosition(self) -> tuple:
        return (self.posx, self.posy)

    def setPosition(self, posx: int, posy: int):
        self.posx = posx
        self.posy = posy
        self.__redefineCenter()

    def getCenter(self) -> tuple:
        return (self.centerx, self.centery)

    def getBlocks(self) -> tuple:
        return self.blocks

    def getSurface(self) -> pygame.Surface:
        return self.surface

    def move(self, horiz: int, vert: int):
        self.posx += horiz
        self.posy += vert
        self.__redefineCenter()

    def update(self, surface: pygame.Surface):
        surface.blit(self.surface, (self.posx, self.posy))

    def _redefineCenter(self):
        self.centerx = self.size - self.posx
        self.centery = self.size - self.posy

    def _createSurface(self):
        surface = pygame.Surface((self.size, self.size)).convert_alpha()
        surface.fill((255, 255, 255, 0))
        return surface

    # Implementar na sub-classe
    def rotate(self):
        pass

    def _generateBlocks(self):
        pass

    def _redefineAngle(self):
        pass
