import pygame.font

class Button:
    def __init__(self, ai_game, msg):
        #Initializing the button atributes
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        #Defining button properties
        self.width, self.height = 200, 50
        self.button_color = (200, 80, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        #Creating a rectangle and centering it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        #generating a text image and putting it inside the button on the center of the screen
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        #Showing the empty button and then the message 
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        