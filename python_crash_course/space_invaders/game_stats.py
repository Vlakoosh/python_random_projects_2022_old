class GameStats:
    #File for managing all the stats data in the alien invasion game
    
    def __init__(self, ai_game):
        #Initializing stats data
        self.settings = ai_game.settings
        self.reset_stats()
        
        self.game_active = True
    
    def reset_stats(self):
        #Initializing stats that might be changed during the playthrough
        self.ships_left = self.settings.ship_limit
    