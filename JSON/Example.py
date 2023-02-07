# import json
#
# computer = [
#     {
#         'id': 1,
#         'name': 'HP',
#         'color': 'Grey',
#     },
#     {
#         'id': 2,
#         'name': 'MSI',
#         'color': 'black'
#     },
#     {
#         'id': 3,
#         'name': 'MSi',
#         'color': 'blue'
#     }
# ]
#
# with open('computer.json', 'w') as file:
#     json.dump(computer, file)

import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.freecurrencyapi.com/v1/latest?apikey=YOUR-APIKEY"

resp = requests.get(url)

print(resp.status_code)






