# AI Chatbot

## Popis a cíl projektu
Grafická chatovací aplikace která umožňuje konverzaci s umělou inteligencí. Uživatel píše zprávy do textového pole a AI odpovídá v reálném čase. Aplikace si pamatuje celou historii konverzace.

## Funkcionalita programu
- Grafické okno s chatovací oblastí
- Textové pole pro psaní zpráv
- Odesílání zpráv stiskem Enter
- AI odpovídá česky a přátelsky
- Paměť konverzace — AI si pamatuje celý rozhovor

## Technická část
**Knihovny:**
- `groq` — komunikace s Groq AI API
- `python-dotenv` — načítání API klíče z `.env` souboru
- `customtkinter` — moderní grafické rozhraní

**API:**
- Groq API — AI model `llama3-8b-8192`

**Algoritmy a struktura:**
- Seznam `historie` — uchovává celý rozhovor ve formátu `role/content`
- Funkce `posli_zpravu()` — přidá zprávu do historie, pošle dotaz na API a vrátí odpověď
- Funkce `po_odeslani()` — spustí se po stisku Enter, zobrazí zprávu uživatele i odpověď AI
- Systémová zpráva (`role: system`) — nastavuje chování AI

## User Guide
1. Nainstaluj potřebné knihovny: `pip install groq python-dotenv customtkinter`