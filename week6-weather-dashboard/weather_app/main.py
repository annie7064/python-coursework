import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from weather_app.config import API_KEY
from weather_app.weather_api import WeatherAPI
from weather_app.weather_parser import WeatherParser
from weather_app.weather_display import WeatherDisplay

def main():
    if not API_KEY or API_KEY == "your_openweather_api_key_here":
        print("Error: OPENWEATHER_API_KEY is not set in .env")
        print("Please set your API key in week6-weather-dashboard/.env and try again.")
        return

    api = WeatherAPI(api_key=API_KEY)
    current_city = "London"

    while True:
        raw_current = api.get_current_weather(current_city)
        raw_forecast = api.get_forecast(current_city)

        if raw_current and raw_forecast:
            parsed_current = WeatherParser.parse_current(raw_current)
            parsed_forecast = WeatherParser.parse_forecast(raw_forecast)
            WeatherDisplay.render(parsed_current, parsed_forecast)
        
        cmd = input("Search city or command (refresh/quit): ").strip().lower()
        if cmd == 'quit':
            break
        elif cmd == 'refresh':
            continue
        elif cmd:
            current_city = cmd

if __name__ == "__main__":
    main()