from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView, MapSource

class MapMainApp(App):

    googleApiKey = "AIzaSyBdwkw6tlqH340Br0Hz1h1AieGkQg98f3I"

    def build(self):

        boxLayout = BoxLayout()
        mapView = MapView(lat=42.9903205, lon=-85.95296849268018, zoom=13)
        mapView.map_source = "osm"
        boxLayout.add_widget(mapView)
        return boxLayout
        
if __name__ == '__main__':
    MapMainApp().run()
