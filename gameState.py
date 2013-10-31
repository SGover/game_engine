import pygame,sys
from spatials import *
from pygame.locals import *
from settings import *
from inputHandlers import baseHandler

class gameState():
    def __init__(self,spatials,handler,color):                            
        self.spatials=spatials
        self.inputHandler=handler
        self.isRunning=False
        self.color=color
        self.surf=pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    def run(self,fpsClock,FPS):
        self.isRunning=True
        while True :            
            self.background_draw()
            for event in pygame.event.get():
                self.inputHandler.handle_input(event)            
            self.update()
            self.draw()
            self.drawHUD()
            pygame.display.update()
            fpsClock.tick(FPS)
    def stop(self):
        self.isRunning=False
    def update(self):
        for s in self.spatials:
            s.update()    
    def background_draw(self):
        self.surf.fill(self.color)
    def drawHUD(self):
        pass
    
    def draw(self):
        for s in self.spatials:
            s.draw(self.surf)
               



class button():
    def __init__(self,rect,text,textSize,action):
        self.rect=rect
        self.text=text
        self.textSize=textSize
        self.action=action
        self.focus=false        
    def activate():
        action()
    def draw(surface):
        pass
    def isOnButton(point):
        return self.rect.collidepoint(point)
        
            
