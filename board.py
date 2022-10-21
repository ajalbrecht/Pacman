import pygame as pg
from pygame.sprite import Sprite, Group
import settings

class Graph(object):
    print("I was called") 
    def __init__(self, screen, pac):
        # 0=wall   1=open_space_with_food    2=open_space_without_food   3=ghost_house_door
        self.screen = screen
        self.pac = pac
        self.game_board = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                           [0,1,0,1,0,0,0,0,0,0,0,1,0,1,0],
                           [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                           [0,1,0,1,0,0,0,2,0,0,0,1,0,1,0],
                           [0,1,0,1,0,0,2,2,2,0,0,1,0,1,0],
                           [0,1,0,1,0,0,0,0,0,0,0,1,0,1,0],
                           [0,1,0,1,1,1,0,0,0,1,1,1,0,1,0],
                           [0,1,0,1,0,1,0,0,0,1,0,1,0,1,0],
                           [0,1,0,1,0,1,1,1,1,1,0,1,0,1,0],
                           [0,1,0,1,0,0,1,0,1,0,0,1,0,1,0],
                           [0,1,0,1,0,0,1,0,1,0,0,1,0,1,0],
                           [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                           [0,1,0,1,0,0,0,1,0,0,0,1,0,1,0],
                           [0,1,0,1,0,0,0,1,0,0,0,1,0,1,0],
                           [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                           [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
        self.nodes = Group()
        self.walls = Group()
        for y in range(17):
            for x in range(15):
                if self.game_board[y][x] == 1:
                    self.nodes.add(Node(x, y,self.screen))
                if self.game_board[y][x] == 0:
                    self.walls.add(Wall(x, y,self.screen))

        self.Pacman = [[0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,1,0,0,0],
                       [0,0,0,0,0,0,0]]

        self.Inky =   [[0,0,0,0,0,0,0],
                       [0,0,0,1,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0]]
        
        self.Blinky = [[0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,1,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0]]
        
        self.Pinky =  [[0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,1,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0]]
        
        self.Clide =  [[0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,1,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0]]
        print("initalized all arrays")

    def TypeToCharacter(self, type):
        if type == 0: return self.Pacman
        if type == 1: return self.Inky
        if type == 2: return self.Blinky
        if type == 3: return self.Pinky
        if type == 4: return self.Clide

    def SetTypeLocation(self, type, x, y, value):      
        if type == 0: self.Pacman[x][y] = value
        if type == 1: self.Inky[x][y] = value
        if type == 2: self.Blinky[x][y] = value
        if type == 3: self.Pinky[x][y] = value
        if type == 4: self.Clide[x][y] = value

    def GetCharacterLocation(self, type):
        character = self.TypeToCharacter(type)
        for y in range(18):
            for x in range(14):
                if character[x][y] == 1:
                    return [x, y]

        return 0 # pacman isnt on the board? soemething must be wrong

    def SetCharacterLocation(self, type, x, y):
        original_location = self.GetCharacterLocation(type)
        # update character location is passed in
        oldx = original_location[0]
        oldy = original_location[1]
        self.SetTypeLocation(type, oldx, oldy, 0)
        self.SetTypeLocation(type, x, y, 1)

    def check_food(self):
        for Node in self.nodes:
            if (Node.position()[0] - 20) < self.pac.position.asTuple()[0] < (Node.position()[0] + 20):
                if (Node.position()[1] - 20) < self.pac.position.asTuple()[1] < (Node.position()[1] + 20):
                    Node.hit()
                    # increments points here  <-

    def check_wall(self):
        # prevent collsion from down direction
        for Wall in self.walls:
            if (Wall.position()[0] - 20) < self.pac.position.asTuple()[0] < (Wall.position()[0] + 20): # 25
                if (Wall.position()[1] - 25) < self.pac.position.asTuple()[1] < (Wall.position()[1]):
                    self.pac.direction = settings.UP
        # prevent colisoin from up direction
        for Wall in self.walls:
            if (Wall.position()[0] - 20) < self.pac.position.asTuple()[0] < (Wall.position()[0] + 20): # 25
                if (Wall.position()[1]) < self.pac.position.asTuple()[1] < (Wall.position()[1] + 25):
                    self.pac.direction = settings.DOWN
        # prevent colisoin from left direction
        for Wall in self.walls:
            if (Wall.position()[0]) < self.pac.position.asTuple()[0] < (Wall.position()[0] + 25): # 25
                if (Wall.position()[1] - 20) < self.pac.position.asTuple()[1] < (Wall.position()[1] + 20):
                    self.pac.direction = settings.RIGHT       
        # prevent colisoin from right direction
        for Wall in self.walls:
            if (Wall.position()[0] - 25) < self.pac.position.asTuple()[0] < (Wall.position()[0]): # 25
                if (Wall.position()[1] - 20) < self.pac.position.asTuple()[1] < (Wall.position()[1] + 20):
                    self.pac.direction = settings.LEFT
        
        
        

    def render(self):
        self.check_food()
        self.check_wall()
        for Node in self.nodes: Node.draw()
        for Wall in self.walls: Wall.draw()
        #collisions = pg.sprite.spritecollide(self.pac, self.nodes, True)
        #if collisions:
        #    self.nodes.hit()


        #for Wall in self.walls:


class Node(Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.x = x * 32 + 16
        self.y = y * 32 + 16
        self.screen = screen
        
    def draw(self):    
        pg.draw.circle(self.screen, (255,255,255), (self.x, self.y), 5)

    def hit(self):
        self.kill()

    def position(self):
        return self.x, self.y

class Wall(Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.x = x * 32 + 16
        self.y = y * 32 + 16
        self.screen = screen
        
    def draw(self):    
        pg.draw.rect(self.screen, (0,0,255), pg.Rect(self.x-16, self.y-16, 32, 32))

    def position(self):
        return self.x, self.y

        



        #want to.. set pos for each, return pos for each, reset all board, 
        #add later (poettialy draw board based upon array, gosts should still have their own draw)
        # 14 * 18 Board
