from pygame.locals import *
import pygame,sys
from pygame.locals import *

class baseHandler:
    def __init__(self):
        pass
    def handle_input(self,event):
            if event.type== QUIT :
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) :
                    doLeftAction()
                elif (event.key == K_RIGHT or event.key == K_d):
                    doUpAction()
                elif (event.key == K_UP or event.key == K_w):
                    doUpAction()
                elif (event.key == K_DOWN or event.key == K_s) and gameSnake.direction!= (0,-1):
                    doDownAction()
    def doDownAction(self):
        pass
    def doUpAction(self):
        pass
    def doRightAction(self):
        pass    
    def doLeftAction(self):
        pass    



    
    
