import pygame
import pygame.locals
import settings 
from pac import Pacman
from board import Graph
from gamestats import GameStats
from button import Button
import game_functions as gf
from ghost import Ghost
from sound import Sound
from scoreboard import Scoreboard
import sys

class GameController(object):
    def __init__(self):
        pygame.init()
        self.stats = GameStats(settings)
        self.settings = settings
        self.screen = pygame.display.set_mode(settings.SCREENSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()
        self.graph = 0
        self.sound = Sound()
        self.x=0
        self.y =0
        self.sb = Scoreboard(self.settings, self.screen, self.stats)

        self.play_button = Button(self.settings, self.screen, "Start Game")
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

    def setBackground(self):
        self.background = pygame.surface.Surface(settings.SCREENSIZE).convert()
        self.background.fill(settings.BLACK)

    def startGame(self):
        self.setBackground()
        self.pacman = Pacman(game= self)
        self.ghost = Ghost(self.screen)
        self.sound = Sound()
        # testing game board commands
        self.graph = Graph(self.screen, self.pacman, self.sound, self.ghost, self.stats, self.sb)
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
                #self.ghost.update()
                gf.check_events(settings=self.settings, stats=self.stats, play_button=self.play_button)
                self.sb.show_score()
                pygame.display.flip()

                

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.pacman.render(screen= self.screen)
        self.ghost.render(self.screen,self.x,self.y)
        self.graph.render()
        self.pacman.render_lives()
        pygame.display.flip()
        pygame.display.update()

    def reset(self):
        self.pacman.reset()
        self.graph.is_empty()

    def game_over(self):
        print("All lives have been lost")

        # self.sound.Die()


if __name__ == "__main__":
    game = GameController()
    game.startGame()
    while True:
        game.update()