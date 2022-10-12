import pygame
import pygame.locals
from vector import Vector
import settings

class Pacman(object):
    def __init__(self):
        self.name = settings.PACMAN
        self.position = Vector(200, 400)
        self.directions = {settings.STOP:Vector(0,0), settings.UP:Vector(0,-1), settings.DOWN:Vector(0,1), settings.LEFT:Vector(-1,0), settings.RIGHT:Vector(1,0)}
        self.direction = settings.STOP
        self.speed = 100
        self.radius = 10
        self.color = settings.YELLOW

    def update(self, dt):	
        self.position += self.directions[self.direction]*self.speed*dt
        direction = self.getValidKey()
        self.direction = direction

    def getValidKey(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            return settings.UP
        if key_pressed[pygame.K_DOWN]:
            return settings.DOWN
        if key_pressed[pygame.K_LEFT]:
            return settings.LEFT
        if key_pressed[pygame.K_RIGHT]:
            return settings.RIGHT
        return settings.STOP

    def render(self, screen):
        p = self.position.asInt()
        pygame.draw.circle(screen, self.color, p, self.radius)

