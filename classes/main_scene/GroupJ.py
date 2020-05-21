# Author............: Fernando Machado
# Date...............: 20/05/2020

import pygame

from classes.main_scene.Group import Group
from classes.main_scene.Block import Block


class GroupJ(Group):
    """
    Classe para construção e manipulação da forma J.
    Parâmetros:
        posx = Posição lateral esquerda da Surface à partir da origem
                da tela (0).
        posx = Posição superior da Surface à partir da origem da tela (0).
        block_size = Dimensão (base e altura) dos blocos da forma.
    """
    def __init__(self, posx: int, posy: int, block_size: int):
        super().__init__(posx, posy, block_size, 3)
        self.color = pygame.Color(0x00, 0xFF, 0x00)     # Verde
        self.blocks = list()
        self._generate_blocks()

    def rotate(self):
        """
        Gira a Surface 90 graus no sentido horário e atualiza posições
        dos blocos presentes.
        Parâmentros: Nenhum.
        Retorno: Nenhum.
        """
        self.surface = pygame.transform.rotate(self.surface, -90)
        self._redefine_angle()

    def _generate_blocks(self):
        """
        Desenha os blocos na Surface de acordo com sua forma e os adiciona
        a lista blocks.
        Parâmentros: Nenhum.
        Retorno: Nenhum.
        """
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

        # Bloco inferior esquerdo
        self.blocks.append(
            Block(
                0,
                self.block_size * 2,
                self.block_size,
                self.color,
                dead_zone=self.block_size // 10
            )
        )

        for block in self.blocks:
            block.draw(self.surface)

    def _redefine_angle(self):
        """
        Redefine as posições dos blocos, de acordo com o ângulo da
        Surface.
        Parâmentros: Nenhum.
        Retorno: Nenhum.
        """
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
                0
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
                self.block_size * 2,
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
                self.block_size * 2
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
                0,
                self.block_size * 2
            )
