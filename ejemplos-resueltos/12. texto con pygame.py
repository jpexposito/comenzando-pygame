import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()

ventana = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Hola Mundo")

#None: se sustituye por la direccion de una fuente
miFuente = pygame.font.Font(None,30)
#texto, ?, colorletra, colorfondo
miTexto = miFuente.render("Prueba Fuente",0,(200,60,80),(255,255,255))

miFuente2 = pygame.font.SysFont("Arial",30)
miTexto2 = miFuente2.render("Prueba Fuente 2",0,(200,60,80),(255,255,255))

while True:
    
 
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    
    ventana.blit(miTexto, (100,100))
    ventana.blit(miTexto2, (100,200))
    pygame.display.update()