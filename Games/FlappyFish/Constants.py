'''
Created on 6. sep. 2015

@author: Einar
'''
from Vector import Vector
import pygame
pygame.init()
 
class Constants():
    """
        SCREEN
    """
    FPS = 60
    SCREEN_SIZE = Vector(1024, 600)
    SCREEN = pygame.display.set_mode((SCREEN_SIZE.x, SCREEN_SIZE.y), 0, 32)
    pygame.display.set_caption('Flappyfish')
    
    """
        Buttons
    """
    BTN_ID_PLAY = 0
    BTN_ID_MAINMENU = 1
    BTN_ID_QUIT = 2
    BTN_ID_BACK = 3
    
    BTN_TEXT_PLAY = "Play"
    BTN_TEXT_TRY_AGAIN = "Try again"
    BTN_TEXT_MAINMENU = "Main menu"
    BTN_TEXT_QUIT = "Quit game"
    BTN_TEXT_BACK = "Back"
    
    BTN_SPACE_BETWEEN = 20
    BTN_WIDTH = 150
    BTN_HEIGHT = 40
    #BTN_COLOR = (162, 162, 162)
    BTN_COLOR = (47, 111, 208)
    BTN_TEXT_COLOR = (255, 255, 255)
        
    """
        FISH
    """
    FISH_WIDTH = 30
    FISH_HEIGHT = 30
    FISH_POS = Vector(0, SCREEN_SIZE.y/2 - FISH_HEIGHT/2)
    FISH_DIR = Vector(1, 0)
    FISH_VELOCITY = 0.5
    FISH_IMAGE = pygame.image.load("img/fish.gif").convert()
    FISH_GRAVITY = 10
    FISH_CONSTANT_POS_X = 250
    FISH_THRUST = -350
    
    """
        PIPE
    """
    PIPE_DIR = Vector(-1, 0)
    PIPE_VELOCITY = 2
    PIPE_WIDTH = 40
    PIPE_HEIGHT = 50
    PIPE_IMAGE_TOP = pygame.image.load("img/pipe_top.gif").convert()
    PIPE_IMAGE_MID = pygame.image.load("img/pipe_mid.gif").convert()
    PIPE_IMAGE_BOT = pygame.image.load("img/pipe_bot.gif").convert()
    PIPE_ROOF = 0
    PIPE_FLOOR = 1
    PIPE_ROTATION_DEGREE = 180
    SPACE_BETWEEN_OPPOSITE_PIPES = 100
    MIN_PIPE_DISTANCE = 150
    MAX_PIPE_DISTANCE = 600
    
    AVAIL_PIPE_BODY_SPACE = (SCREEN_SIZE.y - SPACE_BETWEEN_OPPOSITE_PIPES - (5*PIPE_HEIGHT))/PIPE_HEIGHT
    

    """
        Game Over
    """
    GAME_OVER_TEXT = "Game Over"
    GAME_OVER_TEXT_COLOR = (255,255,255)
    GAME_OVER_FONT_SIZE = 60
    DISTANCE_BETWEEN_GAME_OVER_UNITS = 30
    
    """
        SCORE SCREEN AND TEXT
    """
    SCORE_SCREEN_WIDTH = SCREEN_SIZE.x
    SCORE_SCREEN_HEIGHT = 50
    SCORE_SCREEN_COLOR = (84, 187, 255)
    
    SCORE_TEXT = "Score: "
    HIGHSCORE_TEXT = "Highscore: "
    SCORE_TEXT_COLOR = (255,255,255)
    SCORE_TEXT_FONT_SIZE = 30
    SCORE_TEXT_POS = Vector(20, SCORE_SCREEN_HEIGHT/2)
    
    
        
        
        