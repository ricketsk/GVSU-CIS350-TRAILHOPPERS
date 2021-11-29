from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView, MapSource, MapMarker
import geocoder
from kivy_garden.mapview.view import MapMarker
import requests, json
import googlemaps
from datetime import datetime

api_key = "AIzaSyBdwkw6tlqH340Br0Hz1h1AieGkQg98f3I"

# takes the current location of the user
g = geocoder.ip('')
# sets latitude and longitude to the current locations lat and long
latitiude = g.lat
longitude = g.lng

# url variable store url
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
	print(y[i]['name'])

gmaps = googlemaps.Client(key=api_key)

input = input("Which trail would you like to go to? ")
print("Going to: " + input)



now = datetime.now()
directions_result = gmaps.directions((latitiude,longitude), input, mode="driving",departure_time=now)
print(directions_result[0]['legs'][0]['distance']['text'])
print(directions_result[0]['legs'][0]['duration']['text'])


class MapMainApp(App):

    def build(self):

        boxLayout = BoxLayout()
        mapView = MapView(lat=latitiude,lon=longitude, zoom=16)
        mapView.map_source = "osm"
        map_marker = MapMarker()
        map_marker.lat = latitiude
        map_marker.lon = longitude
        map_marker.source = "mapmarker.jpeg"
        mapView.add_widget(map_marker)
        boxLayout.add_widget(mapView)
        return boxLayout
        
if __name__ == '__main__':
    MapMainApp().run()
