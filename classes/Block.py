
import pygame


class Block(object):
    def __init__(self, posx: int, posy: int, width: int, height: int, color: pygame.Color.Color()):
        self.width = width
        self.height = height
        self.posx = posx
        self.posy = posy
        self.color = color

    def getWidth(self) -> int:
        return self.width

    def setWidth(self, width: int):
        self.width = width

    def getHeight(self) -> int:
        return self.height

    def setHeight(self, height: int):
        self.height = height

    def getPosition(self) -> list:
        return (self.posx, self.posy)

    def setPosition(self, posx: int, posy: int):
        self.posx = posx
        self.posy = posy

    def getColor(self) -> pygame.Color.Color():
        return self.color

    def setColor(self, color: pygame.Color.Color()):
        self.color = color

    def move(self, hor: int, vert: int):
        self.posx += hor
        self.posy += vert

    def draw(self):
        pygame.draw.rect()
