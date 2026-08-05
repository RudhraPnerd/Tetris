import pygame
from game import config

class Pause:
    BG = (0, 0, 0, 160)
    PAUSE_TITLE = config.Font.TITLE_FONT.render("PAUSED", True, (240, 240, 240))
    RESUME_HINT = config.Font.IN_GAME_FONT.render("Click Resume to continue", True, (200, 200, 200))

class Home:
    TITLE = config.Font.TITLE_FONT.render("TETRIS", True, (240, 240, 240))

class GameOver:
    BG = (0, 0, 0, 180)
    TITLE = config.Font.TITLE_FONT.render("GAME OVER", True, (240, 60, 60))
    HINT = config.Font.IN_GAME_FONT.render("Click Restart to play again", True, (200, 200, 200))