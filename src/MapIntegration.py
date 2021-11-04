from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView, MapSource

class MapMainApp(App):
    
    def build(self):
        box_layout = BoxLayout()
        map_view = MapView(lat=42.9641, lon=-85.8890, zoom=13)
        map_view.map_source = "osm"
        box_layout.add_widget(map_view)
        return box_layout

if __name__ == '__main__':
    MapMainApp().run()




