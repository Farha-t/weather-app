import requests

api_key = "b884d9ad90dd0b952a66443f8e4fe092"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

data = response.json()

if data["cod"] == 200:

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    weather = data["weather"][0]["description"]

    print("=" * 30)
    print(f" weather in {city.upper()}")
    print("=" * 30)
    print(f" Temperature : {temperature} °C")
    print(f" Feels Like  : {feels_like} °C") 
    print(f" Humidity    : {humidity}%")
    print(f" Wind Speed  : {wind_speed} m/s")
    print(f" Condition   : {weather.capitalize()}")
    print("=" * 30)

else:
    print("City not found! Please check the city name.")