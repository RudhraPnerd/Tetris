import pygame

SCREEN_SIZE = (640, 700)
SCREEN_TITLE = 'Tetris'
FPS = 60
COLS, ROWS = 10, 20
CELL = 30

BOARD_WIDTH = COLS * CELL   
SIDEBAR_X = BOARD_WIDTH     
SIDEBAR_WIDTH = SCREEN_SIZE[0] - BOARD_WIDTH  


class Files:
    SCORE_FILE = "src/scores"


class Theme:
    BG = (6, 6, 10)
    PANEL_BG = (12, 10, 18)
    GRID_LINE = (40, 20, 50)
    TEXT_PRIMARY = (57, 255, 20)      
    TEXT_SECONDARY = (0, 220, 255)    
    ACCENT = (255, 0, 170)            

    BUTTON_BG = (6, 6, 10)             
    BUTTON_HOVER = (255, 255, 255)     
    BUTTON_START = (57, 255, 20)       
    BUTTON_PAUSE = (255, 0, 170)       
    BUTTON_RESTART = (0, 220, 255)     


SCREEN_BG = Theme.BG
GRID_COLOUR = Theme.GRID_LINE


class Font:
    TITLE_FONT = pygame.font.Font("assets/PressStart2P-Regular.ttf", 24)
    BUTTON_FONT = pygame.font.SysFont('Consolas', 20)
    IN_GAME_FONT = pygame.font.Font("assets/PressStart2P-Regular.ttf", 14)
