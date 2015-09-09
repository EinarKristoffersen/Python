'''
Created on 5. sep. 2015

@author: Einar
'''

import pygame
from Constants import Constants as C

class Circle():
    def __init__(self, radius, color, inner):
        self.radius = radius
        self.color = color
        self.inner = inner
        
    def draw(self):
        if self.inner:
            pygame.draw.circle(C.SCREEN, self.color, (int(self.pos.x), int(self.pos.y)), int(self.radius), self.inner) 
        else:
            pygame.draw.circle(C.SCREEN, self.color, (int(self.pos.x), int(self.pos.y)), int(self.radius))
            
    def update(self, time_passed_seconds):
        self.pos += self.dir*time_passed_seconds
        
    def intersect_circle(self, pos, radius):
        dp1p2 = pos - self.pos
        if self.radius + radius >= dp1p2.magnitude():
            return True
        else:
            return False 