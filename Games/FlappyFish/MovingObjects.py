'''
Created on 7. sep. 2015

@author: Einar
'''

import pygame
from Vector import Vector
from Constants import Constants as C
from Variables import Variables as var


class MovingObject(pygame.sprite.Sprite):
    def __init__(self, direction, velocity, image, size, pos=None):
        pygame.sprite.Sprite.__init__(self)
        self.dir = direction
        
        self.velocity = velocity
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.size = size
        if pos:
            self.pos = pos
            self.rect = image.get_rect()
            self.rect.center = (self.pos.x+self.size.x/2, self.pos.y+self.size.y/2)
    
    def set_pos(self, pos):
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x+self.size.x/2, self.pos.y+self.size.y/2)
    
    def draw(self):
        C.SCREEN.blit(self.image, (self.pos.x, self.pos.y))
        
    def update(self, time_passed_seconds):
        self.pos += self.dir*self.velocity
        self.rect.center = (self.pos.x+self.size.x/2, self.pos.y+self.size.y/2)
        
    def collide_any(self, obj):
        collided = False
        if self.rect.colliderect(obj.rect) is False:
            return collided
        offset_x, offset_y = (obj.rect.left - self.rect.left), (obj.rect.top - self.rect.top)
        if (self.mask.overlap(obj.mask, (offset_x, offset_y)) != None):
            return True
        return False
    
class Fish(MovingObject):
    def __init__(self):
        MovingObject.__init__(self, C.FISH_DIR, C.FISH_VELOCITY, C.FISH_IMAGE, Vector(C.FISH_WIDTH, C.FISH_HEIGHT), C.FISH_POS)
        
    def update(self, time_passed_seconds):
        if self.pos.x < C.FISH_CONSTANT_POS_X:
            self.dir.x += self.velocity*time_passed_seconds
        else:
            self.dir.x = 0
            
        self.dir.y += C.FISH_GRAVITY*time_passed_seconds
        self.pos += self.dir
        self.outside_screen()
        self.rect.center = (self.pos.x+C.FISH_WIDTH/2, self.pos.y+C.FISH_HEIGHT/2)
        
    def outside_screen(self):
        if self.pos.y < C.SCORE_SCREEN_HEIGHT or self.pos.y > C.SCREEN_SIZE.y:
            var.game_over = True


class PipeTop(MovingObject):
    def __init__(self):
        MovingObject.__init__(self, C.PIPE_DIR, C.PIPE_VELOCITY, C.PIPE_IMAGE_TOP, Vector(C.PIPE_WIDTH, C.PIPE_HEIGHT))
        
class PipeMid(MovingObject):
    def __init__(self):
        MovingObject.__init__(self, C.PIPE_DIR, C.PIPE_VELOCITY, C.PIPE_IMAGE_MID, Vector(C.PIPE_WIDTH, C.PIPE_HEIGHT))
        
class PipeBottom(MovingObject):
    def __init__(self):
        MovingObject.__init__(self, C.PIPE_DIR, C.PIPE_VELOCITY, C.PIPE_IMAGE_BOT, Vector(C.PIPE_WIDTH, C.PIPE_HEIGHT))

class Pipe():
    def __init__(self, body_num):
        self.top = PipeTop()
        self.bottom = PipeBottom()
        self.body_elems = []
        for _ in range(0, body_num):
            self.body_elems.append(PipeMid())
        self.pipeGroup = pygame.sprite.Group()
        self.pipeGroup.add(self.top)
        self.pipeGroup.add(self.bottom)
        for elem in self.body_elems:
            self.pipeGroup.add(elem)
        self.passed = False
    
    def get_x_pos(self):        
        return self.bottom.pos.x
        
    def set_pos_floor(self, pos):
        self.bottom.set_pos(Vector(pos.x, pos.y))
        for elem in self.body_elems:
            pos.y -= C.PIPE_HEIGHT
            elem.set_pos(Vector(pos.x, pos.y))
        self.top.set_pos(Vector(pos.x, pos.y-C.PIPE_HEIGHT))
    
    def set_pos_roof(self, pos):
        self.bottom.set_pos(Vector(pos.x, pos.y))
        for elem in self.body_elems:
            pos.y += C.PIPE_HEIGHT
            elem.set_pos(Vector(pos.x, pos.y))
        self.top.set_pos(Vector(pos.x, pos.y+C.PIPE_HEIGHT))
        self.rotate_pipe()
    
    def rotate_pipe(self):
        self.top.image = pygame.transform.rotate(self.top.image, C.PIPE_ROTATION_DEGREE)
        self.bottom.image = pygame.transform.rotate(self.bottom.image, C.PIPE_ROTATION_DEGREE)
        for elem in self.body_elems:
            elem.image = pygame.transform.rotate(elem.image, C.PIPE_ROTATION_DEGREE)

    def draw(self):
        self.top.draw()
        self.bottom.draw()
        for elem in self.body_elems:
            elem.draw()
    
    def update(self, time_passed_seconds):
        self.top.update(time_passed_seconds)
        self.bottom.update(time_passed_seconds)
        
        for elem in self.body_elems:
            elem.update(time_passed_seconds)
    
    def collide_any(self, obj):
        collided = False
        collided = collided or self.top.collide_any(obj)
        collided = collided or self.bottom.collide_any(obj)
        for elem in self.body_elems:
            collided = collided or elem.collide_any(obj)
        return collided
        