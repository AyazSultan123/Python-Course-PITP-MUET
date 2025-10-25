import os
import sys
import requests
from datetime import datetime, timedelta

API_KEY = ""  # Replace with your actual API key
API_URL = "https://api.openweathermap.org/data/2.5/weather"

def format_time(unix_ts, tz_offset_seconds):
    utc = datetime.utcfromtimestamp(unix_ts)
    local = utc + timedelta(seconds=tz_offset_seconds)
    return local.strftime("%Y-%m-%d %H:%M:%S")

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def show_weather(data):
    name = data.get("name", "Unknown")
    country = data.get("sys", {}).get("country", "")
    weather = data.get("weather", [{}])[0].get("description", "N/A").capitalize()
    temp = data.get("main", {}).get("temp", "N/A")
    feels_like = data.get("main", {}).get("feels_like", "N/A")
    humidity = data.get("main", {}).get("humidity", "N/A")
    pressure = data.get("main", {}).get("pressure", "N/A")
    wind = data.get("wind", {}).get("speed", "N/A")
    tz_offset = data.get("timezone", 0)
    sunrise = format_time(data.get("sys", {}).get("sunrise"), tz_offset)
    sunset = format_time(data.get("sys", {}).get("sunset"), tz_offset)

    print(f"\nWeather in {name}, {country}")
    print("-" * 40)
    print(f"Condition   : {weather}")
    print(f"Temperature : {temp} °C (feels like {feels_like} °C)")
    print(f"Humidity    : {humidity}%")
    print(f"Pressure    : {pressure} hPa")
    print(f"Wind Speed  : {wind} m/s")
    print(f"Sunrise     : {sunrise}")
    print(f"Sunset      : {sunset}")
    print("-" * 40)

def main():
    city = input("Enter city name: ").strip()
    if not city:
        print("City name cannot be empty.")
        return
    data = get_weather(city)
    if data:
        show_weather(data)

if __name__ == "__main__":
    main()
