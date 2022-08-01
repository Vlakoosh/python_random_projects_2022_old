class Settings:
    #Class meant for storing all the setting values for the game
    def __init__(self) -> None:
        #Initialize game settings
        
        #Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        #Ship settings
        self.ship_speed = 0.5