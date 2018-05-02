'''
Created on Jun 7, 2015

@author: Edwin
'''
import pygame

class The_Boss(pygame.sprite.Sprite):
    """ This class creates the boss"""
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("Virus_boss.png")

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

