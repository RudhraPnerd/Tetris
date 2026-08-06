import pygame
from game import config

BUTTON_W, BUTTON_H = 140, 44
CENTER_X = (config.SCREEN_SIZE[0] - BUTTON_W) // 2

start = pygame.Rect(CENTER_X, 280, BUTTON_W, BUTTON_H)
pause = pygame.Rect(config.SIDEBAR_X + 30, 40, BUTTON_W, BUTTON_H)
home_button = pygame.Rect(config.SIDEBAR_X + 30, 100, BUTTON_W, BUTTON_H)
restart_button = pygame.Rect(CENTER_X, 400, BUTTON_W, BUTTON_H)


class Settings:
    settings = pygame.Rect(CENTER_X, 340, BUTTON_W, BUTTON_H)
    back = pygame.Rect(CENTER_X, 440, BUTTON_W, BUTTON_H)

    class Difficulties:
        difficulty_easy = pygame.Rect(CENTER_X, 240, BUTTON_W, BUTTON_H)
        difficulty_normal = pygame.Rect(CENTER_X, 300, BUTTON_W, BUTTON_H)
        difficulty_hard = pygame.Rect(CENTER_X, 360, BUTTON_W, BUTTON_H)
