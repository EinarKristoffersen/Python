'''
Created on 4. aug. 2014

@author: Criblica
'''

import Vector.Vector2D
from Constants import Constants as C
import pygame

class Text():
    def __init__(self, text, font_size, text_color):
        self.color = text_color
        pygame.font.init()
        self.font = pygame.font.Font(None, font_size)
        self.finalText = self.font.render(text, True, self.color)
        self.size = self.font.size(text)
        self.textRect = self.finalText.get_rect()
    
    def get_size(self):
        x, y = self.size
        return Vector(x, y)
    
    def set_pos(self, pos):
        self.textRect.x = pos.x
        self.textRect.y = pos.y
    
    def draw(self):
        C.SCREEN.blit(self.finalText, self.textRect)
    
    def update(self, text):
        self.finalText = self.font.render(text, True, self.color)
        