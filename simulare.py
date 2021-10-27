import math
import time
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

polygon=pyglet.graphics.Batch()

for points in points_list:
    polygon.add(2,pyglet.gl.GL_LINES,None,
                ('v2i',points),
                ('c3B',(255,0,0,255,0,0)))

#lines, help only for visuals
# lines=[
#     shapes.Line(rectangle.x,rectangle.y,points_list[0][0],points_list[0][1],width=1,color=(0,255,0),batch=batch),
#     shapes.Line(rectangle.x,rectangle.y,points_list[1][0],points_list[1][1],width=1,color=(0,255,0),batch=batch),
#     shapes.Line(rectangle.x,rectangle.y,points_list[2][0],points_list[2][1],width=1,color=(0,255,0),batch=batch),
#     shapes.Line(rectangle.x,rectangle.y,points_list[3][0],points_list[3][1],width=1,color=(0,255,0),batch=batch)
#     ]

#simulation variables
speed=250
rot_speed=100
is_rotating=False
rot_angle=0
rot_prev=-1
rot_current=0
rectangle.rotation=rot_angle
rad_angle=sympy.rad(rectangle.rotation)
xdir=speed*sympy.cos(rad_angle)
ydir=speed*sympy.sin(rad_angle)

def MainLoop(dt):
    #direction flow
    global rot_prev, rot_current,is_rotating,rot_speed,rot_angle,xdir,ydir
    if is_rotating==False:
        rectangle.x+=xdir*dt
        rectangle.y+=ydir*dt
    if rot_current!=rot_prev:
        if rectangle.x<=points_list[0][0] or rectangle.x>=points_list[2][0] or rectangle.y<=points_list[0][1] or rectangle.y>=points_list[1][1]:
            is_rotating=True
            rot_prev=rot_current
            print("Yes")
    if is_rotating:
        rectangle.rotation+=rot_speed*dt
        rot_angle+=rot_speed*dt
        if rot_angle>=170:
            rad_angle=sympy.rad(rectangle.rotation)
            xdir=speed*sympy.cos(-rad_angle)
            ydir=speed*sympy.sin(-rad_angle)
            rot_current+=1
            rot_angle=0
            is_rotating=False


clock.schedule_interval(MainLoop,1/60.0)

@window.event
def on_draw():
    window.clear()
    #drawing the polygon
    polygon.draw()
    #drawing the batch included graphics (ex:the rectangle)
    batch.draw()

pyglet.app.run()

