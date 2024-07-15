import pygame
from   pygame.locals import *

class Event():

    def __init__( self, composite ):
        self.composite = composite

    """Controller for this class"""
    def on_event( self, event ):
        if event.type == pygame.QUIT:
            self.composite.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                self.composite.running = False
