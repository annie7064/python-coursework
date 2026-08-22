import requests
import json
import time
from pathlib import Path
from typing import Optional, Dict

class WeatherAPI:
    """Handles all weather API interactions with caching and error handling."""

    def __init__(self, api_key: str, base_url: str = "http://api.openweathermap.org/data/2.5"):
        self.api_key = api_key
        self.base_url = base_url
        self.cache_dir = Path(__file__).resolve().parent.parent / "data" / "cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.cache_duration = 600

    def _get_cached_data(self, cache_key: str) -> Optional[Dict]:
        cache_file = self.cache_dir / f"{cache_key}.json"
        if cache_file.exists():
            if time.time() - cache_file.stat().st_mtime < self.cache_duration:
                try:
                    with open(cache_file, 'r') as f:
                        return json.load(f)
                except Exception:
                    pass
        return None

    def _save_to_cache(self, cache_key: str, data: Dict):
        cache_file = self.cache_dir / f"{cache_key}.json"
        try:
            with open(cache_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception:
            pass

    def _make_request(self, endpoint: str, params: Dict) -> Optional[Dict]:
        try:
            params['appid'] = self.api_key
            params['units'] = 'metric'
            response = requests.get(f"{self.base_url}/{endpoint}", params=params, timeout=10)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                print("\nError: Invalid API key. Update your .env file.")
            elif response.status_code == 404:
                print("\nError: City not found.")
            else:
                print(f"\nError: API request failed with status {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"\nNetwork Error: {e}")
        return None

    def get_current_weather(self, city: str) -> Optional[Dict]:
        cache_key = f"current_{city.lower().replace(' ', '_')}"
        cached = self._get_cached_data(cache_key)
        if cached:
            return cached

        data = self._make_request("weather", {'q': city})
        if data:
            self._save_to_cache(cache_key, data)
        return data

    def get_forecast(self, city: str) -> Optional[Dict]:
        cache_key = f"forecast_{city.lower().replace(' ', '_')}"
        cached = self._get_cached_data(cache_key)
        if cached:
            return cached

        data = self._make_request("forecast", {'q': city})
        if data:
            self._save_to_cache(cache_key, data)
        return data