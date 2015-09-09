'''
Created on 5. sep. 2015

@author: Einar
'''
import pygame
from Constants import Constants as C
from Boid import Boid
from Hoik import Hoik
from Obstacle import Obstacle
from Food import Food
from Vector import Vector

class Simulation():
    def __init__(self):
        self.setup()
        self.run()
        
    def setup(self):
        self.clock = pygame.time.Clock()
        self.flock = []
        self.foods = []
        
        self.boids = []
        for _ in range(0, C.TOTAL_BOIDS_NUM):
            self.boids.append(Boid())
        
        self.hoiks = []
        for _ in range(0, C.TOTAL_HOIKS_NUM):
            self.hoiks.append(Hoik())
            
        self.obstacles = []
        for _ in range(0, C.TOTAL_OBSTACLE_NUM):
            self.obstacles.append(Obstacle())
    
    def run(self):
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    for _ in range(0, C.ON_CLICK_CREATE_BOIDS_NUM):
                        self.boids.append(Boid())
                keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_f]:
                    for _ in range(0, C.TOTAL_FOOD_NUM):
                        self.foods.append(Food())
                elif keyPressed[pygame.K_h]:
                    x, y = pygame.mouse.get_pos()
                    self.hoiks.append(Hoik(Vector(x, y)))
                elif keyPressed[pygame.K_ESCAPE]:
                    exit()
                
            time_passed = self.clock.tick(C.FPS)
            time_passed_seconds = time_passed / 1000.0
            
            self.add_rules()
            self.draw()
            self.update(time_passed_seconds)
            
    def add_rules(self):
        for boid in self.boids:
            v1 = Boid.rule1(boid, self.boids, self.flock)
            v4 = Boid.rule4(boid, self.obstacles)
            v7 = Boid.rule7(boid)
            if len(self.flock) > 0:
                v2 = Boid.rule2(boid, self.flock)
                v3 = Boid.rule3(boid, self.flock)
                v5 = Boid.rule5(boid, self.hoiks)
                
                boid.dir += v2+v3+v5
            if len(self.foods) > 0:
                v6 = Boid.rule6(boid, self.foods)
                boid.dir += v6
                boid.eat(self.foods)
            
            boid.dir += v1+v4+v7
            if boid.dir.magnitude() < 100:
                boid.dir = boid.dir.normalized() * (boid.velocity - 50)
            
            if boid.dir.magnitude() > 180:
                boid.dir = boid.dir.normalized() * boid.velocity
            
            self.flock = []
                
        for hoik in self.hoiks:
            v1 = Hoik.rule1(hoik, self.boids, self.flock)
            v2 = Hoik.rule2(hoik, self.obstacles)
            v3 = Hoik.rule3(hoik)
            
            hoik.dir += v1+v2+v3
            if hoik.dir.magnitude() < 100:
                hoik.dir = hoik.dir.normalized() * (hoik.velocity - 50)
            if hoik.dir.magnitude() > 150:
                hoik.dir = hoik.dir.normalized() * (hoik.velocity)
                
            if len(self.flock) > 0:
                hoik.eat(self.boids, self.flock)
            self.flock = []

    def draw(self):
        pygame.draw.rect(C.SCREEN, (0,0,0), (0, 0, C.SCREEN_SIZE.x, C.SCREEN_SIZE.y))
        for boid in self.boids:
            boid.draw()
            boid.draw_tail()
        for hoik in self.hoiks:
            hoik.draw()
        for obstacle in self.obstacles:
            obstacle.draw()
        for food in self.foods:
            food.draw()
            
    def update(self, time):
        for boid in self.boids:
            boid.update(time)
        
        for hoik in self.hoiks:
            hoik.update(time)
            
        pygame.display.update()        
        
    
    
if __name__ == "__main__":
    sim = Simulation()
    