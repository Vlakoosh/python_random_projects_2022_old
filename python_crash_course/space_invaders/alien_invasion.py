from cmath import rect
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
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
    def run_game(self):
        # starting the main loop of the game
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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
        
        #draw aliens on the screen
        self.aliens.draw(self.screen)
        
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
        self._check_bullet_alien_collision()
    
    def _check_bullet_alien_collision(self):
        #dictionary of collisions: list of bullets, list of aliens, Remove bullet on collision, Remove alien on collision
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            #removing existing bullets and creating a new fleet
            self.bullets.empty()
            self._create_fleet()
    
    def _create_fleet(self):
        #Creating an alien
        alien = Alien(self)
        
        #Checking for the number of aliens in a row
        alien_width = alien.rect.width
        
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_of_aliens_x = available_space_x // (2 * alien_width)
        
        #checking for the number of rows of aliens
        alien_height = alien.rect.height
        ship_height = self.ship.rect.height
        
        available_space_y = self.settings.screen_height - (4 * alien_height) - ship_height
        number_of_aliens_y = available_space_y // (2 * alien_height)
        
        #Creating the first row of aliens
        for row_number in range(number_of_aliens_y):
            for alien_number in range(number_of_aliens_x):
                self._create_alien(alien_number, row_number)
    
    def _create_alien(self, alien_number, row_number):
        #Creating an alien and putting it in a row
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    
    def _update_aliens(self):
        #updating the position of all the aliens in the fleet
        self._check_fleet_edges()
        self.aliens.update()
    
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        #Moving the whole fleet down and changing its direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
            

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()