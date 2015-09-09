'''
Created on 5. sep. 2015

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
    SCREEN_SIZE = Vector(1366, 768)
    SCREEN = pygame.display.set_mode((SCREEN_SIZE.x, SCREEN_SIZE.y), 0, 32)
    pygame.display.set_caption('Boids')
    modes = pygame.display.list_modes()
    if modes:
        SCREEN = pygame.display.set_mode(modes[0], pygame.FULLSCREEN)
    
    """
        BOIDS
    """ 
    TOTAL_BOIDS_NUM = 100
    ON_CLICK_CREATE_BOIDS_NUM = 5
    BOID_RADIUS = 3
    BOID_TAIL_LENGTH = 8
    BOID_COLOR = (200, 200, 200)
    BOID_VELOCITY = 150
    BOID_MIN_DISTANCE = 100
    BOID_MAX_DISTANCE = 150
    
    """
        HOIK
    """
    TOTAL_HOIKS_NUM = 1
    HOIK_RADIUS = 8.0
    HOIK_COLOR = (153, 0, 204)
    HOIK_VELOCITY = 190
    
    """
        Obstacle
    """
    TOTAL_OBSTACLE_NUM = 12
    OBSTACLE_RADIUS_MIN = 10
    OBSTACLE_RADIUS_MAX = 50
    OBSTACLE_COLOR = (0, 255, 0)
    
    """    
        Food
    """
    FOOD_COLOR = (255, 10, 10)
    FOOD_RADIUS = 1
    TOTAL_FOOD_NUM = 5