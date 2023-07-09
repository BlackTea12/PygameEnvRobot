import pygame
# ccw: +
# cw: -
class robotDD:
    def __init__(self, display):
        self.front = pygame.image.load("img/dd_front.png")
        self.front = pygame.transform.scale(self.front, (80,80))
        self.back = pygame.image.load("img/dd_back.png")
        self.back = pygame.transform.scale(self.back, (80,80))
        self.left = pygame.image.load("img/dd_left_back.png")
        self.left = pygame.transform.scale(self.left, (80,80))
        self.right = pygame.image.load("img/dd_right_back.png")
        self.right = pygame.transform.scale(self.right, (80,80))
        self.display = display
        
    def move(self, x, y, dtheta, v, w):
        self.Update(dtheta)
        if v > 0:
            if w > 0:
                self.display.blit(self.left, (x,y))
            elif w < 0:
                self.display.blit(self.right, (x,y))
            else:
                self.display.blit(self.front, (x,y))
        elif v < 0:
            if w > 0:
                self.display.blit(self.right, (x,y))
            elif w < 0:
                self.display.blit(self.left, (x,y))
            else:
                self.display.blit(self.back, (x,y))
        else:
            self.display.blit(self.front, (x,y))
            
    # keep in track of rotation for every image
    def Update(self, dtheta):
        self.front = pygame.transform.rotate(self.front, dtheta)
        self.back = pygame.transform.rotate(self.back, dtheta)
        self.left = pygame.transform.rotate(self.left, dtheta)
        self.right = pygame.transform.rotate(self.right, dtheta)