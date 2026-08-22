from datetime import datetime
from typing import Dict, List

class WeatherParser:
    """Parses raw OpenWeatherMap JSON responses into clean dict structures."""

    CONDITION_ICONS = {
        'Clear': '☀️',
        'Clouds': '☁️',
        'Rain': '🌧️',
        'Drizzle': '🌦️',
        'Thunderstorm': '🌩️',
        'Snow': '❄️',
        'Mist': '🌫️'
    }

    @staticmethod
    def parse_current(data: Dict) -> Dict:
        main_cond = data.get('weather', [{}])[0].get('main', 'Clear')
        return {
            'city': data.get('name', 'Unknown'),
            'country': data.get('sys', {}).get('country', ''),
            'temp': round(data.get('main', {}).get('temp', 0)),
            'feels_like': round(data.get('main', {}).get('feels_like', 0)),
            'humidity': data.get('main', {}).get('humidity', 0),
            'pressure': data.get('main', {}).get('pressure', 0),
            'description': data.get('weather', [{}])[0].get('description', '').capitalize(),
            'wind_speed': round(data.get('wind', {}).get('speed', 0) * 3.6),  # m/s to km/h
            'icon': WeatherParser.CONDITION_ICONS.get(main_cond, '🌤️'),
            'updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

    @staticmethod
    def parse_forecast(data: Dict) -> List[Dict]:
        daily = {}
        for entry in data.get('list', []):
            dt_txt = entry.get('dt_txt', '')
            date_str = dt_txt.split(' ')[0]
            temp = entry.get('main', {}).get('temp', 0)
            cond = entry.get('weather', [{}])[0].get('main', 'Clear')

            if date_str not in daily:
                daily[date_str] = {'temps': [], 'conditions': []}
            daily[date_str]['temps'].append(temp)
            daily[date_str]['conditions'].append(cond)

        forecast_summary = []
        for date_str, values in list(daily.items())[:5]:
            formatted_date = datetime.strptime(date_str, '%Y-%m-%d').strftime('%a %d %b')
            max_t = round(max(values['temps']))
            min_t = round(min(values['temps']))
            most_common_cond = max(set(values['conditions']), key=values['conditions'].count)
            icon = WeatherParser.CONDITION_ICONS.get(most_common_cond, '🌤️')
            forecast_summary.append({
                'date': formatted_date,
                'icon': icon,
                'max_temp': max_t,
                'min_temp': min_t
            })
        return forecast_summary