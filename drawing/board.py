import pygame, copy
from config import *
from drawing.pieces import *
from evaluation import *

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

def make_moves(board = [], old_pos = (0, 0), new_pos = (0, 0)):
    board[new_pos[0]][new_pos[1]] = board[old_pos[0]][old_pos[1]]
    board[old_pos[0]][old_pos[1]] = ' '
    if old_pos[1] == 7 and board[new_pos[0]][new_pos[1]] == 'P':
        board[new_pos[0]][new_pos[1]] = 'Q'
    if old_pos[1] == 0 and board[new_pos[0]][new_pos[1]] == 'p':
        board[new_pos[0]][new_pos[1]] = 'q'

def new_board():
    board = [['R', 'P', ' ', ' ', ' ', ' ', 'p', 'r'],
             ['N', 'P', ' ', ' ', ' ', ' ', 'p', 'n'],
             ['B', 'P', ' ', ' ', ' ', ' ', 'p', 'b'],
             ['Q', 'P', ' ', ' ', ' ', ' ', 'p', 'q'],
             ['K', 'P', ' ', ' ', ' ', ' ', 'p', 'k'],
             ['B', 'P', ' ', ' ', ' ', ' ', 'p', 'b'],
             ['N', 'P', ' ', ' ', ' ', ' ', 'p', 'n'],
             ['R', 'P', ' ', ' ', ' ', ' ', 'p', 'r']]
    return board

def is_valid(board, new_pos, old_pos):
    if new_pos[0] < 0 or new_pos[0] > 7 or new_pos[1] < 0 or new_pos[1] > 7:
        return False
    if color[board[new_pos[0]][new_pos[1]]] == color[board[old_pos[0]][old_pos[1]]]:
        return False
    piece = board[old_pos[0]][old_pos[1]]
    if piece in black_pieces:
        if bk.being_checked(board):
            if piece == 'P':
                if not bp.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(temp_board, old_pos, new_pos)
                if bk.being_checked(temp_board):
                    return False
            elif piece == 'R':
                if br.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(temp_board, old_pos, new_pos)
                if bk.being_checked(temp_board):
                    return False
            elif piece == 'N':
                if bn.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(temp_board, old_pos, new_pos)
                if bk.being_checked(temp_board):
                    return False
            elif piece == 'B':
                if bb.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(temp_board, old_pos, new_pos)
                if bk.being_checked(temp_board):
                    return False
            elif piece == 'K':
                if bk.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(temp_board, old_pos, new_pos)
                if bk.being_checked(temp_board):
                    return False
            elif piece == 'Q':
                if bq.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(temp_board, old_pos, new_pos)
                if bk.being_checked(temp_board):
                    return False
            return True
    else:
        if wk.being_checked(board):
            if piece == 'p':
                if not wp.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(temp_board, old_pos, new_pos)
                if wk.being_checked(temp_board):
                    return False
            elif piece == 'r':
                if wr.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(temp_board, old_pos, new_pos)
                if wk.being_checked(temp_board):
                    return False
            elif piece == 'n':
                if wn.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(temp_board, old_pos, new_pos)
                if wk.being_checked(temp_board):
                    return False
            elif piece == 'b':
                if wb.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(temp_board, old_pos, new_pos)
                if wk.being_checked(temp_board):
                    return False
            elif piece == 'k':
                if wk.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(temp_board, old_pos, new_pos)
                if wk.being_checked(temp_board):
                    return False
            elif piece == 'q':
                if wq.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(temp_board, old_pos, new_pos)
                if wk.being_checked(temp_board):
                    return False
            return True
    if piece == 'p':
        return wp.is_valid(board, old_pos, new_pos)
    elif piece == 'r':
        return wr.is_valid(board, old_pos, new_pos)
    elif piece == 'n':
        return wn.is_valid(board, old_pos, new_pos)
    elif piece == 'b':
        return wb.is_valid(board, old_pos, new_pos)
    elif piece == 'k':
        return wk.is_valid(board, old_pos, new_pos)
    elif piece == 'q':
        return wq.is_valid(board, old_pos, new_pos)
    elif piece == 'P':
        return bp.is_valid(board, old_pos, new_pos)
    elif piece == 'R':
        return br.is_valid(board, old_pos, new_pos)
    elif piece == 'N':
        return bn.is_valid(board, old_pos, new_pos)
    elif piece == 'B':
        return bb.is_valid(board, old_pos, new_pos)
    elif piece == 'K':
        return bk.is_valid(board, old_pos, new_pos)
    elif piece == 'Q':
        return bq.is_valid(board, old_pos, new_pos)
    return True
