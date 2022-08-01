import pygame
import sys
from settings import Settings
from ship import Ship

class AlienInvasion:
    # main class used for managing the game resources and how the game works
    def __init__(self) -> None:
        # initialize game and its resources.
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        
    def run_game(self):
        # starting the main loop of the game
        while True:
            #check for certain input events
            self._check_events()
            #update the ship position
            self.ship.update()
            #update the screen
            self._update_screen()
            
            
    def _check_events(self):
        #waiting for keyboard or mouse input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #move the ship to the right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    #move the ship to the left
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    #stop moving the ship to the right
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    #stop moving the ship to the left
                    self.ship.moving_left = False
    
    def _update_screen(self):
        #set background color of the screen
        self.screen.fill(self.settings.bg_color)
        #render the ship on top of the background
        self.ship.blitme()
        #render the current screen and its elements
        pygame.display.flip()
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()