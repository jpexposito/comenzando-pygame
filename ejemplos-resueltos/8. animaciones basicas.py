import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()

ventana = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Hola Mundo")

Mi_imagen = pygame.image.load("imagenes/wolf.png")
posX, posY = randint(10,300), randint(10,200)

velocidad = 2
direccion = 1
Blanco = (255,255,255)
while True:
    
    ventana.fill(Blanco)
    ventana.blit(Mi_imagen, (posX, posY))
    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
            
    if posX>=400:
        direccion = -1
    elif posX<=0:
        direccion = 1

    posX+=velocidad*direccion
    pygame.display.update()