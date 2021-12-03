from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.theming import ThemeManager
import Database_Trailhoppers as data

class WelcomeWindow(Screen):
    pass 

class LoginWindow(Screen):
    userName = ObjectProperty(None)
    passW = ObjectProperty(None)
    def button(self):
        print("Username:", self.userName.text,
        "Password:", self.passW.text)
        self.userName.text = ""
        self.passW.text = ""
    pass

class StartWindow(Screen):
    firstName = ObjectProperty(None)
    lastName = ObjectProperty(None)
    user_Name = ObjectProperty(None)
    email = ObjectProperty(None)
    passWord = ObjectProperty(None)

    def button(self):
        print("First Name:", self.firstName.text, 
        "Last Name:", self.lastName.text, 
        "Username:", self.user_Name.text,
        "Email:", self.email.text, 
        "Password:", self.passWord.text)
        self.firstName.text = ""
        self.lastName.text = ""
        self.user_Name.text = ""
        self.email.text = ""
        self.passWord.text = ""
    
    #data.DatabaseMainApp().submit_user(firstName, lastName, user_Name, email, passWord)
    data.DatabaseMainApp().submit_user("John", "Ham", "JohnHam", "johnham@gamil.com", "password2")
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
        self.theme_cls.theme_style = "Dark"
        Builder.load_file("My.kv")
        data.DatabaseMainApp().build_db()
        
        
        


if __name__ == "__main__":
    MyApp().run()