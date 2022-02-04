import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()

ventana = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Hola Mundo")

rectangulo_dos = pygame.Rect(200,200,100,50)
posX, posY = randint(10,300), randint(10,200)

velocidad = 1
direccion = 1
Blanco = (255,255,255)

rectangulo = pygame.Rect(0,0,100,50)

while True:
    
    ventana.fill(Blanco)

    pygame.draw.rect(ventana,(50,70,70), rectangulo_dos)
    pygame.draw.rect(ventana, (180,70,70), rectangulo)

    rectangulo.left, rectangulo.top = pygame.mouse.get_pos()

    if rectangulo.colliderect(rectangulo_dos):
        velocidad = 0
        print("Colisiono")
    
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
    
    posX, posY = pygame.mouse.get_pos()
    #Centrar mouse en imagen
    posX -= 250
    posY -= 200

    if rectangulo_dos.left>=400 or rectangulo_dos.left<=0:
        direccion = direccion*-1

    rectangulo_dos.left += velocidad*direccion
    pygame.display.update()