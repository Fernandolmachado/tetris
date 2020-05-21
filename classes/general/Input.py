
import pygame

from classes import Game


class Input(object):
    def __init__(self, game: Game):
        self.game = game
        self.esc = False
        self.enter = False
        self.space = False
        self.vertical = 0
        self.horizontal = 0

    def get_space(self):
        return self.space

    def release_space(self):
        self.space = False

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.esc = True
                if event.key == pygame.K_RETURN:
                    self.enter = True
                if event.key == pygame.K_SPACE:
                    self.space = True
                if event.key == pygame.K_DOWN:
                    self.vertical = -1
                elif event.key == pygame.K_UP:
                    self.vertical = 1
                if event.key == pygame.K_LEFT:
                    self.horizontal = -1
                elif event.key == pygame.K_RIGHT:
                    self.horizontal = 1
