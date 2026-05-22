import requests
api_key = "47be26794bd535c5710f9ce348533a22"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_weather_data():
    print("Fetching weather data from Weatherstack API...")
    try:
        response = requests.get(api_url, timeout=30)
        response.raise_for_status()  # Check if the request was successful
        print("Data fetched successfully!")
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        raise


def mock_fetch_data():
    print("Mock fetching weather data...")
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-05-20 07:30', 'localtime_epoch': 1779262200, 'utc_offset': '-4.0'}, 'current': {'observation_time': '11:30 AM', 'temperature': 25, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Sunny'], 'astro': {'sunrise': '05:35 AM', 'sunset': '08:11 PM', 'moonrise': '09:05 AM', 'moonset': 'No moonset', 'moon_phase': 'Waxing Crescent', 'moon_illumination': 15}, 'air_quality': {'co': '172.85', 'no2': '6.45', 'o3': '138', 'so2': '2.95', 'pm2_5': '12.55', 'pm10': '14.75', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 14, 'wind_degree': 246, 'wind_dir': 'WSW', 'pressure': 1015, 'precip': 0, 'humidity': 61, 'cloudcover': 6, 'feelslike': 26, 'uv_index': 0, 'visibility': 10, 'is_day': 'yes'}}