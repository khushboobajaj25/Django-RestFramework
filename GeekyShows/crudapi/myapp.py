import requests
import json
URL = "http://localhost:8000/stu/"


def get_data(id=None):
    data = {"id": id}
    if id is not None:
        data = {"id": id}
    json_data = json.dumps(data)

    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data()

def post_data():
    data = {
        "name": "Ayush",
        "roll": "34",
        "city": "unr"

    }
    json_data = json.dumps(data)
    r = requests.post(url = URL,data=json_data)
    data = r.json()
    print(data)

post_data()

def update_data():
    data = {
        "id":3,
        "name": "Khushboo Bajaj",
        "roll": "34",
        "city": "unrs"

    }
    json_data = json.dumps(data)
    r = requests.put(url = URL,data=json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data():
    data={
        "id":2
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL,data=json_data)
    data = r.json()

# delete_data()
