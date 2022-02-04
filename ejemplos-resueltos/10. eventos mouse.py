import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()

ventana = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Hola Mundo")

Mi_imagen = pygame.image.load("imagenes/wolf.png")
posX, posY = randint(10,300), randint(10,200)

velocidad = 2
direccion = 0
Blanco = (255,255,255)
while True:
    
    ventana.fill(Blanco)
    ventana.blit(Mi_imagen, (posX, posY))
    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key==K_LEFT:
                direccion = -1
            elif evento.key==K_RIGHT:
                direccion = 1
        if evento.type == pygame.KEYUP:
            if evento.key==K_LEFT:
                direccion = 0
            elif evento.key==K_RIGHT:
                direccion = 0
    
    posX += velocidad*direccion

    posX, posY = pygame.mouse.get_pos()
    #Centrar mouse en imagen
    posX -= 250
    posY -= 200

    pygame.display.update()