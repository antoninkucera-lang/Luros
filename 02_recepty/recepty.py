import requests
import os
from dotenv import load_dotenv
import customtkinter as ctk
import webbrowser

# Načtení API klíče z .env souboru
load_dotenv()
API_KEY = os.getenv("API_KEY")
WEATHER_KEY = os.getenv("WEATHER_KEY")

if not API_KEY:
    print("Chyba: API_KEY není nastaven v .env souboru.")
    exit(1)

# Adresa API pro hledání receptů podle ingrediencí
BASE_URL = "https://api.spoonacular.com/recipes/findByIngredients"

# Funkce pošle dotaz na API a vrátí seznam receptů
def hledej_recepty(ingredience):
    # Parametry dotazu - ingredience, počet výsledků ze slideru a API klíč
    params = {
        "ingredients": ingredience,
        "number": int(slider.get()),
        "apiKey": API_KEY
    }
    try:
        # Odeslání dotazu na API
        odpoved = requests.get(BASE_URL, params=params)
        if odpoved.status_code != 200:
            return []
        # Vrácení odpovědi jako Python slovník
        return odpoved.json()
    except requests.exceptions.ConnectionError:
        # Chyba při výpadku internetu
        vysledky.configure(state="normal")
        vysledky.insert("end", "Chyba: Nejsi připojen k internetu.\n")
        vysledky.configure(state="disabled")
        return []
    except Exception as e:
        # Zachycení jakékoliv jiné chyby
        vysledky.configure(state="normal")
        vysledky.insert("end", f"Neočekávaná chyba: {e}\n")
        vysledky.configure(state="disabled")
        return []

# Funkce získá odkaz na recept podle jeho id
def ziskej_odkaz(recept_id):
    url = f"https://api.spoonacular.com/recipes/{recept_id}/information"
    try:
        odpoved = requests.get(url, params={"apiKey": API_KEY})
        if odpoved.status_code != 200:
            return None
        return odpoved.json().get("sourceUrl")
    except:
        return None

# Funkce získá aktuální počasí pro dané město
def ziskej_pocasi(mesto):
    url = "http://api.weatherstack.com/current"
    params = {
        "access_key": WEATHER_KEY,
        "query": mesto,
        "units": "m"
    }
    try:
        odpoved = requests.get(url, params=params)
        data = odpoved.json()
        teplota = data["current"]["temperature"]
        popis = data["current"]["weather_descriptions"][0]
        return f"{mesto}: {popis}, {teplota}°C"
    except:
        return "Počasí nedostupné"

# funkce přepne světlý/tmavý režim
def prepni_rezim():
    aktualni = ctk.get_appearance_mode()
    if aktualni == "Dark":
        ctk.set_appearance_mode("Light")
        tlacitko_rezim.configure(text="🌙 Tmavý režim")
    else:
        ctk.set_appearance_mode("Dark")
        tlacitko_rezim.configure(text="☀️ Světlý režim")

# funkce vymaže textové pole i výsledky
def vymaz():
    pole.delete(0, "end")
    vysledky.configure(state="normal")
    vysledky.delete("1.0", "end")
    vysledky.configure(state="disabled")

# vytvoření hlavního okna
ctk.set_appearance_mode("Dark")
okno_app = ctk.CTk()
okno_app.title("Vyhledávač receptů")
okno_app.geometry("600x700")

# textové pole pro zadání ingrediencí
pole = ctk.CTkEntry(okno_app, width=400, placeholder_text="Zadej ingredience (odděl čárkou)")
pole.pack(pady=20)

# label pro zobrazení počasí
pocasi_label = ctk.CTkLabel(okno_app, text=ziskej_pocasi("Trinec"))
pocasi_label.pack(pady=5)

# slider pro nastavení počtu receptů
pocet_label = ctk.CTkLabel(okno_app, text="Počet receptů: 5")
pocet_label.pack()

slider = ctk.CTkSlider(okno_app, from_=1, to=15, number_of_steps=14)
slider.set(5)
slider.pack(pady=5)

# funkce aktualizuje label při pohybu sliderem
def aktualizuj_label(hodnota):
    pocet_label.configure(text=f"Počet receptů: {int(hodnota)}")

slider.configure(command=aktualizuj_label)

# textová oblast pro zobrazení výsledků - nelze editovat
vysledky = ctk.CTkTextbox(okno_app, width=500, height=400, state="disabled")
vysledky.pack(pady=10)

# funkce se spustí po kliknutí na tlačítko
def po_kliknuti(event=None):
    ingredience = pole.get()
    # smazání předchozích výsledků vždy na začátku
    vysledky.configure(state="normal")
    vysledky.delete("1.0", "end")
    # kontrola jestli uživatel zadal ingredience
    if not ingredience:
        vysledky.insert("end", "Zadej prosím ingredience!\n")
        vysledky.configure(state="disabled")
        return
    # zavolání API a výpis výsledků
    recepty = hledej_recepty(ingredience)
    # seřazení receptů podle počtu chybějících ingrediencí - nejlepší shoda nahoře
    recepty = sorted(recepty, key=lambda r: r['missedIngredientCount'])
    # smyčka projde každý recept a vypíše ho
    for recept in recepty:
        vysledky.insert("end", f"{recept['title']}\n")
        vysledky.insert("end", f"Použité ingredience: {recept['usedIngredientCount']}\n")
        vysledky.insert("end", f"Chybějící ingredience: {recept['missedIngredientCount']}\n")
        # získání a zobrazení odkazu na recept
        odkaz = ziskej_odkaz(recept['id'])
        if odkaz:
            vysledky.insert("end", f"Odkaz: {odkaz}\n")
        vysledky.insert("end", "---\n")
    vysledky.configure(state="disabled")

# spuštění hledání po stisku Enter v textovém poli
pole.bind("<Return>", po_kliknuti)

# tlačítko pro vymazání pole a výsledků
tlacitko_vymaz = ctk.CTkButton(okno_app, text="Vymazat", command=vymaz, fg_color="gray")
tlacitko_vymaz.pack(pady=5)

# tlačítko pro přepnutí režimu
tlacitko_rezim = ctk.CTkButton(okno_app, text="☀️ Světlý režim", command=prepni_rezim, width=150)
tlacitko_rezim.pack(pady=5)

# spuštění okna
okno_app.mainloop()