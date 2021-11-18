import geocoder

g = geocoder.ip('me')
#latitiude = g.lat
#longitude = g.lng
print(g.latlng)