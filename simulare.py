import kivy
from kivy import animation
from kivy.app import App
from kivy.core import window
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.uix.button import Button

class Sim(Widget):
    pass

class SimApp(App):
    def build(self):
        return Sim()

if __name__=="__main__":
    SimApp().run()

