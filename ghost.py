from vector import Vector
import pygame as pg
from pygame.sprite import Sprite, Group
from timer import Timer
import settings
import pygame.locals
from sys import exit

class Ghost(Sprite):
    Ghost_images = [pg.transform.rotozoom(pg.image.load(f'images/red-ghost.png'), 0, 1.0)]
    
    def __init__(self,game):
        self.game = game
        self.screen = game
        #self.settings = game.settings
        self.speed = 100
        self.image = pg.image.load('images/red-ghost.png')

        self.rect = self.image.get_rect()
        #self.screen_rect = game.screen.get_rect()
       
        self.vel = Vector(200, 400)
   
    def render(self, screen):
        #self.update()
        self.rect = (200,400)
        #pg.image.load('images/red-ghost.png')
        self.screen.blit(self.image, (200, 400))

        
