from random import randint
from vector import Vector
import pygame as pg
from pygame.sprite import Sprite, Group
from timer import Timer
from settings import *

class Ghost(Sprite):

    def __init__self(self, game, node, type, pac=None, blinky=None):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.goal = Vector()
    
        GHOST = 3
        self.name = GHOST
        self.pac = pac
        self.points = 200
        self.type = type
        self.sb = game.scoreboard
        self.blinky = blinky
        self.dying = self.dead = False
        self.homeNode = node

    def reset(self):
        STOP = 0
        self.setStartNode(self.startNode)
        self.direction = STOP
        self.speed = 100
        self.visible = True

    def chase(self):
        self.goal = self.pacman.position

    def spawn(self):
        self.goal = self.spawnNode.position

    def setSpawnNode(self, node):
        self.spawnNode = node

    def startSpawn(self):
        SPAWN = 3
        self.mode.setSpawnMode()
        if self.mode.current == SPAWN:
            self.setSpeed(150)
            self.directionMethod = self.goalDirection
            self.spawn()

    def startGroupMov(self):
        FREIGHT = 2
        self.mode.setFreightMode()
        if self.mode.current == FREIGHT:
            self.setSpeed(50)
            self.directionMethod = self.randomDirection  

class Blinky(Ghost):
    def __init__(self, node, pacman=None, blinky=None):
        Ghost.__init__(self, node, pacman, blinky)
       # BLINKY = insertimage
        self.color = RED  
        self.image = pg.image.load('images/red-ghost.png')

class Pinky(Ghost):
    def __init__(self, node, pacman=None, blinky=None):
        Ghost.__init__(self, node, pacman, blinky)
       # PINKY = insert image
        self.color = PINK  

    def scatter(self):
        self.goal = Vector(TILEWIDTH*NCOLS, 0)

    def chase(self):
        self.goal = self.pacman.position + self.pacman.directions[self.pacman.direction] * TILEWIDTH * 4


class Inky(Ghost):
    def __init__(self, node, pacman=None, blinky=None):
        Ghost.__init__(self, node, pacman, blinky)
        #INKY = insert image
        self.color = TEAL

    def scatter(self):
        self.goal = Vector(TILEWIDTH*NCOLS, TILEHEIGHT*NROWS)

    def chase(self):
        vec1 = self.pacman.position + self.pacman.directions[self.pacman.direction] * TILEWIDTH * 2
        vec2 = (vec1 - self.blinky.position) * 2
        self.goal = self.blinky.position + vec2

class Clyde(Ghost):
    def __init__(self, node, pacman=None, blinky=None):
        Ghost.__init__(self, node, pacman, blinky)
        #self.name = insert image
        self.color = ORANGE

    def scatter(self):
        self.goal = Vector(0, TILEHEIGHT*NROWS)

    def chase(self):
        d = self.pacman.position - self.position
        ds = d.magnitudeSquared()
        if ds <= (TILEWIDTH * 8)**2:
            self.scatter()
        else:
            self.goal = self.pacman.position + self.pacman.directions[self.pacman.direction] * TILEWIDTH * 4

class GhostGroup(object):
    def __init__(self, node, pacman):
        self.blinky = Blinky(node, pacman)
        self.pinky = Pinky(node, pacman)
        self.inky = Inky(node, pacman, self.blinky)
        self.clyde = Clyde(node, pacman)
        self.ghosts = [self.blinky, self.pinky, self.inky, self.clyde]
   
    def __iter__(self):
        return iter(self.ghosts)

    def update(self, dt):
        for ghost in self:
            ghost.update(dt)

    def startFreight(self):
        for ghost in self:
            ghost.startFreight()
        self.resetPoints()

    def setSpawnNode(self, node):
        for ghost in self:
            ghost.setSpawnNode(node)

    def updatePoints(self):
        for ghost in self:
            ghost.points *= 2

    def resetPoints(self):
        for ghost in self:
            ghost.points = 200

    def hide(self):
        for ghost in self:
            ghost.visible = False

    def show(self):
        for ghost in self:
            ghost.visible = True

    def reset(self):
        for ghost in self:
            ghost.reset()

    def render(self, screen):
        for ghost in self:
            ghost.render(screen)

