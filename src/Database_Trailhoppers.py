from kivy.app import App
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
import sqlite3



class DatabaseMainApp(App):
    lastName = ObjectProperty(None)
    firstName = ObjectProperty(None)
    user_Name = ObjectProperty(None)
    email = ObjectProperty(None)
    passWord = ObjectProperty(None)
    

    def build_db(self):

        #Define connection and cursor
        connection = sqlite3.connect('TrailHoppers.db')
    

        c = connection.cursor()
        print("connected to SQLite")

        c.execute("""CREATE TABLE users(
                User_id INTEGER,
                First_name TEXT,
                Last_name TEXT,
                Username TEXT,
                Email TEXT,
                Password TEXT)
         """)

        c.execute("""CREATE TABLE if not exists trails(
                Trail TEXT,
                Difficulty INTEGER,
                User_rating INTEGER,
                trail_length REAL,
                Elevation INTEGER,
                Trail_type TEXT)
         """)

        c.execute("""CREATE TABLE if not exists social(
                Completed_trials NULL,
                Liked_trails NULL,
                trial_times REAL)
         """)

        #commit changes
        connection.commit()

        #close connection
        connection.close()


    def submit_user(self, firstName, lastName, user_Name, email,passWord):
        firstName = self.firstName
        lastName = self.lastName
        user_Name = self.user_Name
        email = self.email
        passWord = self.passWord

        #Define connection and cursor
        connection = sqlite3.connect('TrailHoppers.db')

        c = connection.cursor()

        #Add a records to user tabel
        c.execute("""INSERT INTO users(First_name, Last_name, Username, Email, Password) VALUES (:firstName, :lastName, :userName, :email, :passWord)""",
        {
            'firstName': firstName,
            'lastName': lastName,
            'userName': user_Name,
            'email': email,
            'passWord': passWord
        })

        #commit changes
        connection.commit()

        #close connection
        connection.close()