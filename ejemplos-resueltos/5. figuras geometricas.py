import pygame,sys
from pygame.locals import *

pygame.init()

ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hola Mundo")

#ventana, color, centro circulo, tamaño radio
pygame.draw.circle(ventana, (80,70,120), (80,90), 50)

#ventana, color, esquina superior izquierda y esquina inferior derecha
pygame.draw.rect(ventana, (130,70,70), (0,0,200,50))

#ventana, color, puntos del poligono (es un pentagono)
pygame.draw.polygon(ventana, (90,180,70), ((140,0),(291,106),(237,277),(56,277),(0,106)))

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()