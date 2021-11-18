from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView, MapSource
import geocoder

g = geocoder.ip('me')
latitiude = g.lat
longitude = g.lng
#print(g.latlng)

class MapMainApp(App):

    googleApiKey = "AIzaSyBdwkw6tlqH340Br0Hz1h1AieGkQg98f3I"

    def build(self):

        boxLayout = BoxLayout()
        mapView = MapView(lat=latitiude,lon=longitude, zoom=16)
        mapView.map_source = "osm"
        boxLayout.add_widget(mapView)
        return boxLayout
        
if __name__ == '__main__':
    MapMainApp().run()
