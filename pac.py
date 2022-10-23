import pygame
import pygame.locals
from vector import Vector
import settings
from pygame.sprite import Sprite, Group


class Pacman(Sprite):
    def __init__(self, game):
        self.game = game
        self.name = settings.PACMAN
        self.screen = game.screen
        self.settings = game.settings
        self.position = Vector(200, 400)
        self.directions = {settings.STOP:Vector(0,0), settings.UP:Vector(0,-1), settings.DOWN:Vector(0,1), settings.LEFT:Vector(-1,0), settings.RIGHT:Vector(1,0)}
        self.direction = settings.STOP
        self.speed = 65
        self.radius = 10
        self.color = settings.YELLOW
        # self.lives_x_start_pos = self.settings.SCREENWIDTH - (self.pac_lives()[0] * 2 + 20)
        self.image = pygame.image.load('images/yellowdot.png')
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()
        self.keys = 0
        self.pac_lives = settings.PACMAN_LIVES
        self.dying = self.dead = False

    def update(self, dt):	
        self.position += self.directions[self.direction]*self.speed*dt
        direction = self.getValidKey()
        self.direction = direction
        



        
    def getValidKey(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            self.keys = 1
            return settings.UP
        if key_pressed[pygame.K_DOWN]:
            self.keys = -1
            return settings.DOWN
        if key_pressed[pygame.K_LEFT]:
            self.keys = 2
            return settings.LEFT
        if key_pressed[pygame.K_RIGHT]:
            self.keys = -2
            return settings.RIGHT

        return self.keys
    

    def reset(self):
        self.position = Vector(200, 400)
        self.dying = self.dead = False

    def hit(self):
        if not self.dying:
            print('PAC IS HIT !!!!!!!!!!!!!!!!!!!!!')
            self.dying = True 

    def really_dead(self):
        self.pac_lives -= 1
        print(f'Pacman has died! Only {self.pac_lives} lives left')
        self.game.reset() if self.pac_lives > 0 else self.game.game_over()

    def render(self, screen):
        p = self.position.asInt()
        pygame.draw.circle(screen, self.color, p, self.radius)

    # def render_lives(self, screen):
