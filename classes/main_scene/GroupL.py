
import pygame

from classes.main_scene.Group import Group
from classes.main_scene.Block import Block


class GroupL(Group):
    def __init__(self, posx: int, posy: int, block_size: int):
        super().__init__(posx, posy, block_size, 3)
        self.color = pygame.Color(0xFF, 0x00, 0x7D)
        self.blocks = list()
        self._generate_blocks()

    def rotate(self):
        self.surface = pygame.transform.rotate(self.surface, 90)
        self._redefine_angle()

    def _generate_blocks(self):
        # Bloco central
        self.blocks.append(
            Block(
                self.block_size,
                self.block_size,
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
                self.block_size,
                self.block_size * 2,
                self.block_size,
                self.color,
                dead_zone=self.block_size // 10
            )
        )

        # Bloco inferior direito
        self.blocks.append(
            Block(
                self.block_size * 2,
                self.block_size * 2,
                self.block_size,
                self.color,
                dead_zone=self.block_size // 10
            )
        )

        for block in self.blocks:
            block.draw(self.surface)

    def _redefine_angle(self):
        if self.angle == 0:
            self.angle = 1
            self.blocks[1].set_position(
                self.block_size * 2,
                self.block_size
            )
            self.blocks[2].set_position(
                0,
                self.block_size
            )
            self.blocks[3].set_position(
                0,
                self.block_size * 2
            )
        elif self.angle == 1:
            self.angle = 2
            self.blocks[1].set_position(
                self.block_size,
                self.block_size * 2
            )
            self.blocks[2].set_position(
                self.block_size,
                0
            )
            self.blocks[3].set_position(
                0,
                0
            )
        elif self.angle == 2:
            self.angle = 3
            self.blocks[1].set_position(
                0,
                self.block_size
            )
            self.blocks[2].set_position(
                self.block_size * 2,
                self.block_size
            )
            self.blocks[3].set_position(
                self.block_size * 2,
                0
            )
        else:
            self.angle = 0
            self.blocks[1].set_position(
                self.block_size,
                0
            )
            self.blocks[2].set_position(
                self.block_size,
                self.block_size * 2
            )
            self.blocks[3].set_position(
                self.block_size * 2,
                self.block_size * 2
            )
