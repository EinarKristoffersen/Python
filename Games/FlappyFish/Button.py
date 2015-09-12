'''
Created on 6. sep. 2015

@author: Einar
'''

from Constants import Constants as C
import pygame
#from pygame.locals import *
pygame.init()

class Button:
    def __init__(self, btn_id, btn_text, default=True):
        self.text = btn_text
        self.id = btn_id
        
    def set_pos(self, pos):
        self.pos = pos
        self.rect = pygame.Rect(pos.x,pos.y, C.BTN_WIDTH, C.BTN_HEIGHT)
    
    def draw(self):
        self.draw_button(C.SCREEN, C.BTN_COLOR, C.BTN_WIDTH, C.BTN_HEIGHT, self.pos.x, self.pos.y, 0)
        self.write_text(C.SCREEN, self.text, C.BTN_TEXT_COLOR, C.BTN_WIDTH, C.BTN_HEIGHT, self.pos.x, self.pos.y)
        
    """def create_button(self, surface, color, x, y, length, height, width, text_color):
        self.rect = pygame.Rect(x,y, length, height)
        surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, self.text, text_color, length, height, x, y)
        return surface
    """
    def write_text(self, surface, text, text_color, length, height, x, y):
        #font_size = int(length//len(text))
        font_size = int(height) - 15
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface

    def draw_button(self, surface, color, length, height, x, y, width):           
        for i in range(1,10):
            s = pygame.Surface((length+(i*2),height+(i*2)))
            s.fill(color)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x-i,y-i,length+i,height+i), width)
            surface.blit(s, (x-i,y-i))
        pygame.draw.rect(surface, color, (x,y,length,height), 0)
        pygame.draw.rect(surface, color, (x,y,length,height), 1)
        #pygame.draw.rect(surface, (190,190,190), (x,y,length,height), 1)  
        return surface

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False
