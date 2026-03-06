import requests
import os
from dotenv import load_dotenv

# Načtení API klíče z .env souboru
load_dotenv()
API_KEY = os.getenv("API_KEY")

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
    # Vrácení odpovědi jako Python slovník
    return odpoved.json()

# Funkce projde všechny recepty a vypíše je do terminálu
def vypis_recepty(recepty):
    # Smyčka projde každý recept v seznamu
    for recept in recepty:
        print(recept["title"])
        print(f"Použité ingredience: {recept['usedIngredientCount']}")
        print(f"Chybějící ingredience: {recept['missedIngredientCount']}")
        print("---")

# Hlavní část programu
ingredience = input("Zadej ingredience (odděl čárkou): ")
recepty = hledej_recepty(ingredience)
vypis_recepty(recepty)