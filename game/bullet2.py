'''
Created on Jun 7, 2015

@author: Edwin
'''
import pygame


class Bullet2(pygame.sprite.Sprite):
    """ This class represents the bullet for the bad guy. """
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Gunfire_rockets_2.png")
        self.rect = self.image.get_rect()
    def update(self):
        """ Moves the bullet towards the hero. """
        self.rect.x -= 13 