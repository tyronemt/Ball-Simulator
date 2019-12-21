import controller, sys
import model   # Pass a reference to model to each update call inside update_all

# Use the reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
cycle_count = 0
running = False
object_type = "Ball"
objects = set()

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,objects
    running     = False
    cycle_count = 0
    objects     = set()
    display_all()

#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global running,cycle_count
    running     = False
    cycle_count = cycle_count + 1
    for i in objects:
        i.update(model)


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global object_type
    object_type = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global object_type
    copy = objects.copy()
    if object_type == "Remove":
        for i in copy:
            if i.contains((x,y)):
                remove(i)
    else:
        object = eval(object_type + "(" + str(x) + "," + str(y) + ")")
        add(object)


#add simulton s to the simulation
def add(s):
    objects.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    objects.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    lst = []
    for i in objects:
        if issubclass(type(i), p):
            lst.append(i)
    return set(lst)


#call update() for all simultons in the simulation (pass model as its argument)
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count
    x = objects.copy()
    if running == True:
        cycle_count += 1
        for s in x:
            s.update(model)


#delete from the canvas all simultons being simulated; then call display on each
#  simulton being simulated to add it back to the canvas, possibly in a new location, to
#  animate it; also, update the progress label defined in the controller
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in objects:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(objects))+" objects/"+str(cycle_count)+" cycles")
