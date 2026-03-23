# Vyhledávač receptů

## Popis a cíl projektu
Aplikace která umožňuje vyhledávat recepty podle ingrediencí které máš doma. Zadáš suroviny a program ti ukáže co z toho můžeš uvařit. Určeno pro každodenní použití.

## Funkcionalita programu
- Grafické okno s textovým polem pro zadání ingrediencí
- Tlačítko pro spuštění vyhledávání
- Zobrazení výsledků přímo v okně (název receptu, použité a chybějící ingredience)
- Kliknutelný odkaz na každý recept
- Zobrazení aktuálního počasí v Třinci
- Kontrola prázdného vstupu s chybovou hláškou

## Technická část
**Knihovny:**
- `requests` — odesílání HTTP dotazů na API
- `python-dotenv` — načítání API klíčů z `.env` souboru
- `customtkinter` — moderní grafické rozhraní

**API:**
- Spoonacular API — databáze receptů, endpoint `findByIngredients`
- Weatherstack API — aktuální počasí podle města

**Algoritmy a struktura:**
- Funkce `hledej_recepty()` — sestaví parametry a odešle dotaz na API, vrátí JSON
- Funkce `ziskej_odkaz()` — druhý dotaz na API pro získání odkazu na recept podle ID
- Funkce `ziskej_pocasi()` — dotaz na Weatherstack API, vrátí teplotu a popis počasí
- Funkce `po_kliknuti()` — spustí se po kliknutí, smaže staré výsledky, zavolá API a zobrazí výsledky
- Ošetření chyb pomocí `try/except` — zachytí výpadek internetu i jiné chyby

## User Guide
1. Nainstaluj potřebné knihovny: `pip install requests python-dotenv customtkinter`
2. Vytvoř soubor `.env` ve složce projektu a vlož tam:
```
   API_KEY=tvůj_spoonacular_klíč
   WEATHER_KEY=tvůj_weatherstack_klíč
```
3. Spusť program: `python recepty.py`
4. Do textového pole zadej ingredience oddělené čárkou (např. `chicken, rice, tomato`)
5. Klikni na tlačítko **Hledat**
6. Výsledky se zobrazí v okně níže včetně odkazu na každý recept