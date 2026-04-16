# Vyhledávač počasí (WeatherApp) — **VE VÝVOJI**

## Popis a cíl projektu
Aplikace, která umožňuje sledovat aktuální počasí kdekoli na světě. Zadáš název města a program ti vytáhne data z internetu přes API. Aktuálně slouží jako testovací projekt pro práci s reálnými daty a moderním designem. **Stav: Rozpracováno, funkce se budou doplňovat.**

## Funkcionalita programu
- Grafické okno s textovým polem pro zadání názvu města
- Tlačítko pro spuštění vyhledávání (Aktualizace dat)
- Zobrazení hlavních údajů (Teplota, vlhkost a stručný popis počasí)
- Dynamické ikonky podle aktuálního stavu (slunce, mraky, déšť)
- Přepínač světlého a tmavého režimu (Dark/Light mode)
- Kontrola vstupu s chybovou hláškou (pokud město neexistuje nebo nejde internet)
- Zobrazení času poslední úspěšné aktualizace

## Technická část
**Knihovny:**
- `requests` — odesílání HTTP dotazů na API
- `python-dotenv` — bezpečné načítání API klíčů z `.env` souboru
- `customtkinter` — moderní grafické rozhraní
- `Pillow` — knihovna pro práci s obrázky ikon

**API:**
- OpenWeatherMap API — hlavní zdroj dat pro aktuální počasí

**Algoritmy a struktura:**
- Funkce `ziskej_pocasi()` — sestaví dotaz s API klíčem, pošle ho na server a vrátí JSON
- Funkce `aktualizuj_vzhled()` — vezme data z API a přepíše texty a ikonky v okně
- Funkce `prepni_rezim()` — mění barvy aplikace mezi Dark a Light módem
- Ošetření chyb pomocí `try/except` — zachytí výpadek internetu nebo špatné jméno města
- Ukládání klíče — použití `.env` souboru pro bezpečnost

## Status vývoje
1. Nainstaluj knihovny: `pip install requests python-dotenv customtkinter pillow`
2. Vytvoř soubor `.env` a vlož tam: `API_KEY=tve_id_z_openweathermap`
3. Spusť program: `python pocasi.py` (Zatím ve vývoji)