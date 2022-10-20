import pygame.font

class Button():

    def __init__(self, settings, screen, msg):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 325, 25

        self.button_color = (0, 0, 0)
        self.text_color = (210, 210, 210)
        self.font = pygame.font.Font('fonts/Joystix.TTF', 50)

        self.textfont = pygame.font.Font('fonts/Joystix.TTF', 50)

        #Load Images
        self.titleimage1 = pygame.transform.rotozoom(pygame.image.load("images/pacman_title.png"), 0, 0.1725)
        self.titleimage2 = pygame.transform.rotozoom(pygame.image.load("images/pac-man.png"), 0, 0.3)
        self.titleimage3 = pygame.transform.rotozoom(pygame.image.load("images/cherry.png"), 0, 0.3)
        self.titleimage4 = pygame.transform.rotozoom(pygame.image.load("images/4ghost.png"), 0, 0.3)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(55, 450, self.width, self.height)
    

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.titleimage1, (0,0))
        self.screen.blit(self.titleimage2, (20,200))
        self.screen.blit(self.titleimage3, (115,200))
        self.screen.blit(self.titleimage4, (250,200))

        #self.text1 = self.textfont.render("Start Game", 1, (210,210,210))
        #self.screen.blit(self.text1, (100, 100))