import pygame.font

class Scoreboard:
    #Class for managing the scoreboard for the alien invasion game
    
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        #Font settings for scores
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        
        #Getting initial score images ready
        self.prep_score()
        self.prep_level()
    
    def prep_score(self):
        #Converting score value to a pygame image
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        #Showing the score in top right corner of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_level(self):
        level_str = f"Level: {str(self.stats.level)}"
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        
        #show level number
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def show_score(self):
        #Showing the score on the screen
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.level_image,self.level_rect)