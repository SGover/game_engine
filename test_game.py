from baseGame import game
from settings import *
from spatials import dynSpatial
from inputHandlers import keyDownHandler
from pygame.locals import *
from controls import *
import pygame

x=20
y=30
spatials=[]
def moveBy_s():
    mySpatial.rect=mySpatial.rect.move(10,10)
rect=pygame.Rect(x,y,20,20)
mySpatial=dynSpatial(rect,2,BLUE)
mySpatial.addControl(repControl((200,200),(140,140),70))
handler=keyDownHandler([(K_s,moveBy_s)])
spatials.append(mySpatial)                       
mygame = game(spatials,handler)
mygame.run()
