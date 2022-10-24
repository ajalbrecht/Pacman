class GameStats():
    
    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.game_active = False
        self.score = 0
        self.level = 1
    
        f = open("hs.txt","r")
        self.high_score = int(f.read())
        f.close()


    def reset_stats(self): pass

    def update_highscore(self):
        f = open("hs.txt","w")
        f.write(str(self.high_score))
        f.close()