import pygame

SCREEN_SIZE = (480,600)
SCREEN_TITLE = 'Tetris'
FPS = 60
SCREEN_BG = (128, 128, 128)
COLS, ROWS = 20, 20
CELL = 30
GRID_COLOUR = (0, 0, 0)

class Font:
    TITLE_FONT = pygame.font.Font("assets/PressStart2P-Regular.ttf", 24)
    BUTTON_FONT = pygame.font.SysFont('Consolas', 20)
    IN_GAME_FONT = pygame.font.SysFont('Consolas', 18)