from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy_garden.mapview import MapView, MapSource

googleApiKey = "AIzaSyBdwkw6tlqH340Br0Hz1h1AieGkQg98f3I"

class MapMainApp(App):

    def build(self):
        
        box_layout = BoxLayout()
        map_view = MapView(lat=42.9641, lon=-85.8890, zoom=13)
        map_view.map_source = "osm"
        box_layout.add_widget(map_view)
        return box_layout, Label(text="TrailHoppers")


    """def extract_lat_long_via_address(address_or_zipcode):
        lat, lng = None, None
        api_key = googleApiKey
        base_url = "https://maps.googleapis.com/maps/api/geocode/json"
        endpoint = f"{base_url}?address={address_or_zipcode}&key={api_key}"
        # see how our endpoint includes our API key? Yes this is yet another reason to restrict the key
        r = requests.get(endpoint)
        if r.status_code not in range(200, 299):
            return None, None
        try:
            '''
            This try block incase any of our inputs are invalid. This is done instead
            of actually writing out handlers for all kinds of responses.
            '''
            results = r.json()['results'][0]
            lat = results['geometry']['location']['lat']
            lng = results['geometry']['location']['lng']
        except:
            pass
        return lat, lng """

if __name__ == '__main__':
    MapMainApp().run()




