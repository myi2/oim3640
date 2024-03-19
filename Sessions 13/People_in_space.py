import urllib.request
import json
import pprint

url = "http://api.open-notify.org/astros.json"

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    # print(response_text)
    # print(type(response_text))
    data = json.loads(response_text)
    # print(data)
    # print(type(data))
    pprint.pprint(data)

# Can you print number of people in the space?


# Can you print all the names?

# {'craft': 'ISS', 'name': 'Jasmin Moghbeli'},
#             {'craft': 'ISS', 'name': 'Andreas Mogensen'},
#             {'craft': 'ISS', 'name': 'Satoshi Furukawa'},
#             {'craft': 'ISS', 'name': 'Konstantin Borisov'},
#             {'craft': 'ISS', 'name': 'Oleg Kononenko'},
#             {'craft': 'ISS', 'name': 'Nikolai Chub'},
#             {'craft': 'ISS', 'name': "Loral O'Hara"}]}