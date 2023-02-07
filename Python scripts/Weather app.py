import requests
import json

# API key for OpenWeatherMap
API_KEY = 'cd25921097e565c7a876bd98bd21a528'

# Function to get weather data for a specific location
def get_weather_data(location):
    # API endpoint
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}'
    # Making API call
    response = requests.get(url)
    # Parsing JSON data
    data = json.loads(response.text)
    return data

# Function to display weather data
def display_weather(location):
    data = get_weather_data(location)
    # Extracting necessary information
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    condition = data['weather'][0]['main']
    print(f'Weather in {location}:')
    print(f'Temperature: {temperature} °F')
    print(f'Humidity: {humidity}%')
    print(f'Condition: {condition}')

# Function to display forecast
def display_forecast(location):
    data = get_weather_data(location)
    forecast = data['forecast']
    print(f'3-day forecast for {location}:')
    for day in forecast:
        print(f'{day["date"]} - {day["condition"]}, High: {day["high"]} °F, Low: {day["low"]} °F')

# Command-line interface
location = input('Enter location (city or zip code): ')
display_weather(location)
display_forecast(location)

