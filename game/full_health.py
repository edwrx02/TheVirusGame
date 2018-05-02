'''
Created on Jun 7, 2015

@author: Edwin
'''
import pygame


class Full_Health(pygame.sprite.Sprite):
    """ This class creates the full health bar"""
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load("Full_Healthbar.png")
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
