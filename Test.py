#Client Side

import requests
URL="http://127.0.0.1:5000/"
response = requests.get(URL)
message = response.json()
print(message["02/06/22"])