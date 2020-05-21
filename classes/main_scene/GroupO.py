
import pygame

from classes.main_scene.Group import Group
from classes.main_scene.Block import Block


class GroupO(Group):
    def __init__(self, posx: int, posy: int, block_size: int):
        super().__init__(posx, posy, block_size, 2)
        self.color = pygame.Color(0xFF, 0x00, 0x00)
        self.blocks = list()
        self._generate_blocks()

    def rotate(self):
        self.surface = pygame.transform.rotate(self.surface, 90)
        self._redefineAngle()

    def _generate_blocks(self):
        # Bloco central
        self.blocks.append(
            Block(
                0,
                0,
                self.block_size,
                self.color,
                dead_zone=self.block_size // 10
            )
        )

        # Bloco superior central
        self.blocks.append(
            Block(
                self.block_size,
                0,
                self.block_size,
                self.color,
                dead_zone=self.block_size // 10
            )
        )

        # Bloco inferior central
        self.blocks.append(
            Block(
                0,
                self.block_size,
                self.block_size,
                self.color,
                dead_zone=self.block_size // 10
            )
        )

        # Bloco inferior direito
        self.blocks.append(
            Block(
                self.block_size,
                self.block_size,
                self.block_size,
                self.color,
                dead_zone=self.block_size // 10
            )
        )

        for block in self.blocks:
            block.draw(self.surface)

    def _redefineAngle(self):
        # Não precisa modificar o rect dos blocos
        pass
