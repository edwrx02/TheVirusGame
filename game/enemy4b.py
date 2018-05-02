'''
Created on Jun 6, 2015

@author: Edwin
'''
import pygame

class Enemy4b(pygame.sprite.Sprite):
    """ This class represents the enemy4 for stage2. """
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("Virus_badass.png")

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def update(self):
        """Moves the enemy to the left"""
        self.rect.x -= 15