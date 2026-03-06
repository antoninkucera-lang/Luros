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

def mrizka():
    for i in range(sloupce):        # prochází každý sloupec
        for j in range(radky):      # prochází každý řádek
            # nakreslí obrys čtverečku na pozici i, j
            pygame.draw.rect(okno, (255, 255, 255), (i * Velikost_bloku, j * Velikost_bloku, Velikost_bloku, Velikost_bloku), 1)

#hlavní smyčka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #vyplnění pozadí
    okno.fill((0, 0, 0))
    mrizka()
    pygame.display.flip()
    hodiny.tick(60)


