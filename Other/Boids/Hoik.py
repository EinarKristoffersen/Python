'''
Created on 5. sep. 2015

@author: Einar
'''

import random
from Constants import Constants as C
from Circle import Circle
from Vector import Vector

class Hoik(Circle):
    def __init__(self, pos=None):
        Circle.__init__(self, C.HOIK_RADIUS, C.HOIK_COLOR, 2)
        self.velocity = C.HOIK_VELOCITY
        self.dir = Vector(random.randint(-10, 10),random.randint(-10, 10)).normalized() * self.velocity
       
        if pos == None:
            self.pos = Vector(random.randint(0, C.SCREEN_SIZE.x), random.randint(0, C.SCREEN_SIZE.y))
        else:
            self.pos = pos
        
    @classmethod
    def rule1(self, hoik, boids, flock):
        for boid in boids:
            if (boid.pos - hoik.pos).magnitude() < 200:
                flock.append(boid)
        if len(flock) == 0:
            for boid in boids:
                if (boid.pos - hoik.pos).magnitude() < 400:
                    flock.append(boid)
        if len(flock) > 0:
            avg = Vector.average([boid.pos for boid in flock])
            return (avg - hoik.pos)*(50.0/100.0)
        return Vector(0, 0)
    
    @classmethod
    def rule2(self, hoik, obstacles):
        v = Vector(0,0)
        for obstacle in obstacles:
            c = obstacle.pos - hoik.pos
            if (c.magnitude() < (obstacle.radius + hoik.radius + 10)):
                v -= c
        return v * 10
    
    @classmethod
    def rule3(self, hoik):
        v = Vector(0, 0)
        if hoik.pos.x < 10:
            v.x = 20
        elif hoik.pos.x > C.SCREEN_SIZE.x-10:
            v.x = -20
        if hoik.pos.y < 10:
            v.y = 20
        elif hoik.pos.y > C.SCREEN_SIZE.y-10:
            v.y = -20
        return v

    def eat(self, boids, flock):
        for boid in flock:
            if self.intersect_circle(boid.pos, boid.radius):
                boids.remove(boid)
                flock.remove(boid)
                self.radius += 0.2
        
        