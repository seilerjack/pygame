import pygame
from   pygame.locals import *

SURFACE_COLOR = (167, 255, 100)

class Render():

    def __init__( self, composite ):
        self.composite = composite

    def getPos():
        pos = pygame.mouse.get_pos()
        return ( pos )
    
    def draw_background( self ):
        self.composite.display_surf.fill( SURFACE_COLOR )

    def draw_sprite( self ):
        self.composite.all_sprites_list.draw( self.composite.display_surf ) 
        pygame.display.flip()

    """Controller for this class"""
    def on_render( self ):

        self.composite.all_sprites_list.update()
        self.draw_background()
        self.draw_sprite()
        self.composite.clock.tick( 60 )

