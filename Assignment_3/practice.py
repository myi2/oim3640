import requests

def query_yelp(lat, lon):
    headers = {'Authorization': f'Bearer {YELP_API_KEYapi_key}'}
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'latitude': lat, 'longitude': lon, 'radius': 400, 'limit': 5}

    response = requests.get(url, headers=headers, params=params)
    return response.json()  # This is the raw response from Yelp



# For debugging: Print names of businesses found
for business in results.get('businesses', []):
    print(f"Name: {business['name']}, Rating: {business['rating']}, Reviews: {business['review_count']}")
