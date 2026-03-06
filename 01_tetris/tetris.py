import pygame 
import sys 

#nastavení velikosti bloku, sloupců a řádků
Velikost_bloku = 40
sloupce = 10
radky = 15

sirka = sloupce * Velikost_bloku
vyska = radky * Velikost_bloku


pygame.init()

#nastavení okna
okno = pygame.display.set_mode((sirka, vyska))
pygame.display.set_caption("Tetris test")

#rizeni casu
hodiny = pygame.time.Clock()

# pozice bloku na mřížce
blok_x = 5  # sloupec (uprostřed)
blok_y = 0  # řádek (nahoře)

cas_posledniho_padu = pygame.time.get_ticks()
rychlost_padu = 500  # blok spadne o jedno pole každých 500ms

def mrizka():
    for i in range(sloupce):        # prochází každý sloupec
        for j in range(radky):      # prochází každý řádek
            # nakreslí obrys čtverečku na pozici i, j
            pygame.draw.rect(okno, (255, 255, 255), (i * Velikost_bloku, j * Velikost_bloku, Velikost_bloku, Velikost_bloku), 1)

def nakresli_blok(x, y):
    # převede pozici na mřížce na pixely a nakreslí čtvereček
    pygame.draw.rect(okno, (0, 255, 0), (x * Velikost_bloku, y * Velikost_bloku, Velikost_bloku, Velikost_bloku))

#hlavní smyčka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #vyplnění pozadí
  
    ted = pygame.time.get_ticks()
    if ted - cas_posledniho_padu > rychlost_padu:
        if blok_y + 1 < radky:
            blok_y += 1
        cas_posledniho_padu = ted

    okno.fill((0, 0, 0))
    mrizka()
    nakresli_blok(blok_x, blok_y)
    pygame.display.flip()
    hodiny.tick(60)


