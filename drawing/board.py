import pygame, copy
from config import *
from drawing.pieces import *
from evaluation import *

temp_piece_list = {
    ' ': 0,
    'p': 0,
    'P': 0,
    'r': 0,
    'R': 0,
    'n': 0,
    'N': 0,
    'b': 0,
    'B': 0,
    'q': 0,
    'Q': 0,
    'k': 0,
    'K': 0
}

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

def make_moves(piece_list = {}, board = [], old_pos = (0, 0), new_pos = (0, 0)):
    piece_list[board[new_pos[0]][new_pos[1]]] -= 1
    if board[old_pos[0]][old_pos[1]] == 'k':
        if old_pos == (4, 7) and new_pos == (6, 7):
            board[4][7] = ' '
            board[5][7] = 'r'
            board[6][7] = 'k'
            board[7][7] = ' '
            return 0
        elif old_pos == (4, 7) and new_pos == (2, 7):
            board[4][7] = ' '
            board[3][7] = 'r'
            board[2][7] = 'k'
            board[0][7] = ' '
            return 0
    if board[old_pos[0]][old_pos[1]] == 'K':
        if old_pos == (4, 0) and new_pos == (6, 0):
            board[4][0] = ' '
            board[5][0] = 'R'
            board[6][0] = 'K'
            board[7][0] = ' '
            return 0
        elif old_pos == (4, 0) and new_pos == (2, 0):
            board[4][0] = ' '
            board[3][0] = 'R'
            board[2][0] = 'K'
            board[0][0] = ' '
            return 0
    board[new_pos[0]][new_pos[1]] = board[old_pos[0]][old_pos[1]]
    board[old_pos[0]][old_pos[1]] = ' '
    if new_pos[1] == 7 and board[new_pos[0]][new_pos[1]] == 'P':
        board[new_pos[0]][new_pos[1]] = 'Q'
        return 1
    if new_pos[1] == 0 and board[new_pos[0]][new_pos[1]] == 'p':
        board[new_pos[0]][new_pos[1]] = 'q'
        return 1

def undo_moves(piece_list = {}, board = [], old_pos = (0, 0), new_pos = (0, 0), captured_piece = ' ', promoted = 0):
    piece_list[captured_piece] += 1
    if board[new_pos[0]][new_pos[1]] == 'k':
        if new_pos == (6, 7) and old_pos == (4, 7):
            board[4][7] = 'k'
            board[5][7] = ' '
            board[6][7] = ' '
            board[7][7] = 'r'
            return
        elif new_pos == (2, 7) and old_pos == (4, 7):
            board[4][7] = 'k'
            board[3][7] = ' '
            board[2][7] = ' '
            board[0][7] = 'r'
            return
    if board[new_pos[0]][new_pos[1]] == 'K':
        if new_pos == (6, 0) and old_pos == (4, 0):
            board[4][0] = 'K'
            board[5][0] = ' '
            board[6][0] = ' '
            board[7][0] = 'R'
            return
        elif new_pos == (2, 0) and old_pos == (4, 0):
            board[4][0] = 'K'
            board[3][0] = ' '
            board[2][0] = ' '
            board[0][0] = 'R'
            return
    board[old_pos[0]][old_pos[1]] = board[new_pos[0]][new_pos[1]]
    board[new_pos[0]][new_pos[1]] = captured_piece
    if promoted == 1:
        if new_pos[1] == 7:
            board[old_pos[0]][old_pos[1]] = 'P'
        else:
            board[old_pos[0]][old_pos[1]] = 'p'


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

def is_valid(board, new_pos, old_pos, piece_list = temp_piece_list):
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
                make_moves(piece_list, temp_board, old_pos, new_pos)
                if bk.being_checked(temp_board):
                    return False
            elif piece == 'R':
                if not br.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(piece_list, temp_board, old_pos, new_pos)
                if not bk.being_checked(temp_board):
                    return False
            elif piece == 'N':
                if not bn.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(piece_list, temp_board, old_pos, new_pos)
                if not bk.being_checked(temp_board):
                    return False
            elif piece == 'B':
                if not bb.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(piece_list, temp_board, old_pos, new_pos)
                if not bk.being_checked(temp_board):
                    return False
            elif piece == 'K':
                if not bk.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(piece_list, temp_board, old_pos, new_pos)
                if not bk.being_checked(temp_board):
                    return False
            elif piece == 'Q':
                if not bq.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(piece_list, temp_board, old_pos, new_pos)
                if not bk.being_checked(temp_board):
                    return False
            return True
    else:
        if wk.being_checked(board):
            if piece == 'p':
                if not wp.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(piece_list, temp_board, old_pos, new_pos)
                if wk.being_checked(temp_board):
                    return False
            elif piece == 'r':
                if not wr.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(piece_list, temp_board, old_pos, new_pos)
                if not wk.being_checked(temp_board):
                    return False
            elif piece == 'n':
                if not wn.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(piece_list, temp_board, old_pos, new_pos)
                if not wk.being_checked(temp_board):
                    return False
            elif piece == 'b':
                if not wb.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(piece_list, temp_board, old_pos, new_pos)
                if not wk.being_checked(temp_board):
                    return False
            elif piece == 'k':
                if not wk.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(piece_list, temp_board, old_pos, new_pos)
                if not wk.being_checked(temp_board):
                    return False
            elif piece == 'q':
                if wq.is_valid(board, old_pos, new_pos):
                    return False
                temp_board = copy.deepcopy(board)
                make_moves(piece_list, temp_board, old_pos, new_pos)
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
