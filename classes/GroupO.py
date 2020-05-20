
import pygame

from classes.Group import Group
from classes.Block import Block


class GroupO(Group):
    def __init__(self, posx: int, posy: int, blockSize: int):
        super().__init__(posx, posy, blockSize, 2)
        self.color = pygame.Color(0xFF, 0x00, 0x00)
        self.blocks = list()
        self._generateBlocks()

    def rotate(self):
        self.surface = pygame.transform.rotate(self.surface, 90)
        self._redefineAngle()

    def _generateBlocks(self):
        # Bloco central
        self.blocks.append(
            Block(
                0,
                0,
                self.blockSize,
                self.color,
                deadZone=self.blockSize // 10
            )
        )

        # Bloco superior central
        self.blocks.append(
            Block(
                self.blockSize,
                0,
                self.blockSize,
                self.color,
                deadZone=self.blockSize // 10
            )
        )

        # Bloco inferior central
        self.blocks.append(
            Block(
                0,
                self.blockSize,
                self.blockSize,
                self.color,
                deadZone=self.blockSize // 10
            )
        )

        # Bloco inferior direito
        self.blocks.append(
            Block(
                self.blockSize,
                self.blockSize,
                self.blockSize,
                self.color,
                deadZone=self.blockSize // 10
            )
        )

        for block in self.blocks:
            block.draw(self.surface)

    def _redefineAngle(self):
        # Não precisa modificar o rect dos blocos
        pass
