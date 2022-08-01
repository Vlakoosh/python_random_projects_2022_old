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
        
        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 6
        self.bullet_color = (20,20,20)
        self.max_bullets = 5