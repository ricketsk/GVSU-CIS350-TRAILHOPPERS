from logging import Manager
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class StartWindow(Screen):
    firstName = ObjectProperty(None)
    lastName = ObjectProperty(None)
    email = ObjectProperty(None)
    passWord = ObjectProperty(None)

    def button(self):
        print("First Name:", self.firstName.text, 
        "Last Name:", self.lastName.text, 
        "Email:", self.email.text, 
        "Password:", self.passWord.text)
        self.firstName.text = ""
        self.lastName.text = ""
        self.email.text = ""
        self.passWord.text = ""
    pass

class MainWindow(Screen):
    #self.theme_cls.theme_style = "Dark"
    #self.theme_cls.primary_palette = "Green"
    pass

class WindowManager(ScreenManager):
    pass




class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        Builder.load_file("My.kv")
        
        
        
        


if __name__ == "__main__":
    MyApp().run()