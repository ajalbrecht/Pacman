import pygame as pg
from pygame.sprite import Sprite, Group
from ghost import Blinky
import settings
import sound
import random

class Graph(object):
    print("I was called") 
    def __init__(self, screen, pac, sound, ghost, stats, sb):
        # 0=wall   1=open_space_with_food    2=open_space_without_food   3=ghost_house_door
        # 5 = Teleport 4= fruit
        self.screen = screen
        self.pac = pac
        self.sound = sound
        self.ghost = ghost
        self.stats = stats
        self.sb = sb
        
        self.Blinky_timer = 0
        self.Blinky_directionX = 0
        self.Blinky_directionY = 0
        self.Blinky_old_move = 0

        self.game_board = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [0,3,1,1,1,1,1,1,1,1,1,1,1,3,0],
                           [0,1,0,1,0,0,0,0,0,0,0,1,0,1,0],
                           [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                           [0,1,0,1,0,0,0,2,0,0,0,1,0,4,0],
                           [0,1,0,1,0,0,2,2,2,0,0,1,0,1,0],
                           [0,1,0,1,0,0,0,0,0,0,0,1,0,1,0],
                           [0,1,0,1,1,1,0,0,0,1,1,1,0,1,0],
                           [0,1,0,1,0,1,0,0,0,1,0,1,0,1,0],
                           [5,1,0,1,0,1,1,1,1,1,0,1,0,1,6],
                           [0,1,0,1,0,0,1,0,1,0,0,1,0,1,0],
                           [0,1,0,1,0,0,1,0,1,0,0,1,0,1,0],
                           [0,4,1,1,1,1,1,1,1,1,1,1,1,1,0],
                           [0,1,0,1,0,0,0,1,0,0,0,1,0,1,0],
                           [0,1,0,1,0,0,0,1,0,0,0,1,0,1,0],
                           [0,3,1,1,1,1,1,1,1,1,1,1,1,3,0],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                           [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

        self.nodes = Group()
        self.walls = Group()
        self.teleport = Group()
        self.teleport2 = Group()
        self.powerup = Group()
        self.fruit = Group()

        for y in range(17):
            for x in range(15):
                if self.game_board[y][x] == 1:
                    self.nodes.add(Node(x, y,self.screen))
                if self.game_board[y][x] == 0:
                    self.walls.add(Wall(x, y,self.screen))
                if self.game_board[y][x] == 3:
                    self.powerup.add(Powerup(x, y,self.screen))
                if self.game_board[y][x] == 4:
                    self.fruit.add(Fruit(x, y,self.screen))      
                if self.game_board[y][x] == 5:
                    self.teleport.add(Teleport(x, y,self.screen))   
                if self.game_board[y][x] == 6:
                    self.teleport2.add(Teleport2(x, y,self.screen))             

        # dead code atm
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

    def board_copy():
        return self.game_board

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

   ### end of dead code

    def random_track(self, type):
        #self.ghost.ghost_direction(3, 1, 1)
        #print(self.ghost.Blinky_location)
        
        # curent = self.ghost.Blinky_location
        #if self.Blinky_timer == 0:
        #option_list = [1,2,3,4]
       #print(self.ghost.Blinky_location)
       # x = self.ghost.Blinky_location[0] / 32
        #y = self.ghost.Blinky_location[1] / 32
        #print(x,y)
        #self.ghost.ghost_direction(0, 0, 0)
        if self.Blinky_timer == 0:
            x = self.ghost.Blinky_location[0] / 32
            y = self.ghost.Blinky_location[1] / 32
            x = round(x)
            y = round(y)
            option_list = []
            if self.game_board[y+1][x] != 0:
                option_list.append(3)
                self.Blinky_old_move = 3
            if self.game_board[y-1][x] != 0:
                option_list.append(4)
                self.Blinky_old_move = 4
            if self.game_board[y][x+1] != 0:
                option_list.append(1)
                self.Blinky_old_move = 1
            if self.game_board[y][x-1] != 0:
                option_list.append(2)
                self.Blinky_old_move = 2
            print(option_list)
            random_direction = random.choice(option_list)
            if random_direction == 1: 
                self.Blinky_directionX = 1
                self.Blinky_directionY = 0
            if random_direction == 2: 
                self.Blinky_directionX = -1
                self.Blinky_directionY = 0
            if random_direction == 3: 
                self.Blinky_directionX = 0
                self.Blinky_directionY = 1
            if random_direction == 4: 
                self.Blinky_directionX = 0
                self.Blinky_directionY = -1
            self.Blinky_timer = 33
        self.Blinky_timer = self.Blinky_timer - 1
        self.ghost.ghost_direction(0, self.Blinky_directionX, self.Blinky_directionY)



    def check_food(self):
        for Node in self.nodes:
            if (Node.position()[0] - 20) < self.pac.position.asTuple()[0] < (Node.position()[0] + 20):
                if (Node.position()[1] - 20) < self.pac.position.asTuple()[1] < (Node.position()[1] + 20):
                    Node.hit()
                    self.sound.Eat()
                    #When hit, add points and call prep score
                    self.stats.score += self.pac.food_points
                    self.sb.prep_score()

                   

    def check_pacghost(self):
        newx = self.ghost.Blinky_location[0]
        newy = self.ghost.Blinky_location[1]
        if (newx - 20) < self.pac.position.asTuple()[0] < (newx + 20):
            if (newy - 20) < self.pac.position.asTuple()[1] < (newy + 20):
                self.pac.hit()
                self.pac.really_dead()

    # def check_ghostpac(self):
    #     newx = self.ghost.Blinky_location[0]
    #     newy = self.ghost.Blinky_location[1]
    #     if (newx - 20) < self.pac.position.asTuple()[0] < (newx + 20):
    #         if (newy - 20) < self.pac.position.asTuple()[1] < (newy + 20):
    #             self.ghost.hit()

    # def powereffect(self):
    #     self.check_ghostpac()

    def check_teleport(self):
        for Teleport in self.teleport:
            if (Teleport.position()[0] - 20) < self.pac.position.asTuple()[0] < (Teleport.position()[0] + 20):
                if (Teleport.position()[1] - 20) < self.pac.position.asTuple()[1] < (Teleport.position()[1] + 20):
                    self.pac.teleport()
                    Teleport.hit()
    def check_teleport2(self):
        for Teleport2 in self.teleport2:
            if (Teleport2.position()[0] - 20) < self.pac.position.asTuple()[0] < (Teleport2.position()[0] + 20):
                if (Teleport2.position()[1] - 20) < self.pac.position.asTuple()[1] < (Teleport2.position()[1] + 20):
                    self.pac.teleport2()
                    Teleport2.hit()

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

    def is_powerup(self):
        for Powerup in self.powerup:
            if (Powerup.position()[0] - 20) < self.pac.position.asTuple()[0] < (Powerup.position()[0] + 20):
                if (Powerup.position()[1] - 20) < self.pac.position.asTuple()[1] < (Powerup.position()[1] + 20):
                    print("hello there")
                    Powerup.hit()
                    # start chase sound, and end later  
                              
    def is_fruit(self):
        for Fruit in self.fruit:
            if (Fruit.position()[0] - 20) < self.pac.position.asTuple()[0] < (Fruit.position()[0] + 20):
                if (Fruit.position()[1] - 20) < self.pac.position.asTuple()[1] < (Fruit.position()[1] + 20):
                    print("hello there")
                    Fruit.hit()
    
    def is_empty(self):
        #print(self.nodes.sprites())
        if not self.nodes.sprites():
            for y in range(17):
                for x in range(15):
                    if self.game_board[y][x] == 1:
                        self.nodes.add(Node(x, y,self.screen))
    
    def render(self):
        self.check_food()
        self.check_wall()
        self.is_powerup()
        self.is_fruit()
        self.check_pacghost()
        # self.powereffect()
        self.check_teleport()
        self.check_teleport2()
        self.is_empty()
        for Node in self.nodes: Node.draw()
        for Wall in self.walls: Wall.draw()
        for Powerup in self.powerup: Powerup.draw()
        for Fruit in self.fruit: Fruit.draw()
        
        for Teleport in self.teleport: Teleport.draw()
        #self.ghost.ghost_direction(3, 1, 1)
        #print(self.ghost.Blinky_location)
        self.random_track(0)


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

class Powerup(Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.x = x * 32 + 16
        self.y = y * 32 + 16
        self.screen = screen
        
    def draw(self):   
        pg.draw.circle(self.screen, (255,100,0), (self.x, self.y), 8)

    def hit(self):
        self.kill()

    def position(self):
        return self.x, self.y   

class Fruit(Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.x = x * 32 + 16
        self.y = y * 32 + 16
        self.screen = screen
        
    def draw(self):   
        pg.draw.circle(self.screen, (255,0,0), (self.x, self.y), 6)

    def hit(self):
        # add points
        self.kill()

    def position(self):
        return self.x, self.y

class Teleport(Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.x = x * 32 + 16
        self.y = y * 32 + 16
        self.screen = screen
        
    def draw(self):    
        pg.draw.circle(self.screen, (0,0,0), (self.x, self.y), 5)

    def hit(self):
        print("This was hit ")
        

    def position(self):
        return self.x, self.y

        
class Teleport2(Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.x = x * 32 + 16
        self.y = y * 32 + 16
        self.screen = screen
        
    def draw(self):    
        pg.draw.circle(self.screen, (0,0,0), (self.x, self.y), 5)

    def hit(self):
        print("This was hit ")
        

    def position(self):
        return self.x, self.y


        #want to.. set pos for each, return pos for each, reset all board, 
        #add later (poettialy draw board based upon array, gosts should still have their own draw)
        # 14 * 18 Board
