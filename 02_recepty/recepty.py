import requests
import os
from dotenv import load_dotenv
import customtkinter as ctk

# Načtení API klíče z .env souboru
load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("Chyba: API_KEY není nastaven v .env souboru.")
    exit(1)

# Adresa API pro hledání receptů podle ingrediencí
BASE_URL = "https://api.spoonacular.com/recipes/findByIngredients"

# Funkce pošle dotaz na API a vrátí seznam receptů
def hledej_recepty(ingredience):
    # Parametry dotazu - ingredience, počet výsledků a API klíč
    params = {
        "ingredients": ingredience,
        "number": 5,
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

# vytvoření hlavního okna
okno_app = ctk.CTk()
okno_app.title("Vyhledávač receptů")
okno_app.geometry("600x700")

# textové pole pro zadání ingrediencí
pole = ctk.CTkEntry(okno_app, width=400, placeholder_text="Zadej ingredience (odděl čárkou)")
pole.pack(pady=20)

# textová oblast pro zobrazení výsledků - nelze editovat
vysledky = ctk.CTkTextbox(okno_app, width=500, height=400, state="disabled")
vysledky.pack(pady=10)

# funkce se spustí po kliknutí na tlačítko
def po_kliknuti():
    ingredience = pole.get()
    # kontrola jestli uživatel zadal ingredience
    if not ingredience:
        vysledky.configure(state="normal")
        vysledky.insert("end", "Zadej prosím ingredience!\n")
        vysledky.configure(state="disabled")
        return
    recepty = hledej_recepty(ingredience)
    # povolení zápisu, smazání starých výsledků
    vysledky.configure(state="normal")
    vysledky.delete("1.0", "end")
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
    # zakázání editace
    vysledky.configure(state="disabled")

# tlačítko pro spuštění hledání
tlacitko = ctk.CTkButton(okno_app, text="Hledat", command=po_kliknuti)
tlacitko.pack(pady=10)

# spuštění okna
okno_app.mainloop()