from pyexpat.errors import XML_ERROR_XML_DECL
from vector import Vector
import pygame as pg
from pygame.sprite import Sprite, Group
from timer import Timer
import settings
import pygame.locals
from sys import exit
import board

class Ghost(Sprite):
    def __init__(self,game):
        self.game = game
        self.screen = game
        self.Blinky_location = (224, 96) # 266 128
        self.image__01_location = (192, 160) # 220 160
        self.image__02_location = (224, 160)
        self.image__03_location = (256, 160) 
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
        self.dying = self.dead = False

    def ghost_direction(self, type, xNew, yNew):
        if type == 0: 
            xOld = self.Blinky_location[0]
            yOld = self.Blinky_location[1]
            self.Blinky_location = (xNew + xOld, yNew + yOld)
        if type == 1: 
            xOld = self.image__01_location[0]
            yOld = self.image__01_location[1]
            self.image__01_location = (xNew + xOld, yNew + yOld)
        if type == 2: 
            xOld = self.image__02_location[0]
            yOld = self.image__02_location[1]
            self.image__02_location = (xNew + xOld, yNew + yOld)
        if type == 3: 
            xOld = self.image__03_location[0]
            yOld = self.image__03_location[1]
            self.image__03_location = (xNew + xOld, yNew + yOld)

    #def give_location(self, type):
     #   if type = 0: 
       
   
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

    def reset(self):
        self.Blinky_location = (200, 180)
        self.dying = self.dead = False

    def hit(self):
        if not self.dying:
            print("This was hit")
            self.dying = True
            self.reset()
class Blinky(Ghost):
    def __init__(self,game):
        Ghost.__init__(self, game)
        self.render()
        

        
