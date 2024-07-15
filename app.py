import pygame

from pygame.locals   import *

from loop            import Loop
from events          import Event
from render          import Render


SURFACE_COLOR = ( 167, 255, 100 )
SCREEN_HEIGHT = 896
SCREEN_WIDTH  = 414
WHITE         = ( 255, 255, 255 )

class Block( pygame.sprite.Sprite ):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__( self, color, width, height ):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__( self )

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface( [ width, height ] )
       self.image.fill( color )

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.clamp_ip( ( 0, 0 ), ( SCREEN_WIDTH, SCREEN_HEIGHT ) )

    def moveRight( self, pixels ):
        self.rect.x += pixels
 
    def moveLeft( self, pixels ):
        self.rect.x -= pixels
 
    def moveForward( self, speed ):
        self.rect.y += speed * speed/10
 
    def moveBack( self, speed ):
        self.rect.y -= speed * speed/10

    def check_boundaries( self ):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

 
class App():

    def __init__( self ):
        # program details
        self.running      = True
        self.display_surf = None
        self.clock         = pygame.time.Clock()
        self.sprite        = Block( WHITE, 20, 20 )
        
        # size of iPhone 11
        self.size = self.width, self.height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.all_sprites_list = pygame.sprite.Group() 
        
        # program structure
        self.events = Event( self )
        self.loop   = Loop( self )
        self.render = Render( self )

 
    def on_init( self ):
        pygame.init()
        self.display_surf = pygame.display.set_mode( self.size, pygame.NOFRAME | pygame.DOUBLEBUF )
        self.running = True
        self.all_sprites_list.add( self.sprite )


    def on_cleanup( self ):
        pygame.quit()

 
    """Controller for this class"""
    def on_execute( self ):
        if self.on_init() == False:
            self.running = False

        while( self.running ):
            for event in pygame.event.get():
                self.events.on_event( event )

            self.loop.on_loop()
            self.render.on_render()

        self.on_cleanup()


if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
