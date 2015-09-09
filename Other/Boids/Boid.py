'''
Created on 5. sep. 2015

@author: Einar
'''

from Constants import Constants as C
from Vector import Vector
from Circle import Circle
import pygame
import random
random.seed()

class Boid(Circle):
    def __init__(self):
        Circle.__init__(self, C.BOID_RADIUS, C.BOID_COLOR, None)
        self.pos = Vector(random.randint(0, C.SCREEN.get_width()), random.randint(0, C.SCREEN.get_height()))
        self.velocity = C.BOID_VELOCITY
        self.dir = Vector(random.randint(-10, 10),random.randint(-10, 10)).normalized() * self.velocity
    
    def draw_tail(self):
        v = self.dir.normalized() * -abs(1) * C.BOID_TAIL_LENGTH        
        pygame.draw.line(C.SCREEN, self.color, (self.pos.x, self.pos.y), (self.pos.x + v.x, self.pos.y+v.y))
        
    @classmethod
    def rule1(self, this_boid, boids, flock):
        for boid in boids:
            if boid is not this_boid and (boid.pos - this_boid.pos).magnitude() < 70:
                flock.append(boid)
        if len(flock) > 0:
            avg = Vector.average([boid.pos for boid in flock])
            return (avg - this_boid.pos)*(50.0/100.0)
        return Vector(0, 0)

    @classmethod
    def rule2(self, this_boid, flock):
        v = Vector(0, 0)
        for boid in flock:
            if boid is not self:
                d = boid.pos - this_boid.pos
                if d.magnitude() < 15:
                    v -= d 
        return v *3
    
    @classmethod
    def rule3(self, this_boid, flock):
        avg = Vector.average([boid.dir for boid in flock])
        return avg - this_boid.dir * (1.0/8.0)
    
    @classmethod
    def rule4(self, this_boid, obstacles):
        v = Vector(0,0)
        for obstacle in obstacles:
            c = obstacle.pos - this_boid.pos
            if (c.magnitude() < (obstacle.radius + this_boid.radius + 20)):
                v -= c
        return v * 4
    
    @classmethod
    def rule5(self, this_boid, hoiks):
        v = Vector(0,0)
        for hoik in hoiks:
            c = hoik.pos - this_boid.pos
            if (c.magnitude() < (hoik.radius + this_boid.radius + 10)):
                v -= c
            
        return v * 10
    
    @classmethod
    def rule6(self, this_boid, foods):
        v = Vector(0,0)
        for food in foods:
            c = food.pos - this_boid.pos
            if (c.magnitude() < (food.radius + this_boid.radius +200)):
                v = c
        return v * 10
    
    @classmethod
    def rule7(self, this_boid):
        v = Vector(0, 0)
        if this_boid.pos.x < 10:
            v.x = 20
        elif this_boid.pos.x > C.SCREEN_SIZE.x-10:
            v.x = -20
        if this_boid.pos.y < 10:
            v.y = 20
        elif this_boid.pos.y > C.SCREEN_SIZE.y-10:
            v.y = -20
        return v
    
    def eat(self, foods):
        for food in foods:
            if self.intersect_circle(food.pos, food.radius):
                foods.remove(food)
    
            