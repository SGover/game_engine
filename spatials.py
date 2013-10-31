import settings
import controls
import pygame
time_interval=0.001*1000/settings.FPS

    
class spatial():
    def __init__(self,rect, z, color):
        self.posZ= z
        self.rect = rect
        self.color = color
    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect, 0)
    def on_screen( minX, maxX, minY, maxY):
        if rect.right<minX or rect.left>maxX :
            return False
        if rect.top<minY or rect.bottom>maxY :
            return False
        return True
    def update(self):
        pass
class dynSpatial(spatial):    
        def __init__(self,rect,z, color):
            spatial.__init__(self,rect,z,color)            
            self.v=(0,0)
            self.a=(0,0)            
            controls=[]
        def addControl(control):
            control.setSpatial(self)
            controls.append(control)
        def update(self):
            self.v+=a*interval
            self.rect.x+=self.v[0]*time_interval
            for control in controls:
                control.update()
        def stop(self):
            self.v=(0,0)
            self.a=(0,0)

        

