import pygame,sys
from spatials import *
from pygame.locals import *
from settings import *
from inputHandlers import baseHandler

class game():
    def __init__(self,spatials):
        pygame.init()
        self.fpsClock=pygame.time.Clock()
        self.surf=pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        self.lost=False
        self.spatials=spatials
        self.inputHandler=baseHandler()
    def run(self):
        while True :
            if lost:
                pygame.quit()
                sys.exit()
            self.background_draw()
            self.inputHandler.handle_input()
            self.update()
            self.draw()
            pygame.display.update()
            self.fpsClock.tick(FPS)
    def update():
        for s in spatials:
            spatials.update()    
                

