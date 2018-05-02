'''
Created on May 16, 2015

@author: Edwin
'''
import pygame

class Wall(pygame.sprite.Sprite):
    """This creates the wall that's around the screen"""
 
    def __init__(self, x, y, width, height, color):
        """ All the parameters needed to create the wall"""
 
        # Call the parent's constructor
        super().__init__()
 
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x