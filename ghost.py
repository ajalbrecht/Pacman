from vector import Vector
import pygame as pg
from pygame.sprite import Sprite, Group
from timer import Timer
import settings
import pygame.locals
from sys import exit

class Ghost(Sprite):
    ghost_images = [pg.transform.rotozoom(pg.image.load(f'images/red-ghost.png'), 0, 1.0)]
    ghost_images = [pg.transform.rotozoom(pg.image.load(f'images/pink-ghost.png'), 0, 1.0)]
    ghost_images = [pg.transform.rotozoom(pg.image.load(f'images/orange-ghost.png'), 0, 1.0)]
    ghost_images = [pg.transform.rotozoom(pg.image.load(f'images/blue-ghost.png'), 0, 1.0)]
    
    def __init__(self,game):
        self.game = game
        self.screen = game
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
        self.screen.blit(self.Blinky, (200, 160))
        self.screen.blit(self.image__01, (220, 160))
        self.screen.blit(self.image__02, (240, 160))
        self.screen.blit(self.image__03, (260, 160))

class Blinky(Ghost):
    def __init__(self,game):
        Ghost.__init__(self, game)
        self.render()
        

        
