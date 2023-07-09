BLACK = (20,20,40)
LIGHTBLUE = (0,120,255)
DARKBLUE = (0,40,160)
RED = (255,100,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREY = (70,70,70)

import pygame, sys
from pygame.locals import *

class PyGameDisplay:
    def __init__(self, screen_W, screen_H):
        self.Width = screen_W
        self.Height = screen_H
        self.screen_size = [self.Width, self.Height]
        pygame.init()        
        pygame.display.set_caption("Algorithm Testing...")
        self.Screen = pygame.display.set_mode(self.screen_size) # initialise Pygame display screen
        pygame.mouse.set_visible(0)

    def Play(self, dT):
        clock = pygame.time.Clock()
        toggle = True
        while True:
            clock.tick(dT) # fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            if toggle:     
                self.Screen.fill(LIGHTBLUE)
                toggle = False
            else:
                self.Screen.fill(BLACK)
                toggle = True
            pygame.display.update()
            
            
if __name__ == '__main__':
    # testing screen
    game = PyGameDisplay(300,400)
    game.Play(1)
    pygame.quit()
    quit()