import pygame
import sys
from settings import Settings

class AlienInvasion:
    # main class used for managing the game resources and how the game works
    def __init__(self) -> None:
        # initialize game and its resources.
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
    def run_game(self):
        # starting the main loop of the game
        while True:
            #waiting for keyboard or mouse input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #set background color of the screen
            self.screen.fill(self.settings.bg_color)
            
            #render the current screen and its elements
            pygame.display.flip()
            
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()