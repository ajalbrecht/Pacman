import pygame
import pygame.locals
import settings 
from pac import Pacman
from board import Graph

class GameController(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.SCREENSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()
        # testing game board commands
        self.graph = Graph()
        #print(self.graph.SetCharacterLocation(3,(1,1)))

    def setBackground(self):
        self.background = pygame.surface.Surface(settings.SCREENSIZE).convert()
        self.background.fill(settings.BLACK)

    def startGame(self):
        self.setBackground()
        self.pacman = Pacman()

    def update(self):
        dt = self.clock.tick(30) / 1000.0
        self.checkEvents()
        self.render()
        self.pacman.update(dt)
    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.pacman.render(self.screen)
        pygame.display.update()


if __name__ == "__main__":
    game = GameController()
    game.startGame()
    while True:
        game.update()