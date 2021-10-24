import math
import sympy
import pyglet
from pyglet import shapes
from pyglet import clock
import random
from pyglet import gl

#init the window
window=pyglet.window.Window(1200,800)
window.set_location(350,150)

#stack every drawable in this variable
batch=pyglet.graphics.Batch()

#init the rectangle
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
lines=[
    shapes.Line(rectangle.x,rectangle.y,points_list[0][0],points_list[0][1],width=1,color=(0,255,0),batch=batch),
    shapes.Line(rectangle.x,rectangle.y,points_list[1][0],points_list[1][1],width=1,color=(0,255,0),batch=batch),
    shapes.Line(rectangle.x,rectangle.y,points_list[2][0],points_list[2][1],width=1,color=(0,255,0),batch=batch),
    shapes.Line(rectangle.x,rectangle.y,points_list[3][0],points_list[3][1],width=1,color=(0,255,0),batch=batch)
    ]

#simulation variables
speed=2.5
change_direction=False
angle=90

def MainLoop(dt):
    #distance between points and object
    global change_direction
    dx=[rectangle.x-points_list[0][0],points_list[2][0]-rectangle.x]
    dy=[rectangle.y-points_list[0][1],points_list[1][1]-rectangle.y]

    #angles list
    angles=[
        (math.atan2(dx[0],dy[0])*180)/math.pi,
        (math.atan2(dx[0],dy[1])*180)/math.pi,
        (math.atan2(dx[1],dy[1])*180)/math.pi,
        (math.atan2(dx[1],dy[0])*180)/math.pi
    ]

    #updatin the lines
    for i in range(0,len(lines)):
        lines[i].x=rectangle.x
        lines[i].y=rectangle.y

    #direction flow
    if change_direction==False:
        new_angle=math.radians(angle)
        print(math.cos(new_angle))

clock.schedule_interval(MainLoop,0.0005)

@window.event
def on_draw():
    window.clear()
    #drawing the polygon
    polygon.draw()
    #drawing the batch included graphics (ex:the rectangle)
    batch.draw()

pyglet.app.run()

