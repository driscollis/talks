# weather_app.py

import pgeocode
import requests

from rich.text import Text
from textual import on, work
from textual.app import App, ComposeResult
from textual.containers import Horizontal, HorizontalGroup, VerticalScroll, Vertical
from textual.widgets import Button, Label, Header, Input
from textual.worker import get_current_worker

# Weather Meteorological Organization (WMO) codes
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