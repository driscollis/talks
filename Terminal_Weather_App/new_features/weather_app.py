# weather_app.py

import pgeocode
import requests

from rich.text import Text
from textual import on, work
from textual.app import App, ComposeResult
from textual.containers import Horizontal, HorizontalGroup, VerticalScroll, Vertical
from textual.widgets import Button, Label, Header, Input, Select
from textual.worker import get_current_worker

wmo_codes = {0: "Clear sky",
             1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
             45: "Fog", 48: "Fog with depositing rime",
             51: "Light Drizzle", 53: "Moderate Drizzle", 55: "Dense Drizzle",
             56: "Light Freezing Drizzle", 57: "Denze Freezing Drizzle",
             61: "Light Rain", 63: "Moderate Rain", 65: "Heavy Rain",
             66: "Light Freezing Fain", 67: "Heavy Freezing Rain",
             71: "Light Snow", 73: "Moderate Snow", 75: "Heavy Snow",
             77: "Flurries",
             80: "Light Rain", 81: "Moderate Rain", 82: "Violent Rain",
             85: "Slight Snow Showers", 86: "Heavy Snow Showers",
             95: "Thunderstorms",
             96: "Thunderstorms w/ Light Hail",
             99: "Thunderstorms w/ Heavy Hail",}

wmo_to_emoji = {
    0: "sun",
    1: "sun_with_face",
    2: "partly_sunny", 3: "cloud",
    51: "cloud_with_rain", 52: "cloud_with_rain", 53: "cloud_with_rain",
    55: "cloud_with_rain",
    45: "fog", 48: "foggy",
    56: "ice", 57: "ice",
    61: "cloud_with_rain", 63: "cloud_with_rain", 65: "cloud_with_rain",
    66: "ice", 67: "ice",
    71: "snowflake", 73: "snowflake", 75: "snowflake",
    80: "cloud_with_rain", 81: "cloud_with_rain", 82: "cloud_with_rain",
    85: "snowflake", 86: "snowflake",
    95: "thunder_cloud_and_rain", 95: "cloud_with_lightning_and_rain",
    99: "cloud_with_lightning_and_rain",}

class Weather(HorizontalGroup):

    def __init__(self, postal_code: str, country: str, temp_unit: str) -> None:
        super().__init__()
        self.postal_code = postal_code
        self.country = country
        self.temp_unit = temp_unit  # Fahrenheit or Celsius

        # Update the weather once every hour
        self.set_interval(3600, self.update_weather)

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Location", id=f"location_{self.postal_code}"),
            Label("Current Temp", id=f"current_temp_{self.postal_code}"),
            Label("", id=f"wmo_{self.postal_code}"),
        )
        yield Vertical(
            Label("Weekday +1", id=f"plus_one_{self.postal_code}"),
            Label("Temp", id=f"plus_one_temp_{self.postal_code}"),
            Label("Weather", id=f"plus_one_weather_{self.postal_code}")
        )
        yield Vertical(
            Label("Weekday +1", id=f"plus_two_{self.postal_code}"),
            Label("Temp", id=f"plus_two_temp_{self.postal_code}"),
            Label("Weather", id=f"plus_two_weather_{self.postal_code}")
        )
        yield Vertical(
            Label("Weekday +1", id=f"plus_three_{self.postal_code}"),
            Label("Temp", id=f"plus_three_temp_{self.postal_code}"),
            Label("Weather", id=f"plus_three_weather_{self.postal_code}")
        )

    def on_mount(self) -> None:
        self.update_weather()

    @work(exclusive=True, thread=True, group="weather")
    def update_weather(self):
        worker = get_current_worker()
        nomi = pgeocode.Nominatim(self.country)
        location = nomi.query_postal_code(self.postal_code)
        lat = location["latitude"]
        lon = location["longitude"]

        url = (f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,"
               f"precipitation,rain,weather_code&daily=weather_code,temperature_2m_max,temperature_2m_min"
               f"&temperature_unit={self.temp_unit}&timezone=America%2FChicago")
        response = requests.get(url)

        if not worker.is_cancelled and response.status_code == 200:
            weather_data = response.json()
            self.app.call_from_thread(self.update_ui, location, weather_data)

    def update_ui(self, location, weather_data):
        town =  location["place_name"]
        state_code = location["state_code"]
        temp = weather_data["current"]["temperature_2m"]

        temp_abbrev = "F" if self.temp_unit == "fahrenheit" else "C"

        wmo_code = weather_data["daily"]["weather_code"][0]
        emoji = Text.from_markup(f":{wmo_to_emoji[wmo_code]}:")
        weather =  f"Current Weather: {emoji}  {wmo_codes[wmo_code]}"

        self.app.query_one(f"#location_{self.postal_code}").update(
            Text(f"{town}, {state_code}", style="magenta2"))
        self.app.query_one(f"#current_temp_{self.postal_code}").update(
            Text(f"Current Temp: {temp} {temp_abbrev}", style="gold1"))
        self.app.query_one(f"#wmo_{self.postal_code}").update(Text(f"{weather}", style="gold1"))

        # Update 3-Day forecast
        tags = ["plus_one", "plus_two", "plus_three"]
        count = 1
        for tag in tags:
            low = weather_data["daily"]["temperature_2m_min"][count]
            high = weather_data["daily"]["temperature_2m_max"][count]
            wmo_code = weather_data["daily"]["weather_code"][count]
            emoji = Text.from_markup(f":{wmo_to_emoji[wmo_code]}:")
            day = weather_data['daily']['time'][count]

            self.app.query_one(f"#{tag}_{self.postal_code}").update(Text(f"{day}", style="green"))
            self.app.query_one(f"#{tag}_temp_{self.postal_code}").update(
                Text(f"Low: {low} {temp_abbrev} / High: {high} {temp_abbrev}", style="orange3"))
            self.app.query_one(f"#{tag}_weather_{self.postal_code}").update(
                Text(f"{emoji}  {wmo_codes[wmo_code]}", style="blue"))
            count += 1

        self.notify(f"Weather updated for {town} {state_code}")

class WeatherApp(App):

    CSS_PATH = "weather.tcss"

    def compose(self) -> ComposeResult:
        country_options = [("United States", "us"), ("France", "fr")]
        temp_unit_options = [("Celsius", "celsius"), ("Fahrenheit", "fahrenheit")]
        yield Header()
        yield Horizontal(
            Input(placeholder="Postal Code", id="postal_code"),
            Select(country_options, value=country_options[0][1], id="country"),
            Select(temp_unit_options, value=temp_unit_options[0][1], id="temp_unit"),
            Button("Add Weather", id="add_weather"),
            id="add_weather"
        )
        yield VerticalScroll(id="vertical_scroll")

    @on(Button.Pressed, "#add_weather")
    def on_weather_added(self) -> None:
        postal_code = self.query_one("#postal_code", Input).value
        country = self.query_one("#country").value
        temp_unit = self.query_one("#temp_unit").value
        if postal_code:
            self.query_one("#vertical_scroll").mount(Weather(postal_code, country, temp_unit))

if __name__ == "__main__":
    app = WeatherApp()
    app.run()
