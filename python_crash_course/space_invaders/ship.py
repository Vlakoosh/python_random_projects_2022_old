import pygame

class Ship:
    #class for managing the ship in the alien invasion game
    
    def __init__(self, ai_game) -> None:
        #initialization and initial position
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #loading the ship image and setting its rectangle
        self.image = pygame.image.load('python_crash_course/space_invaders/images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #every new space ship is placed on the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        #float variable allowing for a more accurate value of ship's position if parts of a pixel are used
        self.x = float(self.rect.x)
        
        #miscellaneous variables
        self.moving_right = False
        self.moving_left = False
        
        
    def blitme(self):
        #showing the space ship in its actual position
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        #updating the position of the ship based on the direction of movement
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x