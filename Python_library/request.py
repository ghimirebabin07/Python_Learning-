import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 27.7,
    "longitude": 85.3,
    "current_weather": True
}

response = requests.get(url, params=params)

data = response.json()  

weather = data["current_weather"]  

print(f"Temperature : {weather['temperature']}°C")
print(f"Wind Speed  : {weather['windspeed']} km/h")
print(f"Weather Code: {weather['weathercode']}")