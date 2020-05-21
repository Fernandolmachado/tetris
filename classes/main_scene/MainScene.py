# Author............: Fernando Machado
# Date...............: 19/05/2020

import pygame

from classes import Game
from classes.main_scene.GroupI import GroupI
from classes.main_scene.GroupO import GroupO
from classes.main_scene.GroupT import GroupT
from classes.main_scene.GroupJ import GroupJ
from classes.main_scene.GroupL import GroupL
from classes.main_scene.GroupS import GroupS
from classes.main_scene.GroupZ import GroupZ


class MainScene(object):
    def __init__(self, game: Game):
        self.game = game
        self.run = False
        self.bg_color = pygame.Color(34, 23, 153)
        self.reset()

    def reset(self):
        # Componentes
        self.board = None
        self.group0 = GroupI(100, 100, 20)
        self.group1 = GroupO(200, 100, 20)
        self.group2 = GroupT(300, 100, 20)
        self.group3 = GroupJ(400, 100, 20)
        self.group4 = GroupL(500, 100, 20)
        self.group5 = GroupS(600, 100, 20)
        self.group6 = GroupZ(700, 100, 20)

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
            self.group0.rotate()
            self.group1.rotate()
            self.group2.rotate()
            self.group3.rotate()
            self.group4.rotate()
            self.group5.rotate()
            self.group6.rotate()
            self.game.get_input().release_space()

    def update(self):
        # Clear screen
        self.game.clear_screen(self.bg_color)

        self.group0.update(self.game.get_display())
        self.group1.update(self.game.get_display())
        self.group2.update(self.game.get_display())
        self.group3.update(self.game.get_display())
        self.group4.update(self.game.get_display())
        self.group5.update(self.game.get_display())
        self.group6.update(self.game.get_display())
        # Update the screen with new shape
        pygame.display.update()
