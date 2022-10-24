import pygame.font

class Button():

    def __init__(self, settings, screen, msg, stats):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 325, 25
        self.stats = stats

        self.button_color = (0, 0, 0)
        self.text_color = (210, 210, 210)
        self.text_color_hs = (255, 253, 165)
        self.font = pygame.font.Font('fonts/Joystix.TTF', 50)

        self.textfont = pygame.font.Font('fonts/Joystix.TTF', 30)
        self.textfont1 = pygame.font.Font('fonts/Joystix.TTF', 25)

        #Load Images
        self.titleimage1 = pygame.transform.rotozoom(pygame.image.load("images/pacman_title.png"), 0, 0.1725)
        self.titleimage2 = pygame.transform.rotozoom(pygame.image.load("images/pac-man.png"), 0, 0.3)
        self.titleimage3 = pygame.transform.rotozoom(pygame.image.load("images/cherry.png"), 0, 0.3)
        self.titleimage4 = pygame.transform.rotozoom(pygame.image.load("images/4ghost.png"), 0, 0.5)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(75, 485, self.width, self.height)
    

        self.prep_msg(msg)
        self.hs_show(self)

    def hs_show(self, stats):
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color_hs)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.midtop = (395, 535)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.titleimage1, (5,-55))
        self.screen.blit(self.titleimage2, (15,300))
        self.screen.blit(self.titleimage3, (300,325))
        self.screen.blit(self.titleimage4, (85,115))

        self.text1 = self.textfont.render("CLYDE", 1, (219, 155,58))
        self.screen.blit(self.text1, (167.5, 100))

        self.text1 = self.textfont.render("BLiNKY", 1, (255,0,0))
        self.screen.blit(self.text1, (195, 315))

        self.text1 = self.textfont.render("iNKEY", 1, (58,219,214))
        self.screen.blit(self.text1, (40, 240))

        self.text1 = self.textfont.render("PiNKEY", 1, (255,174,231))
        self.screen.blit(self.text1, (340, 200))

        self.text1 = self.textfont1.render("Current High Score:", 1, (255,255,255))
        self.screen.blit(self.text1, (10, 550))

        self.screen.blit(self.high_score_image, self.high_score_rect)



