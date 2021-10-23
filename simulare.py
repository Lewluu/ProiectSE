import pyglet
from pyglet import shapes
from pyglet import clock

window=pyglet.window.Window(1200,800)
window.set_location(350,150)
batch=pyglet.graphics.Batch()

rectangle=shapes.Rectangle(280,280,100,100,color=(125,0,75),batch=batch)
rectangle.anchor_position=(25,25)

speed=5
mvright=mvleft=mvup=mvdown=False

@window.event
def on_key_press(symbol,modifies):
    global mvright, mvleft,mvup,mvdown
    ikey=chr(symbol)
    if ikey=='a':
        mvleft=True
    if ikey=='d':
        mvright=True
    if ikey=='w':
        mvup=True
    if ikey=='s':
        mvdown=True

@window.event
def on_key_release(symbol,modifies):
    global mvright, mvleft,mvup,mvdown
    ikey=chr(symbol)
    if ikey=='a' and mvleft==True:
        mvleft=False
    if ikey=='d' and mvright==True:
        mvright=False
    if ikey=='w' and mvup==True:
        mvup=False
    if ikey=='s' and mvdown==True:
        mvdown=False


def MainLoop(dt):
    if mvright:
        rectangle.x+=speed
    if mvleft:
        rectangle.x-=speed
    if mvup:
        rectangle.y+=speed
    if mvdown:
        rectangle.y-=speed


clock.schedule_interval(MainLoop,0.0005)


@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()

