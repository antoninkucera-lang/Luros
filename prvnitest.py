import pygame 
import sys 

pygame.init()

#nastavení okna
okno = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Tetris test")

#rizeni casu
hodiny = pygame.time.Clock()

#hlavní smyčka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #vyplnění pozadí
    okno.fill((0, 0, 0))
    pygame.display.flip
    hodiny.tick(60)
    

