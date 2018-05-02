'''
Created on May 17, 2015

@author: Edwin
'''
import pygame
class Enemy2b(pygame.sprite.Sprite):
    """ This class represents the enemy2 for stage2. """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("Virus_hanger_med.png")
        self.rect = self.image.get_rect()
    
    def update(self):
        """Moves the enemy to the left"""
        self.rect.x -= 7
    def falling(self, x):
        """Moves the enemy to the down"""
        self.rect.y += x 