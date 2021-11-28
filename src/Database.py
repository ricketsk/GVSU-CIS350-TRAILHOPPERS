from kivy.app import App
from kivy.lang.builder import Builder
import sqlite3

class DatabaseMainApp(App):
    def build(self):

        #Define connection and cursor
        connection = sqlite3.conncet('TrailHoppers_db.db')

        c = connection.cursor()

        c.execute("""CREATE TABLE if not exist users(
                Username text NOT NULL,
                Password text NOT NULL,
                User_ID integer PRIMARY KEY,
                First_name text,
                Last_name text,
                Email text,
                Phone_num text
                )
        """)

        c.execute("""CREATE TABLE if not exist trails(
                Difficulty integer
                User_rating integer
                trail_length real
                Elevation interger
                Trail_type text
        )""")

        c.execute("""CREATE TABLE if not exist social(
                Completed_trials 

        )""")

        #commit changes
        connection.commit()

        #close connection
        connection.close()

        return Builder.load_file('Trailhoppers_db.kv')


    def submit(self):
        
        #Define connection and cursor
        connection = sqlite3.connct('Users_db.db')

        c = connection.cursor()

        #Add a record
        c.execute("INSERT INTO users VALUES (:first)",
        {
            'first': self.root.ids.word_input.text,
        })

        #adds message 
        self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Added'

        #clear input box
        self.root.ids.word_input.text = ''


        #commit changes
        connection.commit()

        #close connection
        connection.close()



if __name__ == '__main__':
    DatabaseMainApp().run()