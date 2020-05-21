# Author............: Fernando Machado
# Date...............: 19/05/2020

import pygame


class Block(object):
    """
    Classe que representa o bloco que quando agregados a outros,
    formam as peças presentes no jogo.

    Parâmetros:
        posx = Posição lateral esquerda do bloco à partir da origem
                da Surface.
        posx = Posição superior do bloco à partir da origem da Surface.
        size = Dimensão (base e altura) do bloco.
        color = Cor do bloco.
        dead_zone = Margem do bloco à partir de posx e posy. default = 0.
    """
    def __init__(self, posx: int, posy: int, size: int, color, dead_zone=0):
        self.size = size
        self.posx = posx
        self.posy = posy
        self.color = color
        self.dead_zone = dead_zone

    def get_size(self) -> int:
        """
        Retorna a dimensão do bloco (base = altura).
        Parâmentros: Nenhum.
        Retorno: Dimensão do bloco - int.
        """
        return self.size

    def set_size(self, size: int):
        """
        Redefine a dimensão do bloco (base = altura).
        Parâmentros:
            size = Nova dimensão do bloco - int.
        Retorno: Nenhum.
        """
        self.size = size

    def get_position(self) -> tuple:
        """
        Retorna a posição do bloco (coordenada do canto superior esquerdo).
        Parâmentros: Nenhum.
        Retorno: tupla com coordenada do canto superior esquerdo do bloco.
        """
        return (self.posx, self.posy)

    def set_position(self, posx: int, posy: int):
        """
        Redefine a posição do bloco (coordenada do canto superior esquerdo).
        Parâmentros:
            posx = Nova posição x do bloco - int.
            posy = Nova posição y do bloco - int.
        Retorno: Nenhum.
        """
        self.posx = posx
        self.posy = posy

    def get_color(self) -> pygame.Color:
        """
        Retorna a cor do bloco.
        Parâmentros: Nenhum.
        Retorno: pygame.Color.
        """
        return self.color

    def set_color(self, color: pygame.Color):
        """
        Redefine a cor do bloco.
        Parâmentros:
            color = Nova cor do bloco - pygame.Color.
        Retorno: Nenhum.
        """
        self.color = color

    def get_react(self) -> tuple:
        """
        Retorna o rect do bloco.
        Parâmentros: Nenhum.
        Retorno: tupla (posx, posy, size, size)
        """
        return (self.posx, self.posy, self.size, self.size)

    def move(self, hor: int, vert: int):
        """
        Incrementa ou decrementa as posições x e y do bloco.
        Parâmentros:
            hor = Valor a ser incrementado em x - int.
            vert = Valor a ser incrementado em y - int.
        Retorno: Nenhum.
        """
        self.posx += hor
        self.posy += vert

    def draw(self, surface):
        """
        Desenha o bloco em um Surface.
        Parâmentros:
            surface = Surface onde o bloco será desenhado - pygame.Surface.
        Retorno: Nenhum.
        """
        pygame.draw.rect(
            surface,
            self.color,
            (
                self.posx + self.dead_zone // 2,
                self.posy + self.dead_zone // 2,
                self.size - self.dead_zone,
                self.size - self.dead_zone
            )
        )
