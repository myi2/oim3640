from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)


# Function to query the Mapbox API and return the geocode data
def get_geocode(place_name, mapbox_token):
    MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
    query = place_name.replace(' ', '%20')
    url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={mapbox_token}'

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to extract latitude and longitude from the Mapbox API response
def extract_lat_lon(json_data):
    if json_data and 'features' in json_data and len(json_data['features']) > 0:
        coordinates = json_data['features'][0]['geometry']['coordinates']
        return coordinates[1], coordinates[0]  # Latitude, Longitude
    return None, None

# Function to query the MBTA API and return the nearest stop data
def get_nearest_mbta_stop(lat, lon, mbta_token):
    MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
    url = f"{MBTA_BASE_URL}?api_key={mbta_token}&filter[latitude]={lat}&filter[longitude]={lon}&sort=distance"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to extract the nearest MBTA stop name and its wheelchair accessibility from the MBTA API response
def extract_mbta_stop_info(json_data):
    if json_data and 'data' in json_data and len(json_data['data']) > 0:
        stop_name = json_data['data'][0]['attributes']['name']
        wheelchair_accessible = json_data['data'][0]['attributes']['wheelchair_boarding']
        return stop_name, wheelchair_accessible
    return None, None

# Main function to find the nearest MBTA stop to a given place name
def find_stop_near(place_name, mapbox_token, mbta_token):
    geocode_data = get_geocode(place_name, mapbox_token)
    lat, lon = extract_lat_lon(geocode_data)
    if lat and lon:
        mbta_data = get_nearest_mbta_stop(lat, lon, mbta_token)
        stop_name, wheelchair_accessible = extract_mbta_stop_info(mbta_data)
        return stop_name, wheelchair_accessible
    return None, None

def query_yelp(lat, lon):
    YELP_API_KEY = 'k9P3_B7QwqUatTcCGLYWyxjHY8gBy0OKDzEHpGa2pAnZcgeBWACtJSdiFm6sL4RjBgOPseZfyfbHhXnZlDWZfJHl1Ef5O6iwGLMNYwo4Xra1TyaZzOgf3mkz9asRZnYx'  
    headers = {'Authorization': f'Bearer {YELP_API_KEY}'}
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'latitude': lat, 'longitude': lon, 'radius': 400, 'limit': 5}

    response = requests.get(url, headers=headers, params=params)
    return response.json()  # This is the raw response from Yelp

def print_businesses(lat, lon):
    results = query_yelp(lat, lon)
    for business in results.get('businesses', []):
        print(f"Name: {business['name']}, Rating: {business['rating']}, Reviews: {business['review_count']}")


# Example usage
MAPBOX_API_ACCESS_TOKEN = 'sk.eyJ1Ijoia2xrMTMyIiwiYSI6ImNsdW9mcTVkNDIybHkya256YWV5bHp6NmkifQ.p-L0xVfztjn5fuJcQuJesQ'
MBTA_API_ACCESS_TOKEN = '918662e2f37b4a01964e4b78d57b44e9'
place_name = "Boston Common"
stop_name, wheelchair_accessible = find_stop_near(place_name, MAPBOX_API_ACCESS_TOKEN, MBTA_API_ACCESS_TOKEN)

if stop_name:
    print(f"Nearest MBTA Stop: {stop_name}, Wheelchair Accessible: {wheelchair_accessible}")
else:
    print("No MBTA stop found nearby.")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        # Include the required API tokens when calling find_stop_near
        stop_name, wheelchair_accessible = find_stop_near(location, MAPBOX_API_ACCESS_TOKEN, MBTA_API_ACCESS_TOKEN)
        return render_template('result.html', stop_name=stop_name, wheelchair_accessible=wheelchair_accessible)
    return render_template('index.html')

# Ensure the server runs only if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)


