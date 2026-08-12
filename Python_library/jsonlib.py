import json

data = {
    "name": "Babin",
    "age": 20,
    "course": "BEIT"
}

json_data = json.dumps(data)

print(json_data) 