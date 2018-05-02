'''
Created on Jun 7, 2015

@author: Edwin
'''
import pygame


class Boss_Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet for the boss guy. """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Gunfire_rockets_2.png")
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    def update(self):
        """ Moves the bullet towards the hero. """
        self.rect.x -= 20 