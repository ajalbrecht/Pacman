import pygame as pg
from pygame.sprite import Sprite, Group

class Graph(object):
    print("I was called") 
    def __init__(self, screen):
        # 0=wall   1=open_space_with_food    2=open_space_without_food   3=ghost_house_door
        self.screen = screen
        self.game_board = [[0,0,0,0,0,0,0],
                        [0,1,1,2,1,1,0],
                        [0,1,0,3,0,1,0],
                        [0,1,2,2,2,1,0],
                        [0,1,0,0,0,1,0],
                        [0,1,1,2,1,1,0],
                        [0,0,0,0,0,0,0]]
        self.nodes = Group()
        for y in range(7):
            for x in range(7):
                if self.game_board[x][y] == 1:
                    self.nodes.add(Node(x, y,self.screen))

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
        for y in range(7):
            for x in range(7):
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

class Node(Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.x = x * 10
        self.y = y * 10
        self.screen = screen
        print("drawing a node at", x, y)
        #pg.draw.circle(self.screen, Color(100,100,100,0), self.x, self.y)

        



        #want to.. set pos for each, return pos for each, reset all board, 
        #add later (poettialy draw board based upon array, gosts should still have their own draw)
