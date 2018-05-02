import pygame


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("Gunfire_rockets.png")

        self.rect = self.image.get_rect()
        effect = pygame.mixer.Sound('Laser_Blasts.wav')
        effect.set_volume(0.2)
        effect.play()
    def update(self):
        """ Move the bullet towards the hero. """
        self.rect.x += 8 
