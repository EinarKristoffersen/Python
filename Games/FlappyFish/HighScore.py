'''
Created on 12. sep. 2015

@author: Einar
'''

class HighScore():
    def __init__(self):
        self.highscore = 0
        filename = "highscore.txt"
        self.file = open(filename, "r+")
        self.get_score()
        
    def get_score(self):
        score = self.file.read()
        if len(score) == 0:
            return
        self.highscore = int(float(score))
    
    def set_highscore_if_needed(self, score):
        if score > self.highscore:
            self.highscore = score
            self.save_score(score)
    
    def save_score(self, score):
        self.file.seek(0)
        self.file.write(str(score))
        self.file.truncate()
      
        
        