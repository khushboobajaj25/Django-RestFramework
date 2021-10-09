import json
import requests


URL = "http://localhost:8000/create/"

# r = requests.get(url=URL)

data = {
    'name': 'Ayush',
    'roll': 3,
    'city': "UNR"
}
json_data = json.dumps(data)
# converting json into python
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)
