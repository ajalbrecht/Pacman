from vector import Vector
import pygame as pg
from pygame.sprite import Sprite, Group
from timer import Timer
import settings
import pygame.locals
from sys import exit

class Ghost(Sprite):
    Ghost_images = [pg.transform.rotozoom(pg.image.load(f'images/red-ghost.png'), 0, 1.0)]
    
    def __init__(self):
        self.name = settings.GHOST
        self.speed = 100
        self.image = pg.image.load('images/red-ghost.png')

    def update(self):	
        self.render()
        
    def render(self):
    
        pg.image.load('images/red-ghost.png')

