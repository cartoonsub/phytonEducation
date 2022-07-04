from re import template
import requests

key = '11c0d3dc6093f7442898ee49d2430d20'

url = 'https://api.openweathermap.org/data/2.5/weather?'
query = {'q' : 'Saint Petersburg', 'appid' : key}

result = requests.get(url, params=query).json()
lon = result['coord']['lon']
lat = result['coord']['lat']

query = {'lon' : lon, 'lat' : lat, 'appid' : key, 'units' : 'metric'}
result = requests.get(url, params=query).json()
print(result)

template = 'Погода в Санкт-Петербурге: {} C., влажность {}%'
print(template.format(result['main']['temp'], result['main']['humidity']))