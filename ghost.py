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
        self.Pinky_location = (192, 160) # 220 160
        self.Inky_location = (224, 160)
        self.Clyde_location = (256, 160) 
        #self.settings = game.settings
        #self.speed = 100
        self.Blinky = pg.image.load('images/red-ghost.png')
        self.Pinky = pg.image.load('images/pink-ghost.png')
        self.Inky = pg.image.load('images/blue-ghost.png')
        self.Clyde = pg.image.load('images/orange-ghost.png')

        self.rect = self.Blinky.get_rect()
        self.rect = self.Pinky.get_rect()
        self.rect = self.Inky.get_rect()
        self.rect = self.Clyde.get_rect()
        #self.screen_rect = game.screen.get_rect()
        self.dying = self.dead = False

    def ghost_direction(self, type, xNew, yNew):
        if type == 0: 
            xOld = self.Blinky_location[0]
            yOld = self.Blinky_location[1]
            self.Blinky_location = (xNew + xOld, yNew + yOld)
        if type == 1: 
            xOld = self.Pinky_location[0]
            yOld = self.Pinky_location[1]
            self.Pinky_location = (xNew + xOld, yNew + yOld)
        if type == 2: 
            xOld = self.Inky_location[0]
            yOld = self.Inky_location[1]
            self.Inky_location = (xNew + xOld, yNew + yOld)
        if type == 3: 
            xOld = self.Clyde_location[0]
            yOld = self.Clyde_location[1]
            self.Clyde_location = (xNew + xOld, yNew + yOld)

    #def give_location(self, type):
     #   if type = 0: 
       
   
    def render(self, screen, x , y):
        self.screen.blit(self.Blinky, self.Blinky_location)
        self.screen.blit(self.Pinky, self.Pinky_location)
        self.screen.blit(self.Inky, self.Inky_location)
        self.screen.blit(self.Clyde, self.Clyde_location)

    # def checkcollison(self):
    #     collisions = pygame.sprite.spritecollide(self, self.pacman)  
    #     if collisions:
    #         for pacman in collisions:
    #             pacman.hit()

    def resetBlinky(self):
        self.Blinky_location = (200, 180)
        self.dying = self.dead = False

    def resetPinky(self):
        self.Pinky_location = (200, 180)
        self.dying = self.dead = False

    def resetInky(self):
        self.Inky_location = (200, 180)
        self.dying = self.dead = False

    def resetClyde(self):
        self.Clyde_location = (200, 180)
        self.dying = self.dead = False
    def hitC(self):
        if not self.dying:
            print("This was hit")
            self.dying = True
            self.resetClyde()

    def hitP(self):
        if not self.dying:
            print("This was hit")
            self.dying = True
            self.resetPinky()

    def hitI(self):
        if not self.dying:
            print("This was hit")
            self.dying = True
            self.resetInky()
    def hitB(self):
        if not self.dying:
            print("This was hit")
            self.dying = True
            self.resetBlinky()
class Blinky(Ghost):
    def __init__(self,game):
        Ghost.__init__(self, game)
        self.render()
        

        
