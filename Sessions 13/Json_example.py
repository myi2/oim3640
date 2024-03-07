import urllib.request
import json

APIKEY = '728e633101dc8d24a2d988b43caad2d0'
city = 'Wellesley'
country_code = 'us'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

# print(url)

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    
print(response_data)

# How do we get current temperature?
