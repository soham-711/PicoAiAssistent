import requests

# Get your location from IP
def get_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        loc = data.get("loc")  # latitude,longitude
        return {
            "city": city,
            "region": region,
            "country": country,
            "loc": loc
        }
    except Exception as e:
        return {"error": str(e)}

# Get weather data using OpenWeatherMap
def get_weather(location, api_key="2bc923bd9a8379e644395f208bce1664"):
    try:
        lat, lon = location["loc"].split(",")
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return {
                "location": f"{location['city']}, {location['region']}, {location['country']}",
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "weather": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"]
            }
        else:
            return {"error": data.get("message", "Unable to fetch weather")}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    location = get_location()
    if "error" not in location:
        weather = get_weather(location)
        print("Weather Data:", weather)
    else:
        print("Location Error:", location["error"])
