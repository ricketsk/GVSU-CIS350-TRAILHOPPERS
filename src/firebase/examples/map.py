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
destinationLatitude = ""
destinationLongitude = ""
labels = []


class map:
######### create fxn ##################
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
        labels.append(y[i]['name'])

        gmaps = googlemaps.Client(key=api_key)

    def printLabels():
        print(labels)
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

class MapMainApp(App):

    def build(self):

        boxLayout = BoxLayout()
        mapView = MapView(lat=latitiude,lon=longitude, zoom=11)
        mapView.double_tap_zoom = True
        mapView.map_source = "osm"
        map_marker = MapMarker()
        map_marker.lat = latitiude
        map_marker.lon = longitude
        map_marker2 = MapMarker()
        map_marker2.lat = destinationLatitude
        map_marker2.lon = destinationLongitude
        map_marker.source = "map-marker.png"
        map_marker2.source = "map-marker2.png"
        mapView.add_widget(map_marker)
        mapView.add_widget(map_marker2)
        boxLayout.add_widget(mapView)
        return boxLayout
        
if __name__ == '__main__':
    MapMainApp().run()
