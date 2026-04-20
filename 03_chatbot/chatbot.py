import os
from dotenv import load_dotenv
import groq
import customtkinter as ctk

# načtení API klíče z .env souboru
load_dotenv()
GROQ_KEY = os.getenv("API_KEY")