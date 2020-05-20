
import pygame


class Block(object):
    def __init__(self, posx: int, posy: int, size: int, color, deadZone=0):
        self.width = size
        self.height = size
        self.posx = posx
        self.posy = posy
        self.color = color
        self.dz = deadZone

    def getWidth(self) -> int:
        return self.width

    def setWidth(self, width: int):
        self.width = width

    def getHeight(self) -> int:
        return self.height

    def setHeight(self, height: int):
        self.height = height

    def getPosition(self) -> tuple:
        return (self.posx, self.posy)

    def setPosition(self, posx: int, posy: int):
        self.posx = posx
        self.posy = posy

    def getColor(self) -> pygame.Color:
        return self.color

    def setColor(self, color: pygame.Color):
        self.color = color

    def getReact(self) -> tuple:
        return (self.posx, self.posy, self.width, self.height)

    def move(self, hor: int, vert: int):
        self.posx += hor
        self.posy += vert

    def draw(self, surface):
        pygame.draw.rect(
            surface,
            self.color,
            (
                self.posx + self.dz // 2,
                self.posy + self.dz // 2,
                self.width - self.dz,
                self.height - self.dz
            )
        )
