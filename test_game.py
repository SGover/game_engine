from baseGame import game
from settings import *
from spatials import spatial
from inputHandlers import keyDownHandler
from pygame.locals import *

import pygame

x=20
y=30
spatials=[]
def moveBy_s():
    mySpatial.rect=mySpatial.rect.move(10,10)
rect=pygame.Rect(x,y,30,30)
mySpatial=spatial(rect,2,BLUE)
handler=keyDownHandler([(K_s,moveBy_s)])
spatials.append(mySpatial)                       
mygame = game(spatials,handler)
mygame.run()
