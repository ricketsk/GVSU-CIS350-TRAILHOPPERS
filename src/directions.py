import googlemaps
from datetime import datetime
import geocoder

api_key = "AIzaSyBdwkw6tlqH340Br0Hz1h1AieGkQg98f3I"

g = geocoder.ip('me')
latitiude = g.lat
longitude = g.lng

gmaps = googlemaps.Client(key=api_key)

print("Where would you like to go?")
input = input()

now = datetime.now()
directions_result = gmaps.directions((latitiude,longitude), input, mode="driving",departure_time=now)
print(directions_result[0]['legs'][0]['distance']['text'])
print(directions_result[0]['legs'][0]['duration']['text'])

