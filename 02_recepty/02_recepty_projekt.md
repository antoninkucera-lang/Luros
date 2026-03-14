# Vyhledávač receptů

## Popis a cíl projektu
Aplikace která umožňuje vyhledávat recepty podle ingrediencí které máš doma. Zadáš suroviny a program ti ukáže co z toho můžeš uvařit. Určeno pro každodenní použití.

## Funkcionalita programu
- Grafické okno s textovým polem pro zadání ingrediencí
- Tlačítko pro spuštění vyhledávání
- Zobrazení výsledků přímo v okně (název receptu, použité a chybějící ingredience)

## Technická část
**Knihovny:**
- `requests` — odesílání HTTP dotazů na API
- `python-dotenv` — načítání API klíče z `.env` souboru
- `customtkinter` — moderní grafické rozhraní

**API:**
- Spoonacular API — databáze receptů, endpoint `findByIngredients`
- Parametry dotazu: ingredience, počet výsledků, API klíč

**Algoritmy a struktura:**
- Funkce `hledej_recepty()` — sestaví parametry a odešle dotaz na API, vrátí JSON
- Funkce `po_kliknuti()` — spustí se po kliknutí na tlačítko, zavolá API a zobrazí výsledky v okně

## User Guide
1. Nainstaluj potřebné knihovny: `pip install requests python-dotenv customtkinter`
2. Vytvoř soubor `.env` ve složce projektu a vlož tam `API_KEY=tvůj_klíč`
3. Spusť program: `python recepty.py`
4. Do textového pole zadej ingredience oddělené čárkou (např. `chicken, rice, tomato`)
5. Klikni na tlačítko **Hledat**
6. Výsledky se zobrazí v okně níže