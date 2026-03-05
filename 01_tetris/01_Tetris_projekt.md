# Tetris

## Popis a cíl projektu
Chci vytvořit hru Tetris v Pythonu. Je to hra pro jednoho hráče kde padají bloky a hráč je skládá do řad. Když se řada zaplní celá, zmizí a hráč dostane body. Hra končí když bloky dosáhnou vrchu obrazovky.

## Funkcionalita programu
Program zatím umí:
- otevřít herní okno
- vykreslit mřížku 10 x 20 bloků

Plánuji přidat:
- padající bloky
- ovládání klávesnicí
- mazání řad
- skóre

## Technická část

**Použité knihovny:**
- `pygame` — slouží k vykreslení okna a mřížky, zatím jsem se naučil základy
- `sys` — použito pro zavření programu

**Co jsem zatím naprogramoval:**
- hlavní smyčka která běží pořád dokola a překresluje obrazovku 60x za sekundu
- funkce `mrizka()` která pomocí cyklu vykreslí mřížku ze čtverečků

## Jak spustit program

1. Nainstaluj knihovnu pygame:
   pip install pygame
2. Spusť soubor tetris.py:
   python tetris.py
3. Hru zavřeš klávesou Alt+F4 nebo křížkem v rohu okna.