from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.theming import ThemeManager
import Database
#from map import MapMainApp

class WelcomeWindow(Screen):
    pass 

class MainWindow(Screen):
    #self.theme_cls.theme_style = "Dark"
    #self.theme_cls.primary_palette = "Green"
    pass
class WindowManager(ScreenManager):
    pass




class MyApp(MDApp):
    def build(self):
        theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        Builder.load_file("My.kv")
        
        
        
        


if __name__ == "__main__":
    MyApp().run()