'''
Created on Jun 7, 2015

@author: Edwin
'''
import pygame


class Health_4(pygame.sprite.Sprite):
    """ This class creates the 4 hit left health bar"""
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load("4_Healthbar.png")
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x