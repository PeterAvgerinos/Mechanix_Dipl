import pygame
from .constants import BLACK, ROWS, COLS, RED, SQUARE_SIZE, WHITE, BLUE

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.blue_left = 12

    # def draw_squares(self, win):
    #     win.fill(BLACK)
    #     for row in range(ROWS):
    #         for col in range(row % 2, ROWS, 2):
    #             pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # def draw_squares(self, win):
    #     win.fill(BLACK)
    #     k = ROWS - 1
    #     for row in range(ROWS):
    #         for col in range(k):
    #             pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    #
    #         k = k - 1
    #
    #         for col in range(k):
    #             pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_squares(self, win):
        win.fill(BLACK)
        k = ROWS - 1
        for row in range(ROWS):
            for col in range(COLS):
                if (k//2) < COLS//2 - 1:
                    pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                elif k//2 == COLS//2 - 1:
                    pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

