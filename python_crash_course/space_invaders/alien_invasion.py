import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    # main class used for managing the game resources and how the game works
    def __init__(self) -> None:
        # initialize game and its resources.
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        # starting the main loop of the game
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            
            
    def _check_events(self):
        #waiting for keyboard or mouse input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            #move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #move the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_DOWN:
            #move the ship down
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            #move the ship up
            self.ship.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            #stop moving the ship to the right
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            #stop moving the ship to the left
            self.ship.moving_left = False
        elif event.key == pygame.K_DOWN:
            #stop moving the ship down
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            #stop moving the ship up
            self.ship.moving_up = False
    
    def _update_screen(self):
        #set background color of the screen
        self.screen.fill(self.settings.bg_color)
        #put all of the bullets on the screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #render the ship on top of the background
        self.ship.blitme()
        #render the current screen and its elements
        pygame.display.flip()
    
    def _fire_bullet(self):
        #creating a new bullet and adding it to the list
        if len(self.bullets) < self.settings.max_bullets:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        
    
    def _update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self.bullets.update()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()