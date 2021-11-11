from geopy.location import Location
from geopy.geocoders import Nominatim
import time
from pprint import pprint    
    
googleApiKey = "AIzaSyBdwkw6tlqH340Br0Hz1h1AieGkQg98f3I"

userInput = input("Enter your location: ")

app = Nominatim(user_agent="tutorial")
location = app.geocode(userInput).raw
pprint(location)

address = userInput

def getLocationByAddress(address):
    app = Nominatim(user_agent="tutorial2")
    time.sleep(1)
    try:
        return app.geocode(address).raw
    except:
        return getLocationByAddress(address)

location = getLocationByAddress(address)
latitude = location["lat"]
longitude = location["lon"]
print(f"{latitude}, {longitude}")
pprint(location)