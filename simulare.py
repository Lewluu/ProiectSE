import pyglet
from pyglet import shapes
from pyglet.window import key

window=pyglet.window.Window(1200,800)
batch=pyglet.graphics.Batch()
keys=key.KeyStateHandler()
window.push_handlers(keys)

rectangle=shapes.Rectangle(80,80,150,150,color=(125,0,75),batch=batch)

@window.event
def on_key_press(symbol,modifies):
    ikey=chr(symbol)
    if ikey=='a':
        rectangle.x-=5

@window.event
def on_draw():
    print("Drawing!!!")
    window.clear()
    batch.draw()

pyglet.app.run()

