import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io

API_KEY = 'a2678816f3f56c1ca5339201b9ca25eb'  # Replace with your OpenWeatherMap API key

def convert_to_celsius(kelvin_temp):
    """Convert temperature from Kelvin to Celsius."""
    return kelvin_temp - 273.15

def get_weather_and_country_code(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + API_KEY
    try:
        response = requests.get(complete_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        weather_data = response.json()
        if weather_data.get("cod") == 200:
            country_code = weather_data["sys"]["country"].lower()
            weather_info = {
                "city": weather_data["name"],
                "country": country_code,
                "temperature": convert_to_celsius(weather_data["main"]["temp"]),
                "feels_like": convert_to_celsius(weather_data["main"]["feels_like"]),
                "pressure": weather_data["main"]["pressure"],
                "humidity": weather_data["main"]["humidity"],
                "description": weather_data["weather"][0]["description"].capitalize()
            }
            return weather_info
        else:
            return None
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print("City not found!")
        else:
            print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"Other error occurred: {err}")
        return None

def get_country_flag_url(country_code):
    return f"https://flagcdn.com/w320/{country_code}.png"

def show_country_flag_and_weather(city_name):
    weather_info = get_weather_and_country_code(city_name)
    if weather_info:
        flag_url = get_country_flag_url(weather_info["country"])
        update_weather_info(weather_info)
        display_flag_image(flag_url)
    else:
        messagebox.showerror("Error", f"Failed to get weather and flag for {city_name}")

def update_weather_info(weather_info):
    weather_text = (
        f"Weather in {weather_info['city']}, {weather_info['country'].upper()}\n"
        f"Temperature: {weather_info['temperature']:.0f}°C\n"
        f"Feels Like: {weather_info['feels_like']:.0f}°C\n"
        f"Pressure: {weather_info['pressure']} hPa\n"
        f"Humidity: {weather_info['humidity']}%\n"
        f"Description: {weather_info['description']}\n"
    )
    weather_label.config(text=weather_text)

def display_flag_image(flag_url):
    try:
        response = requests.get(flag_url)
        response.raise_for_status()
        image_data = response.content
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((100, 60), Image.Resampling.LANCZOS)  # Resize the flag image
        flag_image = ImageTk.PhotoImage(image)
        flag_label.config(image=flag_image)
        flag_label.image = flag_image
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "Failed to load flag image")

# tkinter GUI
root = tk.Tk()
root.title("City to Country Flag and Weather Viewer")

entry_label = tk.Label(root, text="Enter City Name:")
entry_label.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack()

fetch_button = tk.Button(root, text="Show Weather and Flag", command=lambda: show_country_flag_and_weather(city_entry.get()))
fetch_button.pack(pady=10)

weather_label = tk.Label(root, text="", justify=tk.LEFT)
weather_label.pack(pady=10)

flag_label = tk.Label(root)
flag_label.pack(pady=10)

root.mainloop()