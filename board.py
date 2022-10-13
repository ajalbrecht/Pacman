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
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0]]
        
        self.Clide =  [[0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0]]
        print("initalized all arrays")
        #self.getPacmanLocation()
        for x in range(7):
            for y in range(7):
                if [x][y] == 1:
                   print("why hello there")
                print("I ran through all elements")
        
    
    def GetPacmanLocation():
        for x in range(len(self.game_board)):
            for y in range(len(self.game_board[x])):
                if [x][y] == 1:
                   print("why hello there")
                print("I ran through all elements today")
        

        #want to.. set pos for each, return pos for each, reset all board, 
        #add later (poettialy draw board based upon array, gosts should still have their own draw)
