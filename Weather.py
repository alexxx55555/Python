import requests

def convert_to_celsius(kelvin_temp):
    """Convert temperature from Kelvin to Celsius."""
    return kelvin_temp - 273.15

def convert_to_fahrenheit(kelvin_temp):
    """Convert temperature from Kelvin to Fahrenheit."""
    return (kelvin_temp - 273.15) * 9/5 + 32

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    try:
        # Get the response from the URL
        response = requests.get(complete_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        # Convert the response to JSON
        weather_data = response.json()
        # Check if the city is found
        if weather_data.get("cod") == 200:
            main = weather_data["main"]
            weather = weather_data["weather"][0]
            sys = weather_data["sys"]
            # Get city name and country code
            city = weather_data["name"]
            country = sys["country"]
            # Get temperature, feels_like, pressure, humidity
            temperature_celsius = convert_to_celsius(main["temp"])
            feels_like_celsius = convert_to_celsius(main["feels_like"])
            temperature_fahrenheit = convert_to_fahrenheit(main["temp"])
            feels_like_fahrenheit = convert_to_fahrenheit(main["feels_like"])
            pressure = main["pressure"]
            humidity = main["humidity"]
            # Get weather description
            weather_description = weather["description"]
            # Print weather information
            print(f"\nWeather in {city}, {country}")
            print(f"Temperature: {temperature_celsius:.0f}°C / {temperature_fahrenheit:.0f}°F")
            print(f"Feels Like: {feels_like_celsius:.0f}°C / {feels_like_fahrenheit:.0f}°F")
            print(f"Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
            print(f"Weather Description: {weather_description.capitalize()}\n")
        else:
            print("City not found!")
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print("City not found!")
        else:
            print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

if __name__ == "__main__":
    api_key = "a2678816f3f56c1ca5339201b9ca25eb"  # Replace with your OpenWeatherMap API key
    while True:
        city_name = input("Enter city name (or type 'exit' to quit): ")
        if city_name.lower() == "exit":
            print("Exiting the program.")
            break
        get_weather(city_name, api_key)
