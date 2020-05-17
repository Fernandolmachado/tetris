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
        width = 1080
        height = 1848
        self.display = pygame.display.set_mode((width, height))

        # App parameters
        self.clock = pygame.time.Clock()
        self.clock_tick = 20
        self.run = False

        # Sound instatiations
        # sound = pygame.mixer.Sound("file")

        self.reset()

    def reset(self):
        """
        Class attributes that can be reseted
        """

        # Click control attributes
        self.click_point = None
        self.clicked = False

    def play(self):
        """
        Main loop
        """
        self.setup()
        while self.run:
            self.clock.tick(self.clock_tick)
            self.events()
            self.render()
            self.draws()

    def setup(self):
        """
        Setup before loop
        """
        self.run = True

    def checkEvents(self):
        """
        Events threats
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.click_point = event.pos
                self.clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                # assign False to self.clicked here, to implement
                # continuous pushies
                self.clicked = False

    def transform(self):
        """
        Manipulation of images and geometry
        """
        if self.clicked:
            # assign False to self.clicked here, to prevent
            # continuous pushies insteady of self.events
            # self.clicked = False
            pass
        else:
            pass

    def update(self):
        """
        Draw objects on screen
        """
        # Clear screen
        self.display.fill()

        # Update the screen with new shape
        pygame.display.update()
