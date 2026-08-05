import pygame

SCREEN_SIZE = (640, 700)
SCREEN_TITLE = 'Tetris'
FPS = 60
COLS, ROWS = 10, 20
CELL = 30

BOARD_WIDTH = COLS * CELL   # 300
SIDEBAR_X = BOARD_WIDTH     # 300
SIDEBAR_WIDTH = SCREEN_SIZE[0] - BOARD_WIDTH  # 340


class Files:
    SCORE_FILE = "src/scores"


class Theme:
    BG = (6, 6, 10)
    PANEL_BG = (12, 10, 18)
    GRID_LINE = (40, 20, 50)
    TEXT_PRIMARY = (57, 255, 20)      # neon green
    TEXT_SECONDARY = (0, 220, 255)    # neon cyan
    ACCENT = (255, 0, 170)            # neon magenta

    BUTTON_BG = (6, 6, 10)             # buttons are outlined, not filled
    BUTTON_HOVER = (20, 20, 30)
    BUTTON_START = (57, 255, 20)       # neon green outline
    BUTTON_PAUSE = (255, 0, 170)       # neon magenta outline
    BUTTON_RESTART = (0, 220, 255)     # neon cyan outline


# kept for anything still referencing these names directly
SCREEN_BG = Theme.BG
GRID_COLOUR = Theme.GRID_LINE


class Font:
    TITLE_FONT = pygame.font.Font("assets/PressStart2P-Regular.ttf", 24)
    BUTTON_FONT = pygame.font.SysFont('Consolas', 20)
    IN_GAME_FONT = pygame.font.Font("assets/PressStart2P-Regular.ttf", 14)