import pygame.font

class Scoreboard():
    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats
        self.textfont = pygame.font.Font('fonts/Joystix.TTF', 30)

# Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('fonts/Joystix.TTF', 30)

# Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):

        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
        self.settings.bg_color)

    # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 5
        self.score_rect.bottom = 590

    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color,
        self.settings.bg_color_level)

    # Display the score at the top left of the screen
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left + 120
        self.level_rect.top = 0
    

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_high_score(self):
    
        self.high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(self.high_score)
        self.high_score_image = self.font.render(high_score_str, True,
        self.text_color, self.settings.bg_color)

        # Center the high score at the bottom middle of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx - 40
        self.high_score_rect.bottom = self.score_rect.bottom

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        self.text1 = self.textfont.render("LEVEL", 1, (255,255,255))
        self.screen.blit(self.text1, (0, 0))

        self.text1 = self.textfont.render("HS: ", 1, (255,255,255))
        self.screen.blit(self.text1, (95, 560))

        self.text1 = self.textfont.render("Score: ", 1, (255,255,255))
        self.screen.blit(self.text1, (275, 560))
        