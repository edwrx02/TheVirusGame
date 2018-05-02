'''
Created on May 25, 2015

@author: Edwin
'''
import pygame

class Enemy3b(pygame.sprite.Sprite):
    """ This is the bouncing enemy 2nd stage """
    up = True;    
    def __init__(self):
        """ This class represents the enemy3 for stage2. """
        super().__init__()
        self.image = pygame.image.load("Virus_jumper.png") 
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
 
    def update(self):
        """ The bouncing movement of the bad guy. """
        
        if self.rect.y < 300:
            Enemy3b.up = False
        
        if self.rect.y > 700:
            Enemy3b.up = True
        
        if Enemy3b.up == True:
            self.rect.y -=11  
            self.rect.x -=10
        
        if Enemy3b.up == False:
            self.rect.y +=11  
            self.rect.x -=10