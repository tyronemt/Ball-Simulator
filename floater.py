# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    def __init__(self,xcoor,ycoor):
        Prey.__init__(self,xcoor,ycoor,10,10,0,5)
        self.randomize_angle()
        self._image = PhotoImage(file='ufo.gif')
        self._x = xcoor
        self._y = ycoor
        
    def update(self,model):
        probability =  random()
        if probability <= 0.3:
            random_angle = random() - .5
            self._angle += random_angle
            random_speed = random() - .5
            self._speed += random_speed
            if self._speed > 7: 
                self._speed = 7
            elif self._speed < 3:
                self._speed = 3  
        self.move()
        self.wall_bounce()

    
    def display(self,the_canvas):
        the_canvas.create_image(*self.get_location(),image=self._image)
