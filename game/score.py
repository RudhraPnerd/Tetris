SCORE = 0
HIGH_SCORE = 0

LINE_POINTS = {0: 0, 1: 50, 2: 150, 3: 200, 4: 250}

def add_lines(lines_cleared):
    global SCORE, HIGH_SCORE
    SCORE += LINE_POINTS.get(lines_cleared, 0)
    if SCORE > HIGH_SCORE:
        HIGH_SCORE = SCORE

def reset():
    global SCORE
    SCORE = 0