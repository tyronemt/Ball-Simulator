# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).

from prey import Prey

class Ball(Prey): 
    radius = 5
    
    def __init__(self,xcoor,ycoor):
        Prey.__init__(self,xcoor,ycoor,10,10,0,5)
        self._color = "Blue"
        self.randomize_angle()
        self._x = xcoor
        self._y = ycoor
    
    def update(self,model):
        self.move()
        self.wall_bounce()
        
    def display(self,canvas):
       canvas.create_oval(self._x-Ball.radius      , self._y-Ball.radius,
                                self._x+Ball.radius, self._y+Ball.radius,
                                fill=self._color)
        