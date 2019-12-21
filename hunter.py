# Hunter is derived from each of the Mobile_Simulton and Pulsator classes:
#   updating/displaying like a Pulsator, but also moving (either in a straight
#   line or in pursuit of Prey).


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
from builtins import object


class Hunter(Pulsator, Mobile_Simulton):
    def __init__(self,xcoor,ycoor):
        Pulsator.__init__(self,xcoor,ycoor)
        Mobile_Simulton.__init__(self,xcoor,ycoor,20,20,0,5)
        self.randomize_angle()
        self._x = xcoor
        self._y = ycoor
        
    def update(self,model):
        self.move()
        self.wall_bounce()
        target = model.find(Prey)
        Pulsator.update(self,model)
        prey = None
        prey_distance = 0
        for object in target:
            if self.distance(object.get_location())  - prey_distance < 200:
                prey = object
                prey_distance = self.distance(object.get_location())
            else:
                prey = None
                prey_distance = 0
        if prey != None:
            self.set_angle(atan2(prey.get_location()[1] - self.get_location()[1],
                                 prey.get_location()[0] - self.get_location()[0]
                                 ))
    
    def display(self,canvas):
       canvas.create_oval(self._x-(self.get_dimension()[0]/2), self._y-(self.get_dimension()[0]/2),
                                self._x+(self.get_dimension()[0]/2), self._y+(self.get_dimension()[0]/2),
                                fill=self._color)