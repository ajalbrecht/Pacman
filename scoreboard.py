import pygame.font

class Scoreboard():
    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

# Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

# Prepare the initial score image.
        self.prep_score()

    def prep_score(self):

        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
        self.settings.bg_color)

    # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.bottom = 590

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        print("show score is being called atm")