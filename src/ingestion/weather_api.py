import requests

API_KEY = "YOUR_API_KEY"

def get_weather(city="Delhi"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    
    response = requests.get(url)
    data = response.json()
    
    return data