import os
from pathlib import Path
from dotenv import load_dotenv

# Locates the root directory of week6-weather-dashboard
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

# Explicitly load from the absolute path
load_dotenv(dotenv_path=ENV_PATH)

API_KEY = os.getenv("OPENWEATHER_API_KEY", "").strip()
BASE_URL = "http://api.openweathermap.org/data/2.5"
CACHE_DURATION = 600