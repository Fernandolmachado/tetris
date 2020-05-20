# Author............: Fernando Machado
# Date...............: 12/05/2020

import pygame

from classes.GroupL import GroupL
from classes.GroupO import GroupO


class MainScene(object):
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
        self.run = False

        self.bgColor = pygame.Color(34, 23, 153)

        # Sound instatiations
        # sound = pygame.mixer.Sound("file")

        self.reset()

    def reset(self):
        # Componentes
        self.board = None

        # input control attributes
        self.horizontalInput = 0
        self.fastInput = False
        self.turnInput = False

        # Teste
        self.group = GroupO(100, 100, 20)

    def play(self):
        self.setup()
        while self.run:
            self.clock.tick(self.clock_tick)
            self.checkEvents()
            self.transform()
            self.update()
        pygame.quit()

    def setup(self):
        self.run = True

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.turnInput = True
                if event.key == pygame.K_DOWN:
                    self.fastInput = True
                if event.key == pygame.K_LEFT:
                    self.horizontalInput = -1
                elif event.key == pygame.K_RIGHT:
                    self.horizontalInput = 1

    def transform(self):
        if self.fastInput:
            # Change clock
            pass

        if self.turnInput:
            # Rotate group
            self.group.rotate()
            self.turnInput = False

        if self.horizontalInput != 0:
            pass

    def update(self):
        # Clear screen
        self.display.fill(self.bgColor)

        self.group.update(self.display)
        # Update the screen with new shape
        pygame.display.update()
