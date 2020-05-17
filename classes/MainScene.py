# Author............: Fernando Machado
# Date...............: 12/05/2020

import pygame


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
        self.width = 1080
        self.height = 1848
        self.display = pygame.display.set_mode((self.width, self.height))

        # App parameters
        self.clock = pygame.time.Clock()
        self.clock_tick = 20
        self.run = False

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

    def play(self):
        self.setup()
        while self.run:
            self.clock.tick(self.clock_tick)
            self.events()
            self.render()
            self.draws()

    def setup(self):
        self.run = True

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def transform(self):
        if self.fastInput:
            # Change clock
            pass
        elif self.turnInput:
            # Rotate group
            pass

    def update(self):
        # Clear screen
        self.display.fill()

        # Update the screen with new shape
        pygame.display.update()
