import pygame
from pygame.sprite import Sprite
import time

class Alien(Sprite):
    #Class for a singular alien in a fleet
    
    def __init__(self, ai_game):
        #Initializing the alien and identifying its position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #Loading the alien image and defining its rect property
        self.image = pygame.image.load("python_crash_course/space_invaders/images/alien.bmp")
        self.rect = self.image.get_rect()
        
        #Placing a new alien in the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Storing the accurate horizontal placement of the alien
        self.x = float(self.rect.x)
    
    def update(self):
        
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
    
    def check_edges(self):
        #Returns true if an alien hits one of the edges
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        