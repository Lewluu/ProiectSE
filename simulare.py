import kivy
from kivy import animation
from kivy.app import App
from kivy.core import window
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.graphics import Rectangle

class Sim(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
             self.rect=Rectangle(pos=(0,0),size=(100,100))

        anim=Animation(pos=(100,100))
        anim.start(Widget)


class SimApp(App):
    def build(self):
        return Sim()

if __name__=="__main__":
    SimApp().run()

