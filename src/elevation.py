import geocoder
import json
import urllib

g = geocoder.ip('me')
latitiude = g.lat
longitude = g.lng

def elevation(lat, lng):
    lat = latitiude
    lng = longitude
    apikey = "AIzaSyBdwkw6tlqH340Br0Hz1h1AieGkQg98f3I"
    url = "https://maps.googleapis.com/maps/api/elevation/json"
    request = urllib.urlopen(url+"?locations="+str(lat)+","+str(lng)+"&key="+apikey)
    try:
        results = json.load(request).get('results')
        if 0 < len(results):
            elevation = results[0].get('elevation')
            # ELEVATION
            print(elevation)
        else:
            print("HTTP GET Request failed.")
    except ValueError as e:
        print('JSON decode failed: '+str(request))
