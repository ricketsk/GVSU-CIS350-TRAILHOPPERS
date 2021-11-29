import gmaps
import geocoder

g = geocoder.ip('me')
latitiude = g.lat
longitude = g.lng
coords = (latitiude, longitude)

gmaps.configure(api_key="AIzaSyBdwkw6tlqH340Br0Hz1h1AieGkQg98f3I")
gmaps.figure(display_toolbar=True, center=coords, zoom_level=12, map_type='ROADMAP')
