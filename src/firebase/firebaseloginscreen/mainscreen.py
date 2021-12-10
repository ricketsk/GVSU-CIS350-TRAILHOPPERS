from kivy.uix.screenmanager import Screen, SlideTransition

class Mainscreen(Screen):
    def entire(self):
        self.parent.transition = SlideTransition(direction="right")
        self.parent.current = self.parent.current = "main"
        self.parent.transition = SlideTransition(direction="left")

