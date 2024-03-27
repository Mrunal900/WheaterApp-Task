import requests


def get_weather(city_name):
  # API key should be kept secure and not shared in public.
    api_key = '8b45781c5307f5fe1c518c90db55b505'
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()


        city = data['name']
        temperature = data['main']['temp']
        description = data['weather'][0]['description']

        return {'city': city, 'temperature': temperature, 'description': description}

    except (requests.RequestException) as error:
        print(f"Error fetching weather data for {city_name}: {error}")
        return None



if __name__ == "__main__":
    city_name = input("Enter City Name: ")
    weather_data = get_weather(city_name)
    if weather_data:
        print(f"Current weather in {weather_data['city']}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Description: {weather_data['description']}")
    else:
        print("Failed to retrieve weather data.")