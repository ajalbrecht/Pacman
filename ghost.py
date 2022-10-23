from vector import Vector
import pygame as pg
from pygame.sprite import Sprite, Group
from timer import Timer
import settings
import pygame.locals
from sys import exit

class Ghost(Sprite):
    def __init__(self,game):
        self.game = game
        self.screen = game
        self.Blinky_location = (200, 160)
        self.image__01_location = (220, 160)
        self.image__02_location = (240, 160)
        self.image__03_location = (260, 160) 
        #self.settings = game.settings
        #self.speed = 100
        self.Blinky = pg.image.load('images/red-ghost.png')
        self.image__01 = pg.image.load('images/pink-ghost.png')
        self.image__02 = pg.image.load('images/blue-ghost.png')
        self.image__03 = pg.image.load('images/orange-ghost.png')

        self.rect = self.Blinky.get_rect()
        self.rect = self.image__01.get_rect()
        self.rect = self.image__02.get_rect()
        self.rect = self.image__03.get_rect()
        #self.screen_rect = game.screen.get_rect()
       
   
    def render(self, screen, x , y):
        self.screen.blit(self.Blinky, self.Blinky_location)
        self.screen.blit(self.image__01, self.image__01_location)
        self.screen.blit(self.image__02, self.image__02_location)
        self.screen.blit(self.image__03, self.image__03_location)

    # def checkcollison(self):
    #     collisions = pygame.sprite.spritecollide(self, self.pacman)  
    #     if collisions:
    #         for pacman in collisions:
    #             pacman.hit()

class Blinky(Ghost):
    def __init__(self,game):
        Ghost.__init__(self, game)
        self.render()
        

        
