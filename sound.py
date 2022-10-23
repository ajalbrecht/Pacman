import pygame as pg

class Sound:
    def __init__(self):
        pg.mixer.init()
        pg.mixer.music.load('sounds/eat.wav')
        pg.mixer.music.load('sounds/2022-10-21 23-37-02.wav')

    def Eat(self):
        pg.mixer.music.load('sounds/eat.wav')
        pg.mixer.music.play(loops=0)

    def Run(self):
        pg.mixer.music('sounds/startrek2.wav')
        pg.mixer.music.play(loops=1)
    
    def Run_stop(self):
        pg.mixer.music.stop()

    # def Die(self):
    #     pg.mixer.music('sounds/startrek2.wav')
    #     pg.mixer.music.play(loops=0)


    