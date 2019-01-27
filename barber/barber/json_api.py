import urllib.parse
import requests

main_api = 'https://maps.googleapis.com/maps/api/gocode/json?'
address = 'lhr'
url = main_api + urllib.parse.urlencode({'address': address})

json_data = requests.get(url).json()

print(json_data)