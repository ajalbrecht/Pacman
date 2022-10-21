import pygame
import pygame.locals
import settings 
from pac import Pacman
from board import Graph
from gamestats import GameStats
from button import Button
import game_functions as gf

class GameController(object):
    def __init__(self):
        pygame.init()
        self.stats = GameStats(settings)
        self.settings = settings
        self.screen = pygame.display.set_mode(settings.SCREENSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()
        self.graph = 0

        self.play_button = Button(self.settings, self.screen, "Start Game")
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

    def setBackground(self):
        self.background = pygame.surface.Surface(settings.SCREENSIZE).convert()
        self.background.fill(settings.BLACK)

    def startGame(self):
        self.setBackground()
        self.pacman = Pacman()
        # testing game board commands
        self.graph = Graph(self.screen, self.pacman)
        #print(self.graph.SetCharacterLocation(3,2,1))

    def update(self):
        while self.stats.game_active == False:
            self.screen.fill((0,0,0))
            self.screen.blit(self.background,(0,0))
            self.play_button.draw_button()
            gf.check_events(settings=self.settings, stats=self.stats, play_button=self.play_button)
            pygame.display.flip()

        while self.stats.game_active == True:
                dt = self.clock.tick(30) / 1000.0
                self.render()
                self.pacman.update(dt)
                gf.check_events(settings=self.settings, stats=self.stats, play_button=self.play_button)

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.pacman.render(self.screen)
        self.graph.render()
        pygame.display.update()


if __name__ == "__main__":
    game = GameController()
    game.startGame()
    while True:
        game.update()