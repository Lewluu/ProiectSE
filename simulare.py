import time
from pyglet.graphics import vertex_list
import sympy
import pyglet
from pyglet import shapes
from pyglet import clock

#init the window
window=pyglet.window.Window(1200,800)
window.set_location(350,150)

#stack every drawable in this variable
batch=pyglet.graphics.Batch()

#init the object
rectangle=shapes.Rectangle(125,125,100,100,color=(125,0,75),batch=batch)
rectangle.anchor_position=(50,50)
#polygon
points_list=[
    [50,50,50,750],
    [50,750,1150,750],
    [1150,750,1150,50],
    [1150,50,50,50]]
lines=[
    shapes.Line(50,50,50,750,width=1,color=(255,0,0),batch=batch),
    shapes.Line(50,750,1150,750,width=1,color=(255,0,0),batch=batch),
    shapes.Line(1150,750,1150,50,width=1,color=(255,0,0),batch=batch),
    shapes.Line(1150,50,50,50,width=1,color=(255,0,0),batch=batch)
]

#simulation variables
speed=250
rot_speed=100
is_rotating=False
rot_angle=15
rot_prev=-1
rot_current=0
rectangle.rotation=rot_angle
rad_angle=sympy.rad(rectangle.rotation)
#for performance need to limit decimal float to 2 numbers --- IMPORTANT
xdir=round(speed*sympy.cos(-rad_angle),2)
ydir=round(speed*sympy.sin(-rad_angle),2)

print(xdir,ydir)

def MainLoop(dt):
    #direction flow
    global rot_prev, rot_current,is_rotating,rot_speed,rot_angle,xdir,ydir
    #DT=time.perf_counter()
    #the object will move while it isn't rotating
    if is_rotating==False:
        rectangle.x+=xdir*round(dt,2)
        rectangle.y+=ydir*round(dt,2)
        #probably still need a timer, just for simulation case
        if rectangle.x<=points_list[0][0] or rectangle.x>=points_list[2][0] or rectangle.y<=points_list[0][1] or rectangle.y>=points_list[1][1]:
            is_rotating=True
    if is_rotating:
        rectangle.rotation+=rot_speed*dt
        rot_angle+=rot_speed*dt
        #with this condition, there'll be just one time calculation of direction
        if rot_angle>=170:
            rad_angle=sympy.rad(rectangle.rotation)
            xdir=round(speed*sympy.cos(-rad_angle),2)
            ydir=round(speed*sympy.sin(-rad_angle),2)
            rot_angle=0
            is_rotating=False
    print(xdir)


clock.schedule_interval(MainLoop,1/60.0)

@window.event
def on_draw():
    window.clear()
    #drawing the batch included graphics (ex:the rectangle)
    batch.draw()

pyglet.app.run()

