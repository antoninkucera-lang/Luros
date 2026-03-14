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
    # Odeslání dotazu na API
    odpoved = requests.get(BASE_URL, params=params)
    if odpoved.status_code != 200:
        print(f"Chyba API: {odpoved.status_code} - {odpoved.text}")
        return []
    # Vrácení odpovědi jako Python slovník
    return odpoved.json()

# Funkce projde všechny recepty a vypíše je do terminálu
def vypis_recepty(recepty):
    if not recepty:
        print("Žádné recepty nenalezeny.")
        return
    # Smyčka projde každý recept v seznamu
    for recept in recepty:
        print(recept["title"])
        print(f"Použité ingredience: {recept['usedIngredientCount']}")
        print(f"Chybějící ingredience: {recept['missedIngredientCount']}")
        print("---")

# vytvoření hlavního okna
okno_app = ctk.CTk()
okno_app.title("Vyhledávač receptů")
okno_app.geometry("600x700")

# textové pole pro zadání ingrediencí
pole = ctk.CTkEntry(okno_app, width=400, placeholder_text="Zadej ingredience (odděl čárkou)")
pole.pack(pady=20)

# textová oblast pro zobrazení výsledků
vysledky = ctk.CTkTextbox(okno_app, width=500, height=400)
vysledky.pack(pady=10)

# funkce se spustí po kliknutí na tlačítko
def po_kliknuti():
    ingredience = pole.get()
    recepty = hledej_recepty(ingredience)
    vysledky.delete("1.0", "end")
    for recept in recepty:
        vysledky.insert("end", f"{recept['title']}\n")
        vysledky.insert("end", f"Použité ingredience: {recept['usedIngredientCount']}\n")
        vysledky.insert("end", f"Chybějící ingredience: {recept['missedIngredientCount']}\n")
        vysledky.insert("end", "---\n")

# tlačítko pro spuštění hledání
tlacitko = ctk.CTkButton(okno_app, text="Hledat", command=po_kliknuti)
tlacitko.pack(pady=10)

# spuštění okna
okno_app.mainloop()