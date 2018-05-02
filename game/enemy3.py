'''
Created on May 25, 2015

@author: Edwin
'''
import pygame

class Enemy3(pygame.sprite.Sprite):
    """ This is the bouncing enemy """
    up = True;    
    # -- Methods
    def __init__(self):
        """ This class represents the enemy3 for stage1. """
        super().__init__()
        self.image = pygame.image.load("Virus_jumper.png") 
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
 
    def update(self):
        """ The bouncing movement of the bad guy. """
        
        if self.rect.y < 300:
            Enemy3.up = False
        
        if self.rect.y > 700:
            Enemy3.up = True
        
        if Enemy3.up == True:
            self.rect.y -=8  # Does NOT draw the player two pixels down.
            self.rect.x -= 7
        
        if Enemy3.up == False:
            self.rect.y +=8  # Does NOT draw the player two pixels down.
            self.rect.x -= 7
 
   