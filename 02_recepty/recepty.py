import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.spoonacular.com/recipes/findByIngredients"

def hledej_recepty(ingredience):
    params = {
        "ingredients": ingredience,
        "number": 5,
        "apiKey": API_KEY
    }
    odpoved = requests.get(BASE_URL, params=params)
    return odpoved.json()

def vypis_recepty(recepty):
    for recept in recepty:
        print(recept["title"])
        print(f"Použité ingredience: {recept['usedIngredientCount']}")
        print(f"Chybějící ingredience: {recept['missedIngredientCount']}")
        print("---")

ingredience = input("Zadej ingredience (odděl čárkou): ")
recepty = hledej_recepty(ingredience)
vypis_recepty(recepty)