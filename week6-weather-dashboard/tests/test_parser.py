import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from weather_app.weather_parser import WeatherParser

class TestWeatherParser(unittest.TestCase):

    def test_parse_current(self):
        sample = {
            'name': 'London',
            'sys': {'country': 'GB'},
            'main': {'temp': 8.4, 'feels_like': 5.2, 'humidity': 87, 'pressure': 1009},
            'weather': [{'main': 'Rain', 'description': 'light rain'}],
            'wind': {'speed': 6.1}
        }
        parsed = WeatherParser.parse_current(sample)
        self.assertEqual(parsed['city'], 'London')
        self.assertEqual(parsed['temp'], 8)
        self.assertEqual(parsed['icon'], '🌧️')

if __name__ == "__main__":
    unittest.main()