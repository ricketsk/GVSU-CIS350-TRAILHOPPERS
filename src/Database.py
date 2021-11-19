from kivy.app import App
from kivy.lang.builder import Builder
import sqlite3

class DatabaseMainApp(App):
    def build(self):

        #Define connection and cursor
        connection = sqlite3.connect('TrailHoppers_db.db')
    

        c = connection.cursor()
        print("connected to SQLite")

        c.execute("""CREATE TABLE if not exists users(
                User_ID integer PRIMARY KEY,
                Username text NOT NULL UNIQUE,
                Password text NOT NULL UNIQUE,
                First_name text NOT NULL,
                Last_name text NOT NULL,
                Email text UNIQUE,
                Phone_num text UNIQUE
                )
        """)

        c.execute("""CREATE TABLE if not exists trails(
                Trail text NOT NULL,
                Difficulty integer,
                User_rating integer,
                trail_length real,
                Elevation interger,
                Trail_type text
        )""")

        c.execute("""CREATE TABLE if not exists social(
                Completed_trials NULL,
                Liked_trails NULL,
                trial_times REAL

        )""")

        #commit changes
        connection.commit()

        #close connection
        connection.close()

        return Builder.load_file('My.kv')


    def First_submit(self):
        
        #Define connection and cursor
        connection = sqlite3.connct('Users_db.db')

        c = connection.cursor()

        #Add a record
        c.execute("INSERT INTO users VALUES (First_name)",
        {
            'first': self.root.ids.firstName.text,
        })

        #adds message 
        self.root.ids.firstName.text = f'{self.root.ids.firstName.text} Added'

        #clear input box
        self.root.ids.firstName.text = ''


        #commit changes
        connection.commit()

        #close connection
        connection.close()


