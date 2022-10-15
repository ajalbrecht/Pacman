import pygame as pg
from pygame.sprite import Sprite, Group

class Graph(object):
    print("I was called") 
    def __init__(self):
        # 0=wall   1=open_space_with_food    2=open_space_without_food   3=ghost_house_door
        self.game_board = [[0,0,0,0,0,0,0],
                        [0,1,1,2,1,1,0],
                        [0,1,0,3,0,1,0],
                        [0,1,2,2,2,1,0],
                        [0,1,0,0,0,1,0],
                        [0,1,1,2,1,1,0],
                        [0,0,0,0,0,0,0]]

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
    
    def GetCharacterLocation(self, type):
        character = self.TypeToCharacter(type)
        for x in range(7):
            for y in range(7):
                if character[y][x] == 1:
                    return [x, y]

        return 0 # pacman isnt on the board? soemething must be wrong

    def SetCharacterLocation(self, type, updated_location):
        character = self.TypeToCharacter(type)
        original_location = self.GetCharacterLocation(type)
        # update character location is passed in
        y = original_location[0]
        x = original_location[1]
        print(character)
       
       #character[original_location[0]][original_location[1]] = 0
        



        #want to.. set pos for each, return pos for each, reset all board, 
        #add later (poettialy draw board based upon array, gosts should still have their own draw)
