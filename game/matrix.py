import pygame
from pieces import Piece, COLORS
import random
import score

COLS, ROWS = 10, 20
CELL = 30
GRID_COLOUR = (40, 40, 50)
grid = [[None for _ in range(COLS)] for _ in range(ROWS)]

FALL_SPEED = 30
fall_timer = 0

piece = Piece("T")
SHAPE_KEYS = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']

paused = False
game_over = False


def draw_grid(screen):
    for row in range(ROWS):
        for col in range(COLS):
            kind = grid[row][col]
            if kind is not None:
                rect = (col * CELL, row * CELL, CELL, CELL)
                pygame.draw.rect(screen, COLORS[kind], rect)
            else:
                rect = (col * CELL, row * CELL, CELL - 1, CELL - 1)
                pygame.draw.rect(screen, GRID_COLOUR, rect, 1)

    for cx, cy in piece.cells():
        rect = (cx * CELL, cy * CELL, CELL, CELL)
        pygame.draw.rect(screen, COLORS[piece.kind], rect)


def update():
    global fall_timer

    if paused or game_over:
        return

    fall_timer += 1

    if fall_timer >= FALL_SPEED:
        fall_timer = 0

        if can_move_down():
            piece.y += 1
        else:
            lock_piece()


def can_move_down():
    for cx, cy in piece.cells():
        ny = cy + 1
        if ny >= ROWS:
            return False
        if grid[ny][cx] is not None:
            return False
    return True


def is_valid(piece_to_check):
    for cx, cy in piece_to_check.cells():
        if cx < 0 or cx >= COLS or cy >= ROWS:
            return False
        if cy >= 0 and grid[cy][cx] is not None:
            return False
    return True


def lock_piece():
    global piece, game_over
    for cx, cy in piece.cells():
        grid[cy][cx] = piece.kind
    clear_lines()
    piece = spawn_new_piece()

    if not is_valid(piece):
        game_over = True


def spawn_new_piece():
    kind = random.choice(SHAPE_KEYS)
    return Piece(kind)


def move(dx, dy):
    for cx, cy in piece.cells():
        nx, ny = cx + dx, cy + dy

        if nx < 0 or nx >= COLS or ny >= ROWS:
            return False
        if ny >= 0 and grid[ny][nx] is not None:
            return False

    piece.x += dx
    piece.y += dy
    return True


def rotate():
    piece.rotation = (piece.rotation + 1) % 4


def soft_drop():
    if can_move_down():
        piece.y += 1


def hard_drop():
    while can_move_down():
        piece.y += 1
    lock_piece()


def clear_lines():
    global grid
    new_grid = [row for row in grid if not all(row)]
    lines_cleared = ROWS - len(new_grid)
    for _ in range(lines_cleared):
        new_grid.insert(0, [None for _ in range(COLS)])

    grid = new_grid
    score.add_lines(lines_cleared)
    return lines_cleared


def toggle_pause():
    global paused
    paused = not paused


def restart():
    global grid, piece, game_over, paused, fall_timer
    grid = [[None for _ in range(COLS)] for _ in range(ROWS)]
    piece = spawn_new_piece()
    game_over = False
    paused = False
    fall_timer = 0
    score.reset()