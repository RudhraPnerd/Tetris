import os
from game import config

SCORE = 0
HIGH_SCORE = 0

LINE_POINTS = {0: 0, 1: 40, 2: 100, 3: 300, 4: 1200}


def load_high_score():
    global HIGH_SCORE
    if os.path.exists(config.Files.SCORE_FILE):
        with open(config.Files.SCORE_FILE, 'r') as f:
            content = f.read().strip()
            if content.isdigit():
                HIGH_SCORE = int(content)


def save_high_score():
    os.makedirs(os.path.dirname(config.Files.SCORE_FILE), exist_ok=True)
    with open(config.Files.SCORE_FILE, 'w') as f:
        f.write(str(HIGH_SCORE))


def add_lines(lines_cleared):
    global SCORE, HIGH_SCORE
    SCORE += LINE_POINTS.get(lines_cleared, 0)
    if SCORE > HIGH_SCORE:
        HIGH_SCORE = SCORE
        save_high_score()


def reset():
    global SCORE
    SCORE = 0
