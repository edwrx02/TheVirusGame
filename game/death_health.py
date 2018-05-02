'''
Created on Jun 7, 2015

@author: Edwin
'''
import pygame

class Dead_Health(pygame.sprite.Sprite):
    """ This class creates the death health bar for the player"""
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load("Dead_Healthbar.png")
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x