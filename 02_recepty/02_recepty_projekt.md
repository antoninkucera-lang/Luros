# Vyhledávač receptů

## Popis a cíl projektu
Aplikace která umožňuje vyhledávat recepty podle ingrediencí které máš doma. Zadáš suroviny a program ti ukáže co z toho můžeš uvařit. Určeno pro každodenní použití.

## Funkcionalita programu
- Grafické okno s textovým polem pro zadání ingrediencí
- Slider pro nastavení počtu receptů (1–15, výchozí hodnota 5)
- Tlačítko pro spuštění vyhledávání
- Výsledky seřazené podle nejlepší shody (nejméně chybějících ingrediencí nahoře)
- Zobrazení výsledků přímo v okně (název receptu, použité a chybějící ingredience, odkaz)
- Zobrazení aktuálního počasí v Třinci
- Přepínač světlého a tmavého režimu
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
- Funkce `po_kliknuti()` — spustí se po kliknutí, smaže staré výsledky, zavolá API, seřadí výsledky a zobrazí je
- Funkce `prepni_rezim()` — přepíná mezi světlým a tmavým režimem
- Řazení výsledků pomocí `sorted()` a `lambda` — recepty seřazeny podle počtu chybějících ingrediencí
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
5. Pomocí slideru nastav kolik receptů chceš zobrazit
6. Klikni na tlačítko **Hledat**
7. Výsledky se zobrazí seřazené podle nejlepší shody, každý recept obsahuje odkaz
8. Pomocí tlačítka vpravo dole můžeš přepnout světlý nebo tmavý režim