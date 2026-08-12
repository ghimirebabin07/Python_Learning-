import json

data = {
    "name": "Babin",
    "age": 20,
    "course": "BEIT"
}

json_data = json.dumps(data)

print(json_data) 

#json.loads() 
son_data = '{"name": "Babin", "age": 20}'

data = json.loads(json_data)

print(data)
print(data["name"]) 