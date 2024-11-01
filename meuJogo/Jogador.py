import pygame, sys
from pygame.locals import *
import random

pygame.init()

# Configurações da tela
TELA_LARGURA = 600
TELA_ALTURA = 600

class Jogador(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()
        self.image = pygame.image.load("Jogador.png")
        self.rect = self.image.get_rect() 
        self.rect.center = (160, 520) 

    def movimento(self):
        teclaPressionada = pygame.key.get_pressed()
        if teclaPressionada[K_UP]:
            self.rect.move_ip(0, -5)

        if teclaPressionada[K_DOWN]:
            self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if teclaPressionada[K_LEFT]:
                self.rect.move_ip(-5, 0)

        if self.rect.right < TELA_LARGURA:
            if teclaPressionada[K_RIGHT]:
                self.rect.move_ip(5, 0) #(Horizontal, vertical)

    def desenho(self, surface):
        surface.blit(self.image, self.rect)
