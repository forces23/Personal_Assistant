import requests
import datetime

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = "10a6e45597aa881e175f139b42e2c97a"

def convert_unix_to_cst(unix_timestamp):
    datetime_obj = datetime.datetime.fromtimestamp(unix_timestamp)
    formatted_ts = datetime_obj.strftime("%I:%M %p")
    
    return formatted_ts

def get_weather_data(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units" : "imperial" # Use "metric" for Celcius
    }
           
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data.")
        return None
    
def main():
    city_name = "Jefferson City"
    weather_data = get_weather_data(city_name)
    
    if weather_data:
        print(f"------ Current weather in {weather_data['name']} ------")
        print(f"Temperature : {weather_data['main']['temp']}°F")
        print(f"Feels Like : {weather_data['main']['feels_like']}°F")
        print(f"Description : {weather_data['weather'][0]['description']}")
        print(f"Sunrise : {convert_unix_to_cst(weather_data['sys']['sunrise'])}")
        print(f"Sunset : {convert_unix_to_cst(weather_data['sys']['sunset'])}")
        
        # print(f"\n\nWeather Data : \n{weather_data}")
    else:
        print("Weather data not avaialable.")
        
if __name__ == "__main__":
    main()