# Author............: Fernando Machado
# Date...............: 19/05/2020

import pygame


class Group(object):
    """
    Classe de Interface para construção e manipulação das formas
        presentes no jogo.
    Parâmetros:
        posx = Posição lateral esquerda da Surface à partir da origem
                da tela (0).
        posx = Posição superior da Surface à partir da origem da tela (0).
        block_size = Dimensão (base e altura) dos blocos da forma.
        grade = Quantidade de colunas e linhas da grade da forma.
    """
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
        """
        Retorna a dimensão da Surface (base = altura).
        Parâmentros: Nenhum.
        Retorno: Dimensão da surface - int.
        """
        return self.size

    def set_size(self, size: int):
        """
        Redefine a dimensão da Surface (base = altura).
        Parâmentros:
            size = Nova dimensão da Surface - int.
        Retorno: Nenhum.
        """
        self.size = size
        self.__redefine_center()

    def get_position(self) -> tuple:
        """
        Retorna a posição (x, y) da Surface.
        Parâmentros: Nenhum.
        Retorno: Posição da surface (x, y) - tuple.
        """
        return (self.posx, self.posy)

    def set_position(self, posx: int, posy: int):
        """
        Redefine a posição (x, y) da Surface.
        Parâmentros:
            posx = Valor de x para nova coordenada.
            posy = Valor de y para nova coordenada.
        Retorno: Nenhum.
        """
        self.posx = posx
        self.posy = posy
        self.__redefine_center()

    def get_center(self) -> tuple:
        """
        Retorna a posição central (x, y) da Surface.
        Parâmentros: Nenhum.
        Retorno: Posição central da surface (x, y) - tuple.
        """
        return (self.centerx, self.centery)

    def get_blocks(self) -> tuple:
        """
        Retorna os blocos presentes no grupo.
        Parâmentros: Nenhum.
        Retorno: tupla de Block - tuple.
        """
        return self.blocks

    def get_surface(self) -> pygame.Surface:
        """
        Retorna a Surface do grupo.
        Parâmentros: Nenhum.
        Retorno: Surface do grupo - pygame.Surface.
        """
        return self.surface

    def move(self, horiz: int, vert: int):
        """
        Move a Surface horiz em x e vert em y.
        Parâmentros:
            horiz = Valor a ser somado com posx.
            posy = Valor a ser somado com posy.
        Retorno: Nenhum.
        """
        self.posx += horiz
        self.posy += vert
        self.__redefine_center()

    def update(self, surface: pygame.Surface):
        """
        Atualiza situação da Surface (forma) na Surface (pai).
        Parâmentros:
            surface = Surface pai = pygame.Surface
        Retorno: Nenhum.
        """
        surface.blit(self.surface, (self.posx, self.posy))

    def _redefine_center(self):
        """
        Atualiza posição do centro dda Surface.
        Parâmentros: Nenhum.
        Retorno: Nenhum.
        """
        self.centerx = self.size - self.posx
        self.centery = self.size - self.posy

    def _create_surface(self):
        """
        Cria surface da instância.
        Parâmentros: Nenhum.
        Retorno: Surface criada - pygame.Surface.
        """
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
