import os
from dotenv import load_dotenv
from groq import Groq
import customtkinter as ctk

# načtení API klíče z .env souboru
load_dotenv()
GROQ_KEY = os.getenv("GROQ_KEY")

# vytvoření klienta pro komunikaci s Groq API
klient = Groq(api_key=GROQ_KEY)

# historie konverzace - uchovává celý rozhovor
historie = [
    {"role": "system", "content": "Jsi přátelský chatbot který mluví česky. Odpovídej stručně a přátelsky."}
]

# funkce pošle zprávu AI a vrátí odpověď
def posli_zpravu(zprava):
    # přidání zprávy uživatele do historie
    historie.append({"role": "user", "content": zprava})
    # odeslání celé historie na Groq API
    odpoved = klient.chat.completions.create(
        model="llama3-8b-8192",
        messages=historie
    )