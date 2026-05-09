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
    
# funkce aktualizuje čas každou sekundu
def aktualizuj_cas():
    cas = datetime.now().strftime("%H:%M:%S")
    cas_label.configure(text=f"🕐 {cas}")
    # zavolá samu sebe znovu za 1000ms
    okno_app.after(1000, aktualizuj_cas)

# vytvoření hlavního okna
ctk.set_appearance_mode("Dark")
okno_app = ctk.CTk()
okno_app.title("🗂 Dashboard")
okno_app.geometry("900x600")

# hlavní rámeček rozdělený na levou a pravou část
levy_ramec = ctk.CTkFrame(okno_app)
levy_ramec.pack(side="left", fill="both", expand=True, padx=10, pady=10)

pravy_ramec = ctk.CTkFrame(okno_app)
pravy_ramec.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# levá část - label pro čas
cas_label = ctk.CTkLabel(levy_ramec, text="", font=("Arial", 24))
cas_label.pack(pady=20)

# label pro počasí
pocasi_label = ctk.CTkLabel(levy_ramec, text=ziskej_pocasi(), font=("Arial", 14))
pocasi_label.pack(pady=10)