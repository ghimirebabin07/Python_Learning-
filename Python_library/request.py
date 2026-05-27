import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 27.7,
    "longitude": 85.3,
    "current_weather": True,
    "hourly": "temperature_2m,relative_humidity_2m"
}
response = requests.get(url, params=params)

data = response.json()
temps = data["hourly"]["temperature_2m"]
humidity = data["hourly"]["relative_humidity_2m"]

print(temps)
print(humidity)

weather = data["current_weather"]

print(f"Temperature : {weather['temperature']}°C")
print(f"Wind Speed  : {weather['windspeed']} km/h")
print(f"Weather Code: {weather['weathercode']}")