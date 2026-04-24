import os
from dotenv import load_dotenv
from groq import Groq
import customtkinter as ctk

# načtení API klíče z .env souboru
load_dotenv()
GROQ_KEY = os.getenv("GROQ_KEY")

# vytvoření klienta pro komunikaci s Groq API
klient = Groq(api_key=GROQ_KEY)