'''
Created on 6. sep. 2015

@author: Einar
'''

import pygame
import random
from Vector import Vector
from Constants import Constants as C
from Variables import Variables as var
from Menus import MainMenu, GameOverMenu
from HighScore import HighScore
from MovingObjects import Fish, Pipe
from Text import Text

class Game():
    def __init__(self):
        self.setup()
        self.run()
        
    def setup(self):        
        self.clock = pygame.time.Clock()
        
        self.main_menu = MainMenu()
        self.game_over_menu = GameOverMenu()
        self.highscore = HighScore()
        
        self.fish = Fish()
        self.pipes = []
        self.score_text = Text(C.SCORE_TEXT+str(var.score), C.SCORE_TEXT_FONT_SIZE, C.SCORE_TEXT_COLOR)
        self.highscore_text = Text(C.HIGHSCORE_TEXT+str(self.highscore.highscore), C.SCORE_TEXT_FONT_SIZE, C.SCORE_TEXT_COLOR)
        score_size = self.score_text.get_size()
        highscore_size = self.highscore_text.get_size()
        self.score_text.set_pos(Vector(C.SCORE_TEXT_POS.x, C.SCORE_TEXT_POS.y-score_size.y/2))
        self.highscore_text.set_pos(Vector(C.SCREEN_SIZE.x-highscore_size.x-C.SCORE_TEXT_POS.x, C.SCORE_TEXT_POS.y-highscore_size.y/2))
    
    def run(self):
        while(True):
            #show menu
            while(not var.game_started or var.paused):
                time_passed_seconds = self.fps_count()
                self.detect_events(time_passed_seconds)
                self.draw_background()
                self.main_menu.draw()
                self.update_screen()
            
            #game started
            while(var.game_started and not var.paused):
                distance = random.randint(C.MIN_PIPE_DISTANCE, C.MAX_PIPE_DISTANCE)
                if len(self.pipes) == 0 or self.pipes[-1].get_x_pos() < C.SCREEN_SIZE.x-distance:
                    self.gen_pipe_pair()
                    
                self.check_for_passed_pipes()
                
                time_passed_seconds = self.fps_count()
                self.detect_events(time_passed_seconds)
                self.draw_background()
                self.draw_playground()
                self.update_playground(time_passed_seconds)
                self.remove_pipes_outside_screen()
                self.check_for_pipe_collision()  
                
                if(var.game_over):
                    self.game_over()
                
            
    def detect_events(self, time_passed_seconds):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not var.game_started or var.paused:
                    self.main_menu.button_press_actions(pygame.mouse.get_pos())
                elif var.game_over:
                    self.game_over_menu.button_press_actions(pygame.mouse.get_pos(), self.fish)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    var.paused = True
                if event.key == pygame.K_SPACE:
                    self.fish.dir.y = C.FISH_THRUST*time_passed_seconds
    
    def fps_count(self):
        time_passed = self.clock.tick(C.FPS)
        return time_passed / 1000.0
    
    def check_for_passed_pipes(self):
        for pipe in self.pipes:
            if not pipe.passed and pipe.get_x_pos() <= C.FISH_CONSTANT_POS_X:
                pipe.passed = True
                var.score += 0.5
    
    def draw_background(self):
        area = (0, 0, C.SCREEN_SIZE.x, C.SCREEN_SIZE.y) 
        pygame.draw.rect(C.SCREEN, (144,211,255), area)
        
    def draw_score_screen(self):
        area = (0,0, C.SCREEN_SIZE.x, C.SCORE_SCREEN_HEIGHT) 
        pygame.draw.rect(C.SCREEN, C.SCORE_SCREEN_COLOR, area)
        self.score_text.draw()
        self.highscore_text.draw()
    
    def draw_playground(self):
        self.draw_score_screen()
        self.fish.draw()
        for pipe in self.pipes:
            pipe.draw()
    
    def update_playground(self, time_passed_seconds):
        self.score_text.update(C.SCORE_TEXT+str(int(var.score)))
        highscore_size = self.highscore_text.get_size()
        self.highscore_text.set_pos(Vector(C.SCREEN_SIZE.x-highscore_size.x-C.SCORE_TEXT_POS.x, C.SCORE_TEXT_POS.y-highscore_size.y/2))
        self.fish.update(time_passed_seconds)
        for pipe in self.pipes:
            pipe.update(time_passed_seconds)
        self.update_screen()
        
    
    def update_screen(self):
        pygame.display.update()
    
    def gen_pipe_pair(self):
        floor_body_num = random.randint(0, C.AVAIL_PIPE_BODY_SPACE)
        roof_body_num = C.AVAIL_PIPE_BODY_SPACE-floor_body_num
        
        floor_pipe = Pipe(floor_body_num)
        roof_pipe = Pipe(roof_body_num)
        
        floor_pipe.set_pos_floor(Vector(C.SCREEN_SIZE.x, C.SCREEN_SIZE.y-C.PIPE_HEIGHT))
        roof_pipe.set_pos_roof(Vector(C.SCREEN_SIZE.x, C.SCORE_SCREEN_HEIGHT))
        
        self.pipes.append(floor_pipe)
        self.pipes.append(roof_pipe)
        
    def check_for_pipe_collision(self):
        for pipe in self.pipes:
            if pipe.collide_any(self.fish):
                var.game_over = True
                return
    
    def remove_pipes_outside_screen(self):
        for pipe in self.pipes:
            if pipe.get_x_pos()+C.PIPE_WIDTH <= 0:
                self.pipes.remove(pipe)
                
    def remove_all_pipes(self):
        for pipe in self.pipes:
            self.pipes.remove(pipe)
        self.pipes = []
            
    def game_over(self):
        game_over_text = Text(C.GAME_OVER_TEXT, C.GAME_OVER_FONT_SIZE, C.GAME_OVER_TEXT_COLOR)
        final_score_text = Text(C.SCORE_TEXT+str(int(var.score)), C.GAME_OVER_FONT_SIZE, C.GAME_OVER_TEXT_COLOR)
        
        game_over_text_size = game_over_text.get_size()
        final_score_text_size = final_score_text.get_size()
        
        game_over_menu_height = self.game_over_menu.get_height()
        
        text_pos_y = C.SCREEN_SIZE.y/2-(C.DISTANCE_BETWEEN_GAME_OVER_UNITS + game_over_text_size.y + final_score_text_size.y + game_over_menu_height)/2
        game_over_text.set_pos(Vector(C.SCREEN_SIZE.x/2-game_over_text_size.x/2, text_pos_y))
        text_pos_y += game_over_text_size.y + C.DISTANCE_BETWEEN_GAME_OVER_UNITS
        final_score_text.set_pos(Vector(C.SCREEN_SIZE.x/2-final_score_text_size.x/2, text_pos_y))
        text_pos_y += final_score_text_size.y + C.DISTANCE_BETWEEN_GAME_OVER_UNITS
        self.game_over_menu.set_pos(Vector(C.SCREEN_SIZE.x/2-C.BTN_WIDTH/2, text_pos_y))
        
        self.remove_all_pipes()
        self.highscore.set_highscore_if_needed(var.score)
        
        while(var.game_over):
            time_passed_seconds = self.fps_count()
            self.detect_events(time_passed_seconds)   
            self.draw_background()
            game_over_text.draw()
            final_score_text.draw()
            self.game_over_menu.draw()
            self.update_screen()
        
if __name__ == "__main__":
    game = Game()