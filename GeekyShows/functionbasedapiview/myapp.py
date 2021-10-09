import requests
import json
URL = "http://localhost:8000/stu/"


def get_data(id=None):
    data = {"id": id}
    if id is not None:
        data = {"id": id}
    json_data = json.dumps(data)
    headers={"content-Type":"application/json"}
    r = requests.get(url=URL,headers=headers,  data=json_data)
    data = r.json()
    print(data)


# get_data()

def post_data():
    data = {
        "name": "Ayush",
        "roll": "34",
        "city": "unr"

    }
    headers={"content-Type":"application/json"}
    json_data = json.dumps(data)
    r = requests.post(url = URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

# post_data()

def update_data():
    data = {
        "id":1,
        "name": "Khushboo Bajaj",
        "roll": "34",
        "city": "unrs"

    }
   
    json_data = json.dumps(data)
    headers={"content-Type":"application/json"}
    r = requests.put(url = URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data():
    data={"id":1}
    headers={"content-Type":"application/json"}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, headers=headers, data=json_data)
    data = r.json()

delete_data()
