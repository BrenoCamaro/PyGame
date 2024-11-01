#Módulos do pygame
import pygame, sys
from pygame.locals import *
import random

#Meus módulos
import Jogador

pygame.init()

#Predefinição de cores
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Configurações da tela
TELA_LARGURA = 600
TELA_ALTURA = 600
TELA = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption("Protótipo")
TELA.fill(WHITE)

#FPS
FPS = 60
FramePerSec = pygame.time.Clock()


J1 = Jogador.Jogador()
#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        TELA.fill(WHITE) #Remove um estrano rastro deixado pela imagem dos bonecos
        J1.movimento()
        J1.desenho(TELA)

    pygame.display.update()
    FramePerSec.tick(FPS)

