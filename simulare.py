import pyglet
from pyglet import shapes
from pyglet import clock

window=pyglet.window.Window(1200,800)
batch=pyglet.graphics.Batch()

rectangle=shapes.Rectangle(80,80,150,150,color=(125,0,75),batch=batch)

@window.event
def on_key_press(symbol,modifies):
    ikey=chr(symbol)
    if ikey=='a':
        rectangle.x-=5
    if ikey=='d':
        rectangle.x+=5



@window.event
def on_key_press(symbol,modifies):
    MOVE_RIGHT=False
    ikey=chr(symbol)
    if ikey=='a':
        rectangle.x-=5
    if ikey=='d':
        MOVE_RIGHT=True

def callback(dt):
    if MOVE_RIGHT:
        rectangle.x+=5

clock.schedule_interval(callback,1)


@window.event
def on_draw():
    window.clear()
    callback("Call back !!!")
    batch.draw()

pyglet.app.run()

