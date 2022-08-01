import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    #Class for a singular alien in a fleet
    
    def __init__(self, ai_game):
        #Initializing the alien and identifying its position
        super().__init__()
        self.screen = ai_game.screen
        
        #Loading the alien image and defining its rect property
        self.image = pygame.image.load("python_crash_course/space_invaders/images/alien.bmp")
        self.rect = self.image.get_rect()
        
        #Placing a new alien in the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Storing the accurate horizontal placement of the alien
        self.x = float(self.rect.x)
        