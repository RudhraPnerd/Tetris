import pygame
from game import config


class Home:
    TITLE = config.Font.TITLE_FONT.render("TETRIS", True, config.Theme.TEXT_PRIMARY)


class Pause:
    BG = (0, 0, 0, 180)
    PAUSE_TITLE = config.Font.TITLE_FONT.render("PAUSED", True, config.Theme.TEXT_SECONDARY)
    RESUME_HINT = config.Font.IN_GAME_FONT.render("Click Resume to continue", True, config.Theme.TEXT_SECONDARY)



class GameOver:
    BG = (0, 0, 0, 200)
    TITLE = config.Font.TITLE_FONT.render("GAME OVER", True, config.Theme.ACCENT)
    HINT = config.Font.IN_GAME_FONT.render("Click Restart to play again", True, config.Theme.ACCENT)


class Settings:
    TITLE = config.Font.TITLE_FONT.render("SETTINGS", True, config.Theme.TEXT_PRIMARY)
    LABEL = config.Font.IN_GAME_FONT.render("Difficulty", True, config.Theme.TEXT_SECONDARY)
