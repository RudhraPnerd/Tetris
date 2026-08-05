import pygame
from game import config

BUTTON_W, BUTTON_H = 140, 44

start = pygame.Rect((config.SCREEN_SIZE[0] - BUTTON_W) // 2, 320, BUTTON_W, BUTTON_H)
pause = pygame.Rect(config.SIDEBAR_X + 30, 40, BUTTON_W, BUTTON_H)
restart_button = pygame.Rect((config.SCREEN_SIZE[0] - BUTTON_W) // 2, 400, BUTTON_W, BUTTON_H)