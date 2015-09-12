'''
Created on 6. sep. 2015

@author: Einar
'''
from Vector import Vector
from Button import Button
from Constants import Constants as C
from Variables import Variables as var

class Menu():
    def __init__(self):
        self.buttons = []
        self.pos_isset = False
    
    def add_button(self, btn_id, btn_text):
        self.buttons.append(Button(btn_id, btn_text))
    
    def set_pos(self, pos):
        for button in self.buttons:
            button.set_pos(Vector(pos.x, pos.y))
            pos.y += C.BTN_HEIGHT+C.BTN_SPACE_BETWEEN
        self.pos_isset = True
    
    def calc_button_pos(self):
        num_buttons = len(self.buttons)
        x = C.SCREEN_SIZE.x/2 - C.BTN_WIDTH/2
        y = C.SCREEN_SIZE.y/2
        
        if num_buttons%2 == 0:
            y -= C.BTN_SPACE_BETWEEN/2
            y -= (num_buttons/2) * C.BTN_HEIGHT
            y -= ((num_buttons/2)-1) * C.BTN_SPACE_BETWEEN
        else:
            y -= C.BTN_HEIGHT/2
            y -= ((num_buttons-1)/2) * C.BTN_HEIGHT
            y -= ((num_buttons-1)/2) * C.BTN_SPACE_BETWEEN
        
        for button in self.buttons:
            button.set_pos(Vector(x, y))
            y += C.BTN_HEIGHT+C.BTN_SPACE_BETWEEN
            
    def get_height(self):
        return C.BTN_HEIGHT*len(self.buttons)+C.BTN_SPACE_BETWEEN*(len(self.buttons)-1)
            
    def draw(self):
        if not self.pos_isset:
            self.calc_button_pos()
        for button in self.buttons:
            button.draw()

class MainMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.add_button(C.BTN_ID_PLAY, C.BTN_TEXT_PLAY)
        self.add_button(C.BTN_ID_QUIT, C.BTN_TEXT_QUIT)
        
    def button_press_actions(self, mouse_pos):
        for button in self.buttons:
            if button.pressed(mouse_pos):
                if button.id == C.BTN_ID_PLAY:
                    var.game_started = True
                    var.paused = False
                elif button.id == C.BTN_ID_QUIT:
                    exit()
    
class GameOverMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.add_button(C.BTN_ID_PLAY, C.BTN_TEXT_TRY_AGAIN)
        self.add_button(C.BTN_ID_BACK, C.BTN_TEXT_BACK)
        
    def button_press_actions(self, mouse_pos, fish):
        for button in self.buttons:
            if button.pressed(mouse_pos):
                var.score = 0
                fish.pos = C.FISH_POS
                fish.dir = C.FISH_DIR
                fish.velocity = C.FISH_VELOCITY
                if button.id == C.BTN_ID_PLAY:
                    var.game_over = False                    
                if button.id == C.BTN_ID_BACK:
                    var.game_over = False
                    var.game_started = False
                
                