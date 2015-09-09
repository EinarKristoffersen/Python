'''
Created on 12. juli 2014

@author: Criblica
'''

import math

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return "Vector(%s, %s)" % (self.x, self.y)
            
    def __add__(self, b):
        return Vector(self.x + b.x, self.y + b.y)

    def __sub__(self, b):
        return Vector(self.x - b.x, self.y - b.y)

    def __mul__(self, b):
        try:
            b = float(b)
            return Vector(self.x * b, self.y * b)
        except ValueError:
            print "Oops! Right value must be a float"
            raise

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalized(self):
        if self.x == self.y == 0:
            return Vector(0, 0)
        try:
            m = self.magnitude()
            return Vector(self.x / m, self.y / m)
        except ZeroDivisionError:
            print "Cannot normalize a zero-vector"
            raise

    @classmethod
    def average(self, vektorlist):
        avg = Vector(0,0)
        for vektor in vektorlist:
            avg += vektor
        try:
            avg *= 1.0/len(vektorlist)
            return avg
        except ZeroDivisionError:
            print "You can not devide by Zero!"
            raise  