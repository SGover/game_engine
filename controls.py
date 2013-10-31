from math import sqrt
class control():
    
    def __init__(self):
        pass
    
    def setSpatial(self,spatial):
        self.spatial=spatial
    
    def update():
        pass
    
class repControl(control):
#'this control move the object in a reapat liniar way'
    def __init__(self,start,end,speed):
#        'get a starting point ,ending point and speed'
        self.start=start
        self.end=end
        self.speed=speed
        self.totalDis=sqrt((self.end[0]-self.start[0])**2+(self.end[1]-self.start[1])**2)
    def setSpatial(self,spatial):
        self.spatial=spatial
        spatial.moveTo(self.start)
        vel=(self.end[0]-self.start[0],self.end[1]-self.start[1])
        velSize=sqrt(vel[0]**2+vel[1]**2)
        self.spatial.v=(self.speed*vel[0]/velSize,self.speed*vel[1]/velSize)
    def update(self):        
        distance=sqrt((self.spatial.getX()-self.start[0])**2+(self.spatial.getY()-self.start[1])**2)
        if distance>self.totalDis:
            self.spatial.v=(self.spatial.v[0]*(-1),self.spatial.v[1]*(-1))
            self.start,self.end = self.end,self.start
        

