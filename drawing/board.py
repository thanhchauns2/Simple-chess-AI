import pygame
from config import *

def new_chess_board():
    screen = pygame.display.set_mode(screen_size)
    screen.fill(screen_color)
    block_size = screen_size[0] / 8
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                continue
            pygame.draw.rect(screen, black_block, (i * block_size, j * block_size, block_size, block_size))
    return screen

def new_board():
    # board = [['R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R'],
    #          ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    #          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    #          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    #          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    #          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    #          ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    #          ['r', 'n', 'b', 'k', 'q', 'b', 'n', 'r']]
    board = [['R', 'P', ' ', ' ', ' ', ' ', 'p', 'r'],
             ['N', 'P', ' ', ' ', ' ', ' ', 'p', 'n'],
             ['B', 'P', ' ', ' ', ' ', ' ', 'p', 'b'],
             ['Q', 'P', ' ', ' ', ' ', ' ', 'p', 'q'],
             ['K', 'P', ' ', ' ', ' ', ' ', 'p', 'k'],
             ['B', 'P', ' ', ' ', ' ', ' ', 'p', 'b'],
             ['N', 'P', ' ', ' ', ' ', ' ', 'p', 'n'],
             ['R', 'P', ' ', ' ', ' ', ' ', 'p', 'r']]
    return board