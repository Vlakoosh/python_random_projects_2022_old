class Settings:
    #Class meant for storing all the setting values for the game
    def __init__(self) -> None:
        #Initialize game settings
        
        #Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        #Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 400
        self.bullet_height = 15
        self.bullet_color = (20,20,20)
        self.max_bullets = 5
        self.piercing_bullets = True
        
        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        
        self.speedup_scale = 1.25
        self.points_scale = 1.50
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        self.bullet_speed = 2.0
        self.alien_speed = 1.0
        self.alien_points = 1000
        
        self.fleet_direction = 1
        
    def clamp(self, n, minn, maxn):
        return max(min(maxn, n), minn)
    
    def increase_speed(self):
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.bullet_speed = self.clamp(self.bullet_speed, 0, 5)
        self.alien_points = int(self.alien_points * self.points_scale)