import pygame
import sys
import time

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

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
        
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
        self.play_button = Button(self, "Play")
        
    def run_game(self):
        # starting the main loop of the game
        while True:
            self._check_events()
            if self.stats.game_active:
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        #starting a new game after the button is pressed
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #reseting stats
            self.stats.reset_stats()
            self.stats.game_active = True
            
            #clearing bulleys and aliens
            self.aliens.empty()
            self.bullets.empty()
            
            #creating a new fleet and reseting the ship
            self._create_fleet()
            self.ship.center_ship()
            
            self.settings.initialize_dynamic_settings()
            
            pygame.mouse.set_visible(False)
    
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
        elif event.key == pygame.K_r:
            self._start_game()
    
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
        
        #Showing the play button when the game is not active
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        #put all of the bullets on the screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        #render the ship on top of the background
        self.ship.blitme()
        
        #display the scoreboard
        self.sb.show_score() 
        
        self._display_lives()
        
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
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, not self.settings.piercing_bullets, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            
        
        if not self.aliens:
            #removing existing bullets and creating a new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()
    
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
        
        #Checking collision between the ship and the aliens
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        #Checking if an alien reached the bottom of the screen
        self._check_aliens_bottom()
    
    def _display_lives(self):
        ship_width = self.ship.rect.width
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self)
            ship.rect.x = 10 + ship_width * ship_number
            ship.rect.y = 10
            ship.blitme()
            
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
    
    def _ship_hit(self):
        #Reaction to an alien hitting the ship
        
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            
            self.aliens.empty()
            self.bullets.empty()
            
            self._create_fleet()
            self.ship.center_ship()
            
            time.sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
    
    def _start_game(self):
        self.aliens.empty()
        self.bullets.empty()
            
        self._create_fleet()
        self.ship.center_ship()
        
        self.stats.game_active = True
        self.stats.reset_stats()

        self.settings.initialize_dynamic_settings()
        self.sb.prep_score()
        self.sb.prep_level()
        
    
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()