from kivy.app import App
from kivy.lang.builder import Builder
import sqlite3

class DatabaseMainApp(App):
    def build(self):

        #Define connection and cursor
        connection = sqlite3.connect('TrailHoppers.db')
    

        c = connection.cursor()
        print("connected to SQLite")

        c.execute("""CREATE TABLE if not exists users(
                Username text NOT NULL UNIQUE,
                Password text NOT NULL UNIQUE,
                First_name text NOT NULL,
                Last_name text NOT NULL,
                Email text UNIQUE)
         """)

        c.execute("""CREATE TABLE if not exists trails(
                Trail text NOT NULL,
                Difficulty integer,
                User_rating integer,
                trail_length real,
                Elevation interger,
                Trail_type text)
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

        return Builder.load_file('My.kv')


    def Submit(self):
        
        #Define connection and cursor
        connection = sqlite3.connct('TrailHoppers.db')

        c = connection.cursor()

        #Add a record to first_name
        c.execute("INSERT INTO users VALUES (:First_name)",
        {
            'First_name': self.root.ids.firstName.text,
        })

        #Add a record to last_name
        c.execute("INSERT INTO users VALUES (:Last_name)",
        {
            'Last_name': self.root.ids.lastName.text,
        })

         #Add a record to username
        c.execute("INSERT INTO users VALUES (:Username)",
        {
            'Username': self.root.ids.createUserName.text,
        })

        #Add a record to email
        c.execute("INSERT INTO users VALUES (:Email)",
        {
            'Email': self.root.ids.email.text,
        })

        #Add a record password
        c.execute("INSERT INTO users VALUES (:Password)",
        {
            'Password': self.root.ids.passWord.text,
        })

        #commit changes
        connection.commit()

        #close connection
        connection.close()