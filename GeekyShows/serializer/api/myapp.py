import json
import requests
URL = "http://localhost:8000/stulist/"

r = requests.get(url=URL)

data = r.json()

print(data)
