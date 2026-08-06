import pygame
from game import config

BUTTON_W, BUTTON_H = 140, 44
CENTER_X = (config.SCREEN_SIZE[0] - BUTTON_W) // 2

start = pygame.Rect((config.SCREEN_SIZE[0] - BUTTON_W) // 2, 320, BUTTON_W, BUTTON_H)
pause = pygame.Rect(config.SIDEBAR_X + 30, 40, BUTTON_W, BUTTON_H)
restart_button = pygame.Rect((config.SCREEN_SIZE[0] - BUTTON_W) // 2, 400, BUTTON_W, BUTTON_H)

class Settings:
    class Difficulties:
        difficulty_easy = pygame.Rect(CENTER_X, 240, 140, 44)
        difficulty_normal = pygame.Rect(CENTER_X, 300, 140, 44)
        difficulty_hard = pygame.Rect(CENTER_X, 360, 140, 44)

    settings = pygame.Rect(CENTER_X, 340, 140, 44)
    back = pygame.Rect(CENTER_X, 440, 140, 44)
