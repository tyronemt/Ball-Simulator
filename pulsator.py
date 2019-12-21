# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    def __init__(self,xcoor,ycoor):
        Black_Hole.__init__(self,xcoor,ycoor)
        self._x = xcoor
        self._y = ycoor
        self.time = 0

    def update(self,model):
        destroy = Black_Hole.update(self,model)
        if len(destroy) < 1:
            self.time = self.time + 1
            if self.time == 30:
                self.change_dimension(-1,-1)
                self.time = 0
        elif len(destroy) >= 1:
            self.change_dimension(1,1)
            self.time = 0
        if self.get_dimension() == (0,0):
            model.remove(self)
            
    
    def display(self,canvas):
       canvas.create_oval(self._x-(self.get_dimension()[0]/2), self._y-(self.get_dimension()[0]/2),
                                self._x+(self.get_dimension()[0]/2), self._y+(self.get_dimension()[0]/2),
                                fill=self._color)