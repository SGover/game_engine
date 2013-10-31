import pygame,sys
from spatials import *
from pygame.locals import *
from settings import *
from inputHandlers import baseHandler
class game():
    def __init__(self,states,startState):        
        pygame.init()
        pygame.key.set_repeat(100, 300)
        self.fpsClock=pygame.time.Clock()                        
        self.states=states
        self.currState=self.states[startState]
    def run(self):
        self.currState.run(self.fpsClock,FPS)
    def changeState(self,stateName):        
        self.currState.stop()
        self.currState=self.states[stateName]
        self.currState.run(self.fpsClock,FPS)

