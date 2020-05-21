

import pygame

from classes.main_scene import MainScene
from classes.general import Input


class Game(object):
    def __init__(self):
        # Used to prevent high latency of buffer
        # Arguments(frequency, size, channel, buffer)
        # Channel argument: 1 mono, 2 stereo
        # Buffer: must be a power of 2
        pygame.mixer.pre_init(22100, -16, 2, 64)
        # Inicialize pygame modules
        pygame.init()

        # Screen parameters
        self.width = 800
        self.height = 600
        self.display = pygame.display.set_mode((self.width, self.height))
        # App parameters
        self.clock = pygame.time.Clock()
        self.clock_tick = 20
        self.scene = None

        self.input = Input(self)

    def get_display(self) -> pygame.Surface:
        return self.display

    def get_input(self) -> Input:
        return self.input

    def run(self):
        self.run_pesentation_scene()
        self.run_menu_scene()

    def run_pesentation_scene(self):
        pass

    def run_menu_scene(self):
        pass
        self.run_main_scene()

    def run_main_scene(self):
        self.scene = MainScene(self)
        self.scene.play()

    def clear_screen(self, color: pygame.Color):
        # Clear screen
        self.display.fill(color)

    def clock(self):
        self.clock.tick(self.clock_tick)

    def quit(self):
        pygame.quit()
        quit()
