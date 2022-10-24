from re import S
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
        self.time = 0
        self.run_away = 301
        
        self.Blinky_timer = 0
        self.Blinky_directionX = 0
        self.Blinky_directionY = 0
        self.Blinky_old_move = 0

        self.Pinky_timer = 0
        self.Pinky_directionX = 0
        self.Pinky_directionY = 0
        self.Pinky_old_move = 0

        self.Clyde_timer = 0
        self.Clyde_directionX = 0
        self.Clyde_directionY = 0
        self.Clyde_old_move = 0

        self.Inky_timer = 0
        self.Inky_directionX = 0
        self.Inky_directionY = 0
        self.Inky_old_move = 0

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


    def move_pinky(self):
        #self.ghost.ghost_direction(3, 1, 1)
        #print(self.ghost.Blinky_location)
        #print(self.pac.position.asInt()[0])
        # pinky chaces infront of where pacman is
        if self.Pinky_timer == 0:
            run_add = 0
            if self.run_away < 300:
                run_add = 9000


            offsetX = 0
            offsetY = 0
            if self.pac.getValidKey() == settings.UP:
                offsetY = 50
            if self.pac.getValidKey() == settings.DOWN:
                offsetY = -50
            if self.pac.getValidKey() == settings.RIGHT:
                offsetX = 50
            if self.pac.getValidKey() == settings.LEFT:
                offsetX = 50

            x = self.ghost.Pinky_location[0]/ 32
            y = self.ghost.Pinky_location[1]/ 32
            x = round(x)
            y = round(y)
            option_list = []
            heurestic_list = []
            #(self.Blinky_old_move)
            if self.game_board[y+1][x] != 0 and self.Pinky_old_move != 4 and self.game_board[y+1][x] != 2 and self.game_board[y+1][x] != 5 and self.game_board[y+1][x] != 6: 
                option_list.append(3)
                heurestic_list.append((self.pac.position.asInt()[1] + offsetY) - self.ghost.Pinky_location[1])
            if self.game_board[y-1][x] != 0 and self.Pinky_old_move != 3 and self.game_board[y-1][x] != 2 and self.game_board[y-1][x] != 5 and self.game_board[y-1][x] != 6: 
                option_list.append(4)
                heurestic_list.append(self.ghost.Pinky_location[1] - (self.pac.position.asInt()[1] + offsetY) + run_add)
            if self.game_board[y][x+1] != 0 and self.Pinky_old_move != 2 and self.game_board[y][x+1] != 2 and self.game_board[y][x+1] != 5 and self.game_board[y][x+1] != 6: 
                option_list.append(1)
                heurestic_list.append((self.pac.position.asInt()[0] + offsetX) - self.ghost.Pinky_location[0])
            if self.game_board[y][x-1] != 0 and self.Pinky_old_move != 1 and self.game_board[y][x-1] != 2 and self.game_board[y][x-1] != 5 and self.game_board[y][x-1] != 6: 
                option_list.append(2)
                heurestic_list.append(run_add + self.ghost.Pinky_location[0] - (self.pac.position.asInt()[0] + offsetX))
            #print(option_list)
            #print(heurestic_list)
            best_option = -1000
            best_index = 0
            for i in range(len(heurestic_list)):
                #print(i)
                if heurestic_list[i] > best_option:
                    best_option = heurestic_list[i]
                    best_index = i
                    #print(heurestic_list[i])
            best_index = option_list[best_index]
            #print(best_option, best_index)

            #random_direction = random.choice(option_list)
            if best_index == 1: 
                self.Pinky_directionX = 1
                self.Pinky_directionY = 0
                self.Pinky_old_move = 1
            if best_index == 2: 
                self.Pinky_directionX = -1
                self.Pinky_directionY = 0
                self.Pinky_old_move = 2
            if best_index == 3: 
                self.Pinky_directionX = 0
                self.Pinky_directionY = 1
                self.Pinky_old_move = 3
            if best_index == 4: 
                self.Pinky_directionX = 0
                self.Pinky_directionY = -1
                self.Pinky_old_move = 4
            self.Pinky_timer = 32
        self.Pinky_timer = self.Pinky_timer - 1
        self.ghost.ghost_direction(1, self.Pinky_directionX, self.Pinky_directionY)
    
    def move_clyde(self):
        #self.ghost.ghost_direction(3, 1, 1)
        #print(self.ghost.Blinky_location)
        #print(self.pac.position.asInt()[0])
        run_add = 0
        if self.run_away < 300:
            run_add = 9000

        if self.Clyde_timer == 0:
            x = self.ghost.Clyde_location[0] / 32
            y = self.ghost.Clyde_location[1] / 32
            x = round(x)
            y = round(y)
            option_list = []
            heurestic_list = []
            #(self.Blinky_old_move)
            if self.game_board[y+1][x] != 0 and self.Clyde_old_move != 4 and self.game_board[y+1][x] != 2 and self.game_board[y+1][x] != 5 and self.game_board[y+1][x] != 6: 
                option_list.append(3)
                heurestic_list.append(run_add + self.pac.position.asInt()[1] - self.ghost.Clyde_location[1])
            if self.game_board[y-1][x] != 0 and self.Clyde_old_move != 3 and self.game_board[y-1][x] != 2 and self.game_board[y-1][x] != 5 and self.game_board[y-1][x] != 6: 
                option_list.append(4)
                heurestic_list.append(self.ghost.Clyde_location[1] - self.pac.position.asInt()[1])
            if self.game_board[y][x+1] != 0 and self.Clyde_old_move != 2 and self.game_board[y][x+1] != 2 and self.game_board[y][x+1] != 5 and self.game_board[y][x+1] != 6: 
                option_list.append(1)
                heurestic_list.append(self.pac.position.asInt()[0] - self.ghost.Clyde_location[0])
            if self.game_board[y][x-1] != 0 and self.Clyde_old_move != 1 and self.game_board[y][x-1] != 2 and self.game_board[y][x-1] != 5 and self.game_board[y][x-1] != 6: 
                option_list.append(2)
                heurestic_list.append(run_add + self.ghost.Clyde_location[0] - self.pac.position.asInt()[0])
            #print(option_list)
            #print(heurestic_list)
            best_option = -1000
            best_index = 0
            for i in range(len(heurestic_list)):
                #print(i)
                if heurestic_list[i] > best_option:
                    best_option = heurestic_list[i]
                    best_index = i
                    #print(heurestic_list[i])
            best_index = option_list[best_index]
            #print(best_option, best_index)

            #random_direction = random.choice(option_list)
            if best_index == 1: 
                self.Clyde_directionX = 1
                self.Clyde_directionY = 0
                self.Clyde_old_move = 1
            if best_index == 2: 
                self.Clyde_directionX = -1
                self.Clyde_directionY = 0
                self.Clyde_old_move = 2
            if best_index == 3: 
                self.Clyde_directionX = 0
                self.Clyde_directionY = 1
                self.Clyde_old_move = 3
            if best_index == 4: 
                self.Clyde_directionX = 0
                self.Clyde_directionY = -1
                self.Clyde_old_move = 4

           # clyde runs because hes to close based on decripton
            if best_option < 100 and best_option > 0:
                print("switched directions")
                if self.Clyde_old_move == 1: self.Clyde_old_move = 2
                if self.Clyde_old_move == 2: self.Clyde_old_move = 1
                if self.Clyde_old_move == 3: self.Clyde_old_move = 4
                if self.Clyde_old_move == 4: self.Clyde_old_move = 3

            self.Clyde_timer = 32
        self.Clyde_timer = self.Clyde_timer - 1
        self.ghost.ghost_direction(3, self.Clyde_directionX, self.Clyde_directionY)


    def move_blinky(self):
        #self.ghost.ghost_direction(3, 1, 1)
        #print(self.ghost.Blinky_location)
        #print(self.pac.position.asInt()[0])
        run_add = 0
        if self.run_away < 300:
            run_add = 9000

        if self.Blinky_timer == 0:
            x = self.ghost.Blinky_location[0] / 32
            y = self.ghost.Blinky_location[1] / 32
            x = round(x)
            y = round(y)
            option_list = []
            heurestic_list = []
            #(self.Blinky_old_move)
            if self.game_board[y+1][x] != 0 and self.Blinky_old_move != 4 and self.game_board[y+1][x] != 2 and self.game_board[y+1][x] != 5 and self.game_board[y+1][x] != 6: 
                option_list.append(3)
                heurestic_list.append(self.pac.position.asInt()[1] - self.ghost.Blinky_location[1])
            if self.game_board[y-1][x] != 0 and self.Blinky_old_move != 3 and self.game_board[y-1][x] != 2 and self.game_board[y-1][x] != 5 and self.game_board[y-1][x] != 6: 
                option_list.append(4)
                heurestic_list.append(run_add + self.ghost.Blinky_location[1] - self.pac.position.asInt()[1])
            if self.game_board[y][x+1] != 0 and self.Blinky_old_move != 2 and self.game_board[y][x+1] != 2 and self.game_board[y][x+1] != 5 and self.game_board[y][x+1] != 6: 
                option_list.append(1)
                heurestic_list.append(run_add + self.pac.position.asInt()[0] - self.ghost.Blinky_location[0])
            if self.game_board[y][x-1] != 0 and self.Blinky_old_move != 1 and self.game_board[y][x-1] != 2 and self.game_board[y][x-1] != 5 and self.game_board[y][x-1] != 6: 
                option_list.append(2)
                heurestic_list.append(self.ghost.Blinky_location[0] - self.pac.position.asInt()[0])
            #print(option_list)
            #print(heurestic_list)
            best_option = -1000
            best_index = 0
            for i in range(len(heurestic_list)):
                #print(i)
                if heurestic_list[i] > best_option:
                    best_option = heurestic_list[i]
                    best_index = i
                    #print(heurestic_list[i])
            best_index = option_list[best_index]
            #print(best_option, best_index)

            #random_direction = random.choice(option_list)
            if best_index == 1: 
                self.Blinky_directionX = 1
                self.Blinky_directionY = 0
                self.Blinky_old_move = 1
            if best_index == 2: 
                self.Blinky_directionX = -1
                self.Blinky_directionY = 0
                self.Blinky_old_move = 2
            if best_index == 3: 
                self.Blinky_directionX = 0
                self.Blinky_directionY = 1
                self.Blinky_old_move = 3
            if best_index == 4: 
                self.Blinky_directionX = 0
                self.Blinky_directionY = -1
                self.Blinky_old_move = 4
            self.Blinky_timer = 32
        self.Blinky_timer = self.Blinky_timer - 1
        self.ghost.ghost_direction(0, self.Blinky_directionX, self.Blinky_directionY)

    def move_inky(self):
        #self.ghost.ghost_direction(3, 1, 1)
        #print(self.ghost.Blinky_location)
        #print(self.pac.position.asInt()[0])
        run_add = 0
        if self.run_away < 300:
            run_add = 9000

        if self.Inky_timer == 0:
            x = self.ghost.Inky_location[0] / 32
            y = self.ghost.Inky_location[1] / 32
            x = round(x)
            y = round(y)
            option_list = []
            heurestic_list = []
            #print(self.Blinky_old_move)
            if self.game_board[y+1][x] != 0 and self.Inky_old_move != 4 and self.game_board[y+1][x] != 2 and self.game_board[y+1][x] != 5 and self.game_board[y+1][x] != 6: 
                option_list.append(3)
                heurestic_list.append((run_add + self.pac.position.asInt()[1] + self.ghost.Blinky_location[1])/2 - self.ghost.Inky_location[1])
            if self.game_board[y-1][x] != 0 and self.Inky_old_move != 3 and self.game_board[y-1][x] != 2 and self.game_board[y-1][x] != 5 and self.game_board[y-1][x] != 6: 
                option_list.append(4)
                heurestic_list.append((self.pac.position.asInt()[1] + self.ghost.Blinky_location[1])/2 - self.pac.position.asInt()[1])
            if self.game_board[y][x+1] != 0 and self.Inky_old_move != 2 and self.game_board[y][x+1] != 2 and self.game_board[y][x+1] != 5 and self.game_board[y][x+1] != 6: 
                option_list.append(1)
                heurestic_list.append((run_add + self.pac.position.asInt()[0] + self.ghost.Blinky_location[0])/2 - self.ghost.Inky_location[0])
            if self.game_board[y][x-1] != 0 and self.Inky_old_move != 1 and self.game_board[y][x-1] != 2 and self.game_board[y][x-1] != 5 and self.game_board[y][x-1] != 6: 
                option_list.append(2)
                heurestic_list.append((self.pac.position.asInt()[0] + self.ghost.Blinky_location[0])/2 - self.pac.position.asInt()[0])
            #print(option_list)
            #print(heurestic_list)
            best_option = -1000
            best_index = 0
            for i in range(len(heurestic_list)):
                #print(i)
                if heurestic_list[i] > best_option:
                    best_option = heurestic_list[i]
                    best_index = i
                    #print(heurestic_list[i])
            best_index = option_list[best_index]
            #print(best_option, best_index)

            #random_direction = random.choice(option_list)
            if best_index == 1: 
                self.Inky_directionX = 1
                self.Inky_directionY = 0
                self.Inky_old_move = 1
            if best_index == 2: 
                self.Inky_directionX = -1
                self.Inky_directionY = 0
                self.Inky_old_move = 2
            if best_index == 3: 
                self.Inky_directionX = 0
                self.Inky_directionY = 1
                self.Inky_old_move = 3
            if best_index == 4: 
                self.Inky_directionX = 0
                self.Inky_directionY = -1
                self.Inky_old_move = 4
            self.Inky_timer = 32
        self.Inky_timer = self.Inky_timer - 1
        self.ghost.ghost_direction(2, self.Inky_directionX, self.Inky_directionY)      



    def check_food(self):
        for Node in self.nodes:
            if (Node.position()[0] - 20) < self.pac.position.asTuple()[0] < (Node.position()[0] + 20):
                if (Node.position()[1] - 20) < self.pac.position.asTuple()[1] < (Node.position()[1] + 20):
                    Node.hit()
                    self.sound.Eat()
                    #When hit, add points and call prep score
                    self.stats.score += self.pac.food_points
                    self.sb.prep_score()

                   

    def check_pacBlinky(self):
        newx = self.ghost.Blinky_location[0]
        newy = self.ghost.Blinky_location[1]
        if (newx - 20) < self.pac.position.asTuple()[0] < (newx + 20):
            if (newy - 20) < self.pac.position.asTuple()[1] < (newy + 20):
                self.pac.hit()
                self.sound.Die()
                self.pac.really_dead()
    def check_pacPinky(self):
        newx = self.ghost.Pinky_location[0]
        newy = self.ghost.Pinky_location[1]
        if (newx - 20) < self.pac.position.asTuple()[0] < (newx + 20):
            if (newy - 20) < self.pac.position.asTuple()[1] < (newy + 20):
                self.pac.hit()
                self.sound.Die()
                self.pac.really_dead()

    def check_pacInky(self):
        newx = self.ghost.Inky_location[0]
        newy = self.ghost.Inky_location[1]
        if (newx - 20) < self.pac.position.asTuple()[0] < (newx + 20):
            if (newy - 20) < self.pac.position.asTuple()[1] < (newy + 20):
                self.pac.hit()
                self.sound.Die()
                self.pac.really_dead()

    def check_pacClyde(self):
        newx = self.ghost.Pinky_location[0]
        newy = self.ghost.Pinky_location[1]
        if (newx - 20) < self.pac.position.asTuple()[0] < (newx + 20):
            if (newy - 20) < self.pac.position.asTuple()[1] < (newy + 20):
                self.pac.hit()
                self.sound.Die()
                self.pac.really_dead()

    def check_pac_collision(self):
        self.check_pacBlinky()
        self.check_pacPinky()
        self.check_pacClyde()
        self.check_pacInky()


    def check_ghostPinky(self):
        newx = self.ghost.Pinky_location[0]
        newy = self.ghost.Pinky_location[1]
        if (newx - 20) < self.pac.position.asTuple()[0] < (newx + 20):
            if (newy - 20) < self.pac.position.asTuple()[1] < (newy + 20):
                self.ghost.hitP()
                self.Pinky_timer = 0



    def check_ghostInky(self):
        newx = self.ghost.Inky_location[0]
        newy = self.ghost.Inky_location[1]
        if (newx - 20) < self.pac.position.asTuple()[0] < (newx + 20):
            if (newy - 20) < self.pac.position.asTuple()[1] < (newy + 20):
                self.ghost.hitI()
                self.Inky_timer = 0


    

    def check_ghostClyde(self):
        newx = self.ghost.Clyde_location[0]
        newy = self.ghost.Clyde_location[1]
        if (newx - 20) < self.pac.position.asTuple()[0] < (newx + 20):
            if (newy - 20) < self.pac.position.asTuple()[1] < (newy + 20):
                self.ghost.hitC()
                self.Clyde_timer = 0

    def check_ghostBlinky(self):
        newx = self.ghost.Blinky_location[0]
        newy = self.ghost.Blinky_location[1]
        if (newx - 20) < self.pac.position.asTuple()[0] < (newx + 20):
            if (newy - 20) < self.pac.position.asTuple()[1] < (newy + 20):
                self.ghost.hitB()
                self.Blinky_timer = 0

    def powereffect(self):
        self.check_ghostBlinky()
        self.check_ghostClyde()
        self.check_ghostInky()
        self.check_ghostPinky()


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

    def check_teleportGB(self):
        newx = self.ghost.Blinky_location[0]
        newy = self.ghost.Blinky_location[1]
        for Teleport in self.teleport:
            if (Teleport.position()[0] - 20) < newx < (Teleport.position()[0] + 20):
                if (Teleport.position()[1] - 20) < newy < (Teleport.position()[1] + 20):
                    self.ghost.teleportB_()
                    Teleport.hit()
    def check_teleportGB2(self):
        newx = self.ghost.Blinky_location[0]
        newy = self.ghost.Blinky_location[1]
        for Teleport2 in self.teleport2:
            if (Teleport2.position()[0] - 20) < newx < (Teleport2.position()[0] + 20):
                if (Teleport2.position()[1] - 20) < newy < (Teleport2.position()[1] + 20):
                    self.ghost.teleportB_2()
                    Teleport2.hit()

    def check_teleportGP(self):
        newx = self.ghost.Pinky_location[0]
        newy = self.ghost.Pinky_location[1]
        for Teleport in self.teleport:
            if (Teleport.position()[0] - 20) < newx < (Teleport.position()[0] + 20):
                if (Teleport.position()[1] - 20) < newy < (Teleport.position()[1] + 20):
                    self.ghost.teleportP_()
                    Teleport.hit()
    def check_teleportGP2(self):
        newx = self.ghost.Pinky_location[0]
        newy = self.ghost.Pinky_location[1]
        for Teleport2 in self.teleport2:
            if (Teleport2.position()[0] - 20) < newx < (Teleport2.position()[0] + 20):
                if (Teleport2.position()[1] - 20) < newy < (Teleport2.position()[1] + 20):
                    self.ghost.teleportP_2()
                    Teleport2.hit()

    def check_teleportGI(self):
        newx = self.ghost.Inky_location[0]
        newy = self.ghost.Inky_location[1]
        for Teleport in self.teleport:
            if (Teleport.position()[0] - 20) < newx < (Teleport.position()[0] + 20):
                if (Teleport.position()[1] - 20) < newy < (Teleport.position()[1] + 20):
                    self.ghost.teleportI_()
                    Teleport.hit()
    def check_teleportGI2(self):
        newx = self.ghost.Inky_location[0]
        newy = self.ghost.Inky_location[1]
        for Teleport2 in self.teleport2:
            if (Teleport2.position()[0] - 20) < newx < (Teleport2.position()[0] + 20):
                if (Teleport2.position()[1] - 20) < newy < (Teleport2.position()[1] + 20):
                    self.ghost.teleportI_2()
                    Teleport2.hit()

    def check_teleportGC(self):
        newx = self.ghost.Clyde_location[0]
        newy = self.ghost.Blinky_location[1]
        for Teleport in self.teleport:
            if (Teleport.position()[0] - 20) < newx < (Teleport.position()[0] + 20):
                if (Teleport.position()[1] - 20) < newy < (Teleport.position()[1] + 20):
                    self.ghost.teleportC_()
                    Teleport.hit()
    def check_teleportGC2(self):
        newx = self.ghost.Clyde_location[0]
        newy = self.ghost.Clyde_location[1]
        for Teleport2 in self.teleport2:
            if (Teleport2.position()[0] - 20) < newx < (Teleport2.position()[0] + 20):
                if (Teleport2.position()[1] - 20) < newy < (Teleport2.position()[1] + 20):
                    self.ghost.teleportC_2()
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
                    self.sound.Power()
                    Powerup.hit()
                    self.run()
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
            self.stats.level = self.stats.level + 1
            self.sb.prep_level()
            print("level increment")
            for y in range(17):
                for x in range(15):
                    if self.game_board[y][x] == 1:
                        self.nodes.add(Node(x, y,self.screen))
                    if self.game_board[y][x] == 3:
                        self.powerup.add(Powerup(x, y,self.screen))

    def run(self):
        # invert positins to run
        self.run_away = 0
        self.sound.Run()

    
    def render(self):
        self.check_food()
        self.check_wall()
        self.is_powerup()
        self.is_fruit()
        self.check_teleport()
        self.check_teleport2()
        self.check_teleportGB()
        self.check_teleportGB2()
        self.check_teleportGP()
        self.check_teleportGP2()
        self.check_teleportGI()
        self.check_teleportGI2()
        self.check_teleportGC()
        self.check_teleportGC2()
        self.is_empty()

        if self.run_away < 300:
            self.powereffect()
        else:
            self.check_pac_collision()

        for Node in self.nodes: Node.draw()
        for Wall in self.walls: Wall.draw()
        for Powerup in self.powerup: Powerup.draw()
        for Fruit in self.fruit: Fruit.draw()
        
        for Teleport in self.teleport: Teleport.draw()
        #self.ghost.ghost_direction(3, 1, 1)
        #print(self.ghost.Blinky_location)
        self.move_blinky()
        if self.time == 100:
            self.ghost.ghost_direction(1, 32, -64)
        if self.time > 100:
            self.move_pinky()
        
        if self.time == 200:
           self.ghost.ghost_direction(2, 0, -64) 
        if self.time > 200:
            self.move_inky()

        if self.time == 300:
            self.ghost.ghost_direction(3, -32, -64)
        if self.time > 300:
            self.move_clyde()
        
        self.time += 1
        self.run_away += 1


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
        self.x = x * 32 + 18
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

