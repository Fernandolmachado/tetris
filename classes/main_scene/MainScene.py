# Author............: Fernando Machado
# Date...............: 12/05/2020

import pygame

from classes import Game
from classes.main_scene.GroupL import GroupL


class MainScene(object):
    def __init__(self, game: Game):
        self.game = game
        self.run = False
        self.bgColor = pygame.Color(34, 23, 153)
        self.reset()

    def reset(self):
        # Componentes
        self.board = None
        self.group = GroupL(100, 100, 20)

    def play(self):
        self.setup()
        while self.run:
            self.game.get_input().check_events()
            self.transform()
            self.update()

    def setup(self):
        self.run = True

    def transform(self):
        if self.game.get_input().get_space():
            # Rotate group
            self.group.rotate()
            self.game.get_input().release_space()

    def update(self):
        # Clear screen
        self.game.clear_screen(self.bgColor)

        self.group.update(self.game.get_display())
        # Update the screen with new shape
        pygame.display.update()
