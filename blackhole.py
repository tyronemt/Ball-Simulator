# Black_Hole is derived from Simulton only, updating by finding+removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
from cmath import sqrt


class Black_Hole(Simulton):

    def __init__(self,xcoor,ycoor):
        Simulton.__init__(self,xcoor,ycoor,20,20)
        self._color = "Black"
        self._x = xcoor
        self._y = ycoor


    def update(self,model):
        target = model.find(Prey)
        destroy = []
        for x in target:
            if self.contains(x):
                destroy.append(x)
        destroy = set(destroy)
        for i in destroy:
            model.remove(i)
        return destroy
         
    def contains(self,target):
        return self.distance(target.get_location()) <= (self.get_dimension()[0]/2)
             
    
    def display(self,canvas):
       canvas.create_oval(self._x-(self.get_dimension()[0]/2)      , self._y-(self.get_dimension()[0]/2),
                                self._x+(self.get_dimension()[0]/2), self._y+(self.get_dimension()[0]/2),
                                fill=self._color)