# The special object acts like a ball but every 100 cycle each special object doubles. It can get very chaotic and push
# your computer to its limit so be careful when using it.

from prey import Prey

class Special(Prey): 
    radius = 5
    
    def __init__(self,xcoor,ycoor):
        Prey.__init__(self,xcoor,ycoor,10,10,0,5)
        self._color = "Red"
        self.randomize_angle()
        self._x = xcoor
        self._y = ycoor
        self.time = 0
    
    def update(self,model):
        self.move()
        self.wall_bounce()
        self.time = self.time + 1
        if self.time == 10:
            self.time = 0
            object = Special(self._x,self._y)
            model.add(object)
        
    def display(self,canvas):
       canvas.create_oval(self._x-(self.get_dimension()[0]/2)      , self._y-(self.get_dimension()[0]/2),
                                self._x+(self.get_dimension()[0]/2), self._y+(self.get_dimension()[0]/2),
                                fill=self._color)