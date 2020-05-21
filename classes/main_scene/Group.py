
import pygame


class Group(object):
    def __init__(self, posx: int, posy: int, block_size: int, grade: int):
        self.posx = posx
        self.posy = posy
        self.block_size = block_size
        self.size = block_size * grade
        self.centerx = self.size - self.posx
        self.centery = self.size - self.posy
        self.blocks = list()
        self.surface = self._create_surface()
        self.color = None
        self.angle = 0

    def get_size(self) -> int:
        return self.size

    def set_size(self, size: int):
        self.size = size
        self.__redefine_center()

    def get_position(self) -> tuple:
        return (self.posx, self.posy)

    def set_position(self, posx: int, posy: int):
        self.posx = posx
        self.posy = posy
        self.__redefine_center()

    def get_center(self) -> tuple:
        return (self.centerx, self.centery)

    def get_blocks(self) -> tuple:
        return self.blocks

    def get_surface(self) -> pygame.Surface:
        return self.surface

    def move(self, horiz: int, vert: int):
        self.posx += horiz
        self.posy += vert
        self.__redefine_center()

    def update(self, surface: pygame.Surface):
        surface.blit(self.surface, (self.posx, self.posy))

    def _redefine_center(self):
        self.centerx = self.size - self.posx
        self.centery = self.size - self.posy

    def _create_surface(self):
        surface = pygame.Surface((self.size, self.size)).convert_alpha()
        surface.fill((255, 255, 255, 0))
        return surface

    # Implementar na sub-classe
    def rotate(self):
        pass

    def _generate_blocks(self):
        pass

    def _redefine_angle(self):
        pass
