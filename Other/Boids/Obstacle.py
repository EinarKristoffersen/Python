'''
Created on 5. sep. 2015

@author: Einar
'''
import random
from Constants import Constants as C
from Circle import  Circle
from Vector import Vector

class Obstacle(Circle):
    def __init__(self):
        radius = random.randint(C.OBSTACLE_RADIUS_MIN, C.OBSTACLE_RADIUS_MAX)
        Circle.__init__(self, radius, C.OBSTACLE_COLOR, None)
        self.pos = Vector(random.randint(0, C.SCREEN_SIZE.x), random.randint(0, C.SCREEN_SIZE.y))
