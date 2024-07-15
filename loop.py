import pygame
from   pygame.locals import *

class Loop():

    def __init__( self, composite ):
        self.composite = composite

    """Controller for this class"""
    def on_loop( self ):
        self.move_player()

    def move_player( self ):
        keys = pygame.key.get_pressed()
        if keys[ pygame.K_LEFT ]:
            self.composite.sprite.moveLeft( 5 )
            self.composite.sprite.check_boundaries()
        if keys[ pygame.K_RIGHT ]:
            self.composite.sprite.moveRight( 5 )
            self.composite.sprite.check_boundaries()
        if keys[ pygame.K_DOWN ]:
            self.composite.sprite.moveForward( 5 )
            self.composite.sprite.check_boundaries()
        if keys[ pygame.K_UP ]:
            self.composite.sprite.moveBack( 5 )
            self.composite.sprite.check_boundaries()
