from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/")
def index():
    """Fetches the current weather in Stockholm and renders it on the homepage."""
    params = {
        "q": "Stockholm",
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    weather_data = response.json()
    current_temp = weather_data["main"]["temp"]

    return render_template("index.html", current_temp=current_temp)

if __name__ == "__main__":
    app.run(port=8000)
