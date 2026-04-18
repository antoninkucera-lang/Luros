import requests
import os
from dotenv import load_dotenv
import customtkinter as ctk
import webbrowser
import pyperclip
from datetime import datetime

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
    # smazání uložených odkazů
    odkazy.clear()
    aktualizuj_tlacitka_odkazu()

# funkce zkopíruje odkaz do schránky
def zkopiruj_odkaz(odkaz):
    pyperclip.copy(odkaz)

# funkce zobrazí nebo skryje tlačítka odkazů
def aktualizuj_tlacitka_odkazu():
    # smazání starých tlačítek
    for tlacitko in tlacitka_odkazu:
        tlacitko.destroy()
    tlacitka_odkazu.clear()
    # vytvoření nových tlačítek pro každý odkaz
    for i, odkaz in enumerate(odkazy):
        t = ctk.CTkButton(
            ramec_odkazu,
            text=f"📋 Kopírovat odkaz {i + 1}",
            command=lambda o=odkaz: zkopiruj_odkaz(o),
            width=200,
            height=25
        )
        t.pack(pady=2)
        tlacitka_odkazu.append(t)

# funkce aktualizuje čas každou sekundu
def aktualizuj_cas():
    cas = datetime.now().strftime("%H:%M:%S")
    cas_label.configure(text=f"🕐 {cas}")
    # zavolá samu sebe znovu za 1000ms
    okno_app.after(1000, aktualizuj_cas)

# seznam uložených odkazů a tlačítek
odkazy = []
tlacitka_odkazu = []

# vytvoření hlavního okna
ctk.set_appearance_mode("Dark")
okno_app = ctk.CTk()
okno_app.title("Vyhledávač receptů")
okno_app.geometry("600x800")

# textové pole pro zadání ingrediencí
pole = ctk.CTkEntry(okno_app, width=400, placeholder_text="Zadej ingredience (odděl čárkou)")
pole.pack(pady=20)

# label pro zobrazení počasí
pocasi_label = ctk.CTkLabel(okno_app, text=ziskej_pocasi("Trinec"))
pocasi_label.pack(pady=5)

# label pro zobrazení aktuálního času
cas_label = ctk.CTkLabel(okno_app, text="")
cas_label.pack(pady=2)

# spuštění aktualizace času
aktualizuj_cas()

# slider pro nastavení počtu receptů
pocet_label = ctk.CTkLabel(okno_app, text="Počet receptů: 5")
pocet_label.pack()

slider = ctk.CTkSlider(okno_app, from_=1, to=15, number_of_steps=14)
slider.set(5)
slider.pack(pady=5)

# funkce aktualizuje label při pohybu sliderem - tooltip
def aktualizuj_label(hodnota):
    pocet_label.configure(text=f"Počet receptů: {int(hodnota)} (posuň slider pro změnu)")

slider.configure(command=aktualizuj_label)

# textová oblast pro zobrazení výsledků - nelze editovat
vysledky = ctk.CTkTextbox(okno_app, width=500, height=300, state="disabled")
vysledky.pack(pady=10)

# rámeček pro tlačítka odkazů
ramec_odkazu = ctk.CTkFrame(okno_app, fg_color="transparent")
ramec_odkazu.pack()

# funkce se spustí po stisku Enter
def po_kliknuti(event=None):
    ingredience = pole.get()
    # smazání předchozích výsledků a odkazů vždy na začátku
    vysledky.configure(state="normal")
    vysledky.delete("1.0", "end")
    odkazy.clear()
    aktualizuj_tlacitka_odkazu()
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
    for i, recept in enumerate(recepty):
        vysledky.insert("end", f"{recept['title']}\n")
        vysledky.insert("end", f"Použité ingredience: {recept['usedIngredientCount']}\n")
        vysledky.insert("end", f"Chybějící ingredience: {recept['missedIngredientCount']}\n")
        # získání odkazu a uložení do seznamu
        odkaz = ziskej_odkaz(recept['id'])
        if odkaz:
            vysledky.insert("end", f"Odkaz {i + 1}: viz tlačítko níže\n")
            odkazy.append(odkaz)
        vysledky.insert("end", "---\n")
    vysledky.configure(state="disabled")
    # zobrazení tlačítek pro kopírování odkazů
    aktualizuj_tlacitka_odkazu()

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