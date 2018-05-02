'''
Created on May 27, 2015

@author: Edwin
'''
import pygame


class Boom(pygame.sprite.Sprite):
    """Creates the boom image"""
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("Boom_explode.png")
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
    def update(self):
        """ Moves the image """
        self.rect.x -=4 