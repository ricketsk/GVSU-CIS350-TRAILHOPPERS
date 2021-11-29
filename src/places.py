import requests, json

api_key = "AIzaSyBdwkw6tlqH340Br0Hz1h1AieGkQg98f3I"

url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

s = "Trails near me"

query = s#input('Search query: ')

r = requests.get(url + 'query=' + query + '&key=' + api_key)

x = r.json()

y = x['results']

for i in range(len(y)):

	print(y[i]['name'])
