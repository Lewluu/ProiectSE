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
sensor=shapes.Rectangle(100,100,50,50,color=(155,0,155),batch=batch)
sensor.anchor_position=(25,-25)

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
change_direction=False
rot_angle=0
DT=0
ctm=0
rectangle.rotation=rot_angle
rad_angle=sympy.rad(rectangle.rotation)
xdir=speed*sympy.cos(rad_angle)
ydir=speed*sympy.sin(rad_angle)

def MainLoop(dt):
    #distance between points and object
    global change_direction
    # dx=[rectangle.x-points_list[0][0],points_list[2][0]-rectangle.x]
    # dy=[rectangle.y-points_list[0][1],points_list[1][1]-rectangle.y]

    #angles list
    # point_angles=[
    #     (math.atan2(dx[0],dy[0])*180)/math.pi,
    #     (math.atan2(dx[0],dy[1])*180)/math.pi,
    #     (math.atan2(dx[1],dy[1])*180)/math.pi,
    #     (math.atan2(dx[1],dy[0])*180)/math.pi
    # ]

    #direction flow
    global rot_angle,rad_angle,speed,DT,ctm,xdir,ydir
    DT=time.perf_counter()-ctm                          #it'll start just after changing direction
    if change_direction==False:
        #updating current time
        ctm=time.perf_counter()
        #check if object is in the polygon
        #update position
        rectangle.x+=xdir*dt
        rectangle.y+=ydir*dt
        #new method to check if the object is out of bounds
        if rectangle.x<=points_list[0][0] or rectangle.x>=points_list[2][0] or rectangle.y<=points_list[0][1] or rectangle.y>=points_list[1][1]:
            change_direction=True
        # for ang in point_angles:
        #      if ang<0 or ang>90:
        #          change_direction=True
    #memory leak here
    if change_direction==True:
        if rot_angle<170:
            rectangle.rotation+=rot_speed*dt
            rot_angle+=rot_speed*dt
            rad_angle=sympy.rad(rectangle.rotation)
        elif DT<2:                                                      #trying to syncronize rotation speed with direction change
            xdir=speed*sympy.cos(-rad_angle)
            ydir=speed*sympy.sin(-rad_angle)
            rectangle.x+=xdir*dt
            rectangle.y+=ydir*dt
        else:
            rot_angle=0
            change_direction=False

clock.schedule_interval(MainLoop,1/60.0)

@window.event
def on_draw():
    window.clear()
    #drawing the polygon
    polygon.draw()
    #drawing the batch included graphics (ex:the rectangle)
    batch.draw()

pyglet.app.run()

