import pygame


class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
    change_x = 0
    change_y = 0
 
    def __init__(self, x, y):
        """ Set up the player on creation. """
        super().__init__()
        self.image = pygame.image.load("Ship_Long2.png")
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y
        
    def update(self):
        """ Find a new position for the player """

        self.rect.x += self.change_x  
        
        """Checks to see if the player hits the wall"""        
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        self.rect.y += self.change_y        
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom