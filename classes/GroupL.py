
import pygame

from classes.Group import Group
from classes.Block import Block


class GroupL(Group):
    def __init__(self, posx: int, posy: int, blockSize: int):
        super().__init__(posx, posy, blockSize)
        self.color = pygame.Color(0xFF, 0x00, 0x7D)
        self.blocks = list()
        self._generateBlocks()

    def rotate(self):
        self.surface = pygame.transform.rotate(self.surface, 90)
        self._redefineAngle()

    def _generateBlocks(self):
        # Bloco central
        self.blocks.append(
            Block(
                self.blockSize,
                self.blockSize,
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
                self.blockSize,
                self.blockSize * 2,
                self.blockSize,
                self.color,
                deadZone=self.blockSize // 10
            )
        )

        # Bloco inferior direito
        self.blocks.append(
            Block(
                self.blockSize * 2,
                self.blockSize * 2,
                self.blockSize,
                self.color,
                deadZone=self.blockSize // 10
            )
        )

        for block in self.blocks:
            block.draw(self.surface)

    def _redefineAngle(self):
        if self.angle == 0:
            self.angle = 1
            self.blocks[1].setPosition(
                self.blockSize * 2,
                self.blockSize
            )
            self.blocks[2].setPosition(
                0,
                self.blockSize
            )
            self.blocks[3].setPosition(
                0,
                self.blockSize * 2
            )
        elif self.angle == 1:
            self.angle = 2
            self.blocks[1].setPosition(
                self.blockSize,
                self.blockSize * 2
            )
            self.blocks[2].setPosition(
                self.blockSize,
                0
            )
            self.blocks[3].setPosition(
                0,
                0
            )
        elif self.angle == 2:
            self.angle = 3
            self.blocks[1].setPosition(
                0,
                self.blockSize
            )
            self.blocks[2].setPosition(
                self.blockSize * 2,
                self.blockSize
            )
            self.blocks[3].setPosition(
                self.blockSize * 2,
                0
            )
        else:
            self.angle = 0
            self.blocks[1].setPosition(
                self.blockSize,
                0
            )
            self.blocks[2].setPosition(
                self.blockSize,
                self.blockSize * 2
            )
            self.blocks[3].setPosition(
                self.blockSize * 2,
                self.blockSize * 2
            )
