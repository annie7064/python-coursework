from typing import Dict, List

class WeatherDisplay:
    """Formats weather data for terminal presentation."""

    @staticmethod
    def render(current: Dict, forecast: List[Dict]):
        print("\n🌤️  WEATHER DASHBOARD")
        print("=======================")
        print(f"\n📍 Current Location: {current['city']}, {current['country']}")
        print(f"🕐 Last Updated: {current['updated']}")
        print("\nCurrent Weather:")
        print("────────────────")
        print(f"Temperature:   {current['temp']}°C (Feels like: {current['feels_like']}°C)")
        print(f"Conditions:    {current['description']} {current['icon']}")
        print(f"Humidity:      {current['humidity']}%")
        print(f"Wind:          {current['wind_speed']} km/h")
        print(f"Pressure:      {current['pressure']} hPa")

        print("\n5-Day Forecast:")
        print("───────────────")
        for f in forecast:
            print(f"{f['date']}:  {f['icon']}   {f['max_temp']}°C / {f['min_temp']}°C")
        print()