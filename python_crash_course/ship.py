import pygame

class Ship:
    #class for managing the ship in the alien invasion game
    
    def __init__(self, ai_game) -> None:
        #initialization and initial position
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        #loading the ship image and setting its rectangle
        self.image - pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #every new space ship is placed on the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        #showing the space ship in its actual position
        self.screen.blit(self.image, self.rect)