# Dashboard

## Popis a cíl projektu
Osobní dashboard který zobrazuje aktuální čas, počasí v Třinci, české zprávy a obsahuje poznámkový blok. Vše na jedné obrazovce pro rychlý přehled.

## Funkcionalita programu
- Zobrazení aktuálního času (aktualizuje se každou sekundu)
- Zobrazení aktuálního počasí v Třinci
- České zprávy z RSS feedu
- Poznámkový blok s možností uložení a smazání
- Tmavý režim

## Technická část
**Knihovny:**
- `requests` — odesílání HTTP dotazů na API
- `python-dotenv` — načítání API klíče z `.env` souboru
- `customtkinter` — moderní grafické rozhraní
- `datetime` — práce s aktuálním časem
- `xml.etree.ElementTree` — parsování RSS feedu zpráv

**API:**
- Weatherstack API — aktuální počasí podle města
- Novinky.cz RSS feed — aktuální české zprávy

**Algoritmy a struktura:**
- Funkce `ziskej_pocasi()` — dotaz na Weatherstack API, vrátí teplotu a popis počasí
- Funkce `ziskej_zpravy()` — stáhne RSS feed a parsuje XML, vrátí seznam nadpisů
- Funkce `uloz_poznamky()` — zapíše text do souboru `poznamky.txt`
- Funkce `nacti_poznamky()` — načte text ze souboru `poznamky.txt`
- Funkce `aktualizuj_cas()` — každou sekundu aktualizuje čas pomocí `okno_app.after()`
- Ošetření chyb pomocí `try/except`

## User Guide
1. Nainstaluj potřebné knihovny: `pip install requests python-dotenv customtkinter`
2. Vytvoř soubor `.env` ve složce projektu a vlož tam:
3. Spusť program: `python dashboard.py`
4. Dashboard zobrazí čas, počasí a zprávy automaticky
5. Do poznámkového bloku piš co chceš
6. Klikni **Uložit** pro uložení poznámek
7. Klikni **Smazat** pro vymazání poznámek
