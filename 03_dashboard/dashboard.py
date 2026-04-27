import os
import requests
from dotenv import load_dotenv
import customtkinter as ctk
from datetime import datetime

# načtení API klíčů z .env souboru
load_dotenv()
WEATHER_KEY = os.getenv("WEATHER_KEY")
NEWS_KEY = os.getenv("NEWS_KEY")

# funkce získá aktuální počasí pro dané město
def ziskej_pocasi():
    url = "http://api.weatherstack.com/current"
    params = {
        "access_key": WEATHER_KEY,
        "query": "Trinec",
        "units": "m"
    }
    try:
        odpoved = requests.get(url, params=params)
        data = odpoved.json()
        teplota = data["current"]["temperature"]
        popis = data["current"]["weather_descriptions"][0]
        return f"🌤 Třinec: {popis}, {teplota}°C"
    except:
        return "Počasí nedostupné"
    
# funkce získá aktuální české zprávy
def ziskej_zpravy():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "cz",
        "apiKey": NEWS_KEY,
        "pageSize": 5
    }
    try:
        odpoved = requests.get(url, params=params)
        data = odpoved.json()
        clanky = data["articles"]
        return [clanek["title"] for clanek in clanky]
    except:
        return ["Zprávy nedostupné"]
    
# funkce uloží poznámky do souboru
def uloz_poznamky(text):
    with open("poznamky.txt", "w", encoding="utf-8") as soubor:
        soubor.write(text)

# funkce načte poznámky ze souboru
def nacti_poznamky():
    try:
        with open("poznamky.txt", "r", encoding="utf-8") as soubor:
            return soubor.read()
    except:
        return ""