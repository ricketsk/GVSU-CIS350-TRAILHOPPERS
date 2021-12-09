from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView, MapSource, MapMarker
import geocoder
from kivy_garden.mapview.view import MapMarker
import requests, json
import googlemaps
import time
from datetime import datetime
from geopy.location import Location
from geopy.geocoders import Nominatim

api_key = "AIzaSyBdwkw6tlqH340Br0Hz1h1AieGkQg98f3I"

# takes the current location of the user
g = geocoder.ip('')
# sets latitude and longitude to the current locations lat and long

latitiude = g.lat
longitude = g.lng
list = []


url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

s = 'Trails near me'

# The text string on which to search
query = s

# get method of requests module
# return response object
r = requests.get(url + 'query=' + query + '&key=' + api_key)

# json method of response object convert
# json format data into python format data
x = r.json()

# now x contains list of nested dictionaries
# we know dictionary contain key value pair
# store the value of result key in variable y
y = x['results']

# keep looping upto length of y
for i in range(len(y)):

    # Print value corresponding to the
    # 'name' key at the ith index of y
    list.append(y[i]['name'])

    gmaps = googlemaps.Client(key=api_key)

print(list)
"""
######### make it text input box ##############
input = input("Which trail would you like to go to? ")
print("Going to: " + input)

############# new fxn ########################
app = Nominatim(user_agent="tutorial")
location = app.geocode(input).raw

address = input

def getLocationByAddress(address):
    app = Nominatim(user_agent="tutorial2")
    time.sleep(1)
    try:
        return app.geocode(address).raw
    except:
        return getLocationByAddress(address)

location = getLocationByAddress(address)
destinationLatitude = location["lat"]
destinationLongitude = location["lon"]

now = datetime.now()
directions_result = gmaps.directions((latitiude,longitude), (destinationLatitude,destinationLongitude), mode="driving",departure_time=now)
print(directions_result[0]['legs'][0]['distance']['text'])
print(directions_result[0]['legs'][0]['duration']['text'])

"""
class MainApp(MDApp):
    lat = latitiude
    lon = longitude

    user_idToken = ""
    local_id = ""

    def display_user_tokens(self):
        self.root.ids.the_label.text = "local_id: " + self.local_id + "\n user_idToken: " + self.user_idToken

    def sign_out(self):
        self.root.ids.firebase_login_screen.log_out()
        self.root.current = 'firebase_login_screen'


MainApp().run()

