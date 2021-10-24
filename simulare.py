import pyglet
from pyglet import shapes
from pyglet import clock
import random

from pyglet import gl

window=pyglet.window.Window(1200,800)
window.set_location(350,150)
batch=pyglet.graphics.Batch()

rectangle=shapes.Rectangle(125,125,100,100,color=(125,0,75),batch=batch)
rectangle.anchor_position=(50,50)

speed=2.5

def MainLoop(dt):
    if rectangle.y < 750:
        rectangle.y+=speed


clock.schedule_interval(MainLoop,0.0005)

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


@window.event
def on_draw():
    window.clear()
    #drawing the batch included graphics (ex:the rectangle)
    batch.draw()
    #drawing the polygon
    polygon.draw()

pyglet.app.run()

