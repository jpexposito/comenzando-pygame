import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()

ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hola Mundo")


miFuente = pygame.font.SysFont("Arial",30)
miTexto = miFuente.render("Tiempo: 0",0,(200,60,80))

aux = 1
while True:
     
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    
    Tiempo = pygame.time.get_ticks()//1000
    if aux==Tiempo:
        aux+=1     
        miTexto = miFuente.render("Tiempo: "+str(Tiempo),0,(200,60,80))   

    ventana.fill((255,255,255))    
    ventana.blit(miTexto, (100,100))
    pygame.display.update()