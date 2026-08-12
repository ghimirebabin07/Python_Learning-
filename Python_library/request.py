import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response)
print(response.status_code)
print(response.text) 

#Get JSON data 
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)

data = response.json()

print(data)
print(data["title"])

#query params 
params = {
    "userId": 1
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

print(response.url)
print(response.json())

