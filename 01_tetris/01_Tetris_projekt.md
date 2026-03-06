# Tetris

## Popis a cíl projektu
Chci vytvořit hru Tetris v Pythonu. Je to hra pro jednoho hráče kde padají bloky a hráč je skládá do řad.

## Funkcionalita programu
Program zatím umí otevřít herní okno s mřížkou, vykreslovat padající blok který jde ovládat šipkami, bloky se stackují na sobě a po dopadu se spawnuje nový blok.

Ještě chci přidat různé tvary bloků (L, T, S...).

## Technická část

**Použité knihovny:**
- `pygame` — používám ho na vykreslování okna, mřížky a bloků, taky na obsluhu klávesnice a časovač
- `sys` — slouží k zavření programu

**Jak to funguje:**
- `dopadle_bloky` je list kde ukládám pozice všech bloků které už dopadly, jako dvojice (x, y)
- blok nepadá každý snímek ale každých 500ms — řeším to pomocí `pygame.time.get_ticks()`
- před každým posunem dolů kontroluji jestli pod blokem není jiný blok — `(blok_x, blok_y + 1) not in dopadle_bloky`
- funkce `mrizka()` kreslí mřížku pomocí dvou vnořených cyklů `for`
- funkce `nakresli_blok()` a `nakresli_dopadle()` kreslí bloky na obrazovku

## Jak spustit program

1. Nainstaluj pygame:
```
pip install pygame
```
2. Spusť soubor:
```
python tetris.py
```
3. Ovládání:
   - šipka doleva / doprava — pohyb bloku
   - šipka dolů — rychlejší pád
   - zavření křížkem nebo Alt+F4