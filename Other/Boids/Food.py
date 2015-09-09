'''
Created on 5. sep. 2015

@author: Einar
'''

from Constants import Constants as C
from Vector import Vector
from Circle import Circle
import random

class Food(Circle):
    def __init__(self):
        Circle.__init__(self, C.FOOD_RADIUS, C.FOOD_COLOR, None)
        self.pos = Vector(random.randint(0, C.SCREEN_SIZE.x), random.randint(0, C.SCREEN_SIZE.y))
