import pygame
import sys

class AlienInvasion:
    # main class used for managing the game resources and how the game works
    def __init__(self) -> None:
        # initialize game and its resources.
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
    def run_game(self):
        # starting the main loop of the game
        while True:
            #waiting for keyboard or mouse input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            pygame.display.flip()
            
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()