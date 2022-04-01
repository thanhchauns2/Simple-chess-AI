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

def make_moves(state, old_pos = (0, 0), new_pos = (0, 0)):
    if state.board[old_pos[0]][old_pos[1]] in black_pieces:

        state.pieces_counting[state.board[new_pos[0]][new_pos[1]]] -= 1

        if state.board[new_pos[0]][new_pos[1]] in white_pieces:
            state.white_pieces_list.remove(new_pos)
        state.black_pieces_list.append(new_pos)
        state.black_pieces_list.remove(old_pos)

        if state.board[old_pos[0]][old_pos[1]] == 'K':
            if old_pos == (4, 0) and new_pos == (6, 0):
                state.board[4][0] = ' '
                state.board[5][0] = 'R'
                state.board[6][0] = 'K'
                state.board[7][0] = ' '
                state.black_pieces_list.remove((4, 0))
                state.black_pieces_list.append((6, 0))
                state.black_pieces_list.append((5, 0))
                state.black_pieces_list.remove((7, 0))
                bk.moved = True
                return 0
            elif old_pos == (4, 0) and new_pos == (2, 0):
                state.board[4][0] = ' '
                state.board[3][0] = 'R'
                state.board[2][0] = 'K'
                state.board[0][0] = ' '
                state.black_pieces_list.remove((4, 0))
                state.black_pieces_list.append((2, 0))
                state.black_pieces_list.append((3, 0))
                state.black_pieces_list.remove((0, 0))
                bk.moved = True
                return 0
            bk.moved = True

        state.board[new_pos[0]][new_pos[1]] = state.board[old_pos[0]][old_pos[1]]
        state.board[old_pos[0]][old_pos[1]] = ' '
        if new_pos[1] == 7 and state.board[new_pos[0]][new_pos[1]] == 'P':
            state.board[new_pos[0]][new_pos[1]] = 'Q'
            state.pieces_counting['Q'] += 1
            state.pieces_counting['P'] -= 1
            return 1
        return 0
    else:
        state.pieces_counting[state.board[new_pos[0]][new_pos[1]]] -= 1

        if state.board[new_pos[0]][new_pos[1]] in black_pieces:
            state.black_pieces_list.remove(new_pos)
        state.white_pieces_list.append(new_pos)
        state.white_pieces_list.remove(old_pos)

        if state.board[old_pos[0]][old_pos[1]] == 'k':
            if old_pos == (4, 7) and new_pos == (6, 7):
                state.board[4][7] = ' '
                state.board[5][7] = 'r'
                state.board[6][7] = 'k' 
                state.board[7][7] = ' '
                for k in state.board:
                    print(k)
                for k in state.white_pieces_list:
                    print(k)
                state.white_pieces_list.remove((4, 7))
                state.white_pieces_list.append((6, 7))
                state.white_pieces_list.append((5, 7))
                state.white_pieces_list.remove((7, 7))
                wk.moved = True
                return 0
            elif old_pos == (4, 7) and new_pos == (2, 7):
                state.board[4][7] = ' '
                state.board[3][7] = 'r'
                state.board[2][7] = 'k'
                state.board[0][7] = ' '
                state.white_pieces_list.remove((4, 7))
                state.white_pieces_list.append((2, 7))
                state.white_pieces_list.append((3, 7))
                state.white_pieces_list.remove((0, 7))
                wk.moved = True
                return 0
            wk.moved = True

        state.board[new_pos[0]][new_pos[1]] = state.board[old_pos[0]][old_pos[1]]
        state.board[old_pos[0]][old_pos[1]] = ' '
        if new_pos[1] == 0 and state.board[new_pos[0]][new_pos[1]] == 'p':
            state.board[new_pos[0]][new_pos[1]] = 'q'
            state.pieces_counting['q'] += 1
            state.pieces_counting['p'] -= 1
            return 1
        return 0
    # piece_list[board[new_pos[0]][new_pos[1]]] -= 1
    # if board[old_pos[0]][old_pos[1]] == 'k':
    #     if old_pos == (4, 7) and new_pos == (6, 7):
    #         board[4][7] = ' '
    #         board[5][7] = 'r'
    #         board[6][7] = 'k' 
    #         board[7][7] = ' '
    #         return 0
    #     elif old_pos == (4, 7) and new_pos == (2, 7):
    #         board[4][7] = ' '
    #         board[3][7] = 'r'
    #         board[2][7] = 'k'
    #         board[0][7] = ' '
    #         return 0
    # if board[old_pos[0]][old_pos[1]] == 'K':
    #     if old_pos == (4, 0) and new_pos == (6, 0):
    #         board[4][0] = ' '
    #         board[5][0] = 'R'
    #         board[6][0] = 'K'
    #         board[7][0] = ' '
    #         return 0
    #     elif old_pos == (4, 0) and new_pos == (2, 0):
    #         board[4][0] = ' '
    #         board[3][0] = 'R'
    #         board[2][0] = 'K'
    #         board[0][0] = ' '
    #         return 0
    # board[new_pos[0]][new_pos[1]] = board[old_pos[0]][old_pos[1]]
    # board[old_pos[0]][old_pos[1]] = ' '
    # if new_pos[1] == 7 and board[new_pos[0]][new_pos[1]] == 'P':
    #     board[new_pos[0]][new_pos[1]] = 'Q'
    #     return 1
    # if new_pos[1] == 0 and board[new_pos[0]][new_pos[1]] == 'p':
    #     board[new_pos[0]][new_pos[1]] = 'q'
    #     return 1

def undo_moves(state, old_pos = (0, 0), new_pos = (0, 0), captured_piece = ' ', promoted = 0):
    if state.board[new_pos[0]][new_pos[1]] in black_pieces:

        state.pieces_counting[captured_piece] += 1

        if captured_piece in white_pieces:
            state.white_pieces_list.append(new_pos)
        state.black_pieces_list.remove(new_pos)
        state.black_pieces_list.append(old_pos)

        if state.board[new_pos[0]][new_pos[1]] == 'K':
            if new_pos == (6, 0) and old_pos == (4, 0):
                state.board[4][0] = 'K'
                state.board[5][0] = ' '
                state.board[6][0] = ' '
                state.board[7][0] = 'R'
                state.black_pieces_list.append((7, 0))
                state.black_pieces_list.remove((6, 0))
                state.black_pieces_list.remove((5, 0))
                state.black_pieces_list.append((4, 0))
                return
            elif new_pos == (2, 0) and old_pos == (4, 0):
                state.board[4][0] = 'K'
                state.board[3][0] = ' '
                state.board[2][0] = ' '
                state.board[0][0] = 'R'
                state.black_pieces_list.append((0, 0))
                state.black_pieces_list.remove((2, 0))
                state.black_pieces_list.remove((3, 0))
                state.black_pieces_list.append((4, 0))
                return
        state.board[old_pos[0]][old_pos[1]] = state.board[new_pos[0]][new_pos[1]]
        state.board[new_pos[0]][new_pos[1]] = captured_piece
        if promoted == 1:
            if new_pos[1] == 7:
                state.board[old_pos[0]][old_pos[1]] = 'P'
                state.pieces_counting['P'] += 1
                state.pieces_counting['Q'] -= 1
    
    else:

        state.pieces_counting[captured_piece] += 1

        if captured_piece in black_pieces:
            state.black_pieces_list.append(new_pos)
        state.white_pieces_list.remove(new_pos)
        state.white_pieces_list.append(old_pos)

        if state.board[new_pos[0]][new_pos[1]] == 'k':
            if new_pos == (6, 7) and old_pos == (4, 7):
                state.board[4][7] = 'k'
                state.board[5][7] = ' '
                state.board[6][7] = ' '
                state.board[7][7] = 'r'
                return
            elif new_pos == (2, 7) and old_pos == (4, 7):
                state.board[4][7] = 'k'
                state.board[3][7] = ' '
                state.board[2][7] = ' '
                state.board[0][7] = 'r'
                return
        state.board[old_pos[0]][old_pos[1]] = state.board[new_pos[0]][new_pos[1]]
        state.board[new_pos[0]][new_pos[1]] = captured_piece
        if promoted == 1:
            if new_pos[1] == 0:
                state.board[old_pos[0]][old_pos[1]] = 'p'
                state.pieces_counting['p'] += 1
                state.pieces_counting['q'] -= 1

    # piece_list[captured_piece] += 1
    # if board[new_pos[0]][new_pos[1]] == 'k':
    #     if new_pos == (6, 7) and old_pos == (4, 7):
    #         board[4][7] = 'k'
    #         board[5][7] = ' '
    #         board[6][7] = ' '
    #         board[7][7] = 'r'
    #         return
    #     elif new_pos == (2, 7) and old_pos == (4, 7):
    #         board[4][7] = 'k'
    #         board[3][7] = ' '
    #         board[2][7] = ' '
    #         board[0][7] = 'r'
    #         return
    # if board[new_pos[0]][new_pos[1]] == 'K':
    #     if new_pos == (6, 0) and old_pos == (4, 0):
    #         board[4][0] = 'K'
    #         board[5][0] = ' '
    #         board[6][0] = ' '
    #         board[7][0] = 'R'
    #         return
    #     elif new_pos == (2, 0) and old_pos == (4, 0):
    #         board[4][0] = 'K'
    #         board[3][0] = ' '
    #         board[2][0] = ' '
    #         board[0][0] = 'R'
    #         return
    # board[old_pos[0]][old_pos[1]] = board[new_pos[0]][new_pos[1]]
    # board[new_pos[0]][new_pos[1]] = captured_piece
    # if promoted == 1:
    #     if new_pos[1] == 7:
    #         board[old_pos[0]][old_pos[1]] = 'P'
    #     else:
    #         board[old_pos[0]][old_pos[1]] = 'p'


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

def is_valid(state, new_pos, old_pos):
    if new_pos[0] < 0 or new_pos[0] > 7 or new_pos[1] < 0 or new_pos[1] > 7:
        return False
    if color[state.board[new_pos[0]][new_pos[1]]] == color[state.board[old_pos[0]][old_pos[1]]]:
        return False
    piece = state.board[old_pos[0]][old_pos[1]]
    # if piece in black_pieces:
    #     if bk.being_checked(board):
    #         if piece == 'P':
    #             if not bp.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if bk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'R':
    #             if not br.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if not bk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'N':
    #             if not bn.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if not bk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'B':
    #             if not bb.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if not bk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'K':
    #             if not bk.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if not bk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'Q':
    #             if not bq.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if not bk.being_checked(temp_board):
    #                 return False
    #         return True
    # else:
    #     if wk.being_checked(board):
    #         if piece == 'p':
    #             if not wp.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if wk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'r':
    #             if not wr.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if not wk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'n':
    #             if not wn.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if not wk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'b':
    #             if not wb.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if not wk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'k':
    #             if not wk.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if not wk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'q':
    #             if wq.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if wk.being_checked(temp_board):
    #                 return False
    #         return True
    if piece == 'p':
        return wp.is_valid(state.board, old_pos, new_pos)
    elif piece == 'r':
        return wr.is_valid(state.board, old_pos, new_pos)
    elif piece == 'n':
        return wn.is_valid(state.board, old_pos, new_pos)
    elif piece == 'b':
        return wb.is_valid(state.board, old_pos, new_pos)
    elif piece == 'k':
        return wk.is_valid(state.board, old_pos, new_pos)
    elif piece == 'q':
        return wq.is_valid(state.board, old_pos, new_pos)
    elif piece == 'P':
        return bp.is_valid(state.board, old_pos, new_pos)
    elif piece == 'R':
        return br.is_valid(state.board, old_pos, new_pos)
    elif piece == 'N':
        return bn.is_valid(state.board, old_pos, new_pos)
    elif piece == 'B':
        return bb.is_valid(state.board, old_pos, new_pos)
    elif piece == 'K':
        return bk.is_valid(state.board, old_pos, new_pos)
    elif piece == 'Q':
        return bq.is_valid(state.board, old_pos, new_pos)
    return True

class State:
    def __init__(self):
        self.board = new_board()
        self.pieces_counting = {
            'p': 8,
            'r': 2,
            'n': 2,
            'b': 2,
            'k': 1,
            'q': 1,
            'P': 8,
            'R': 2,
            'N': 2,
            'B': 2,
            'K': 1,
            'Q': 1,
            ' ': 32,
        }
        self.black_pieces_list = [(0, 0), (0, 1),
                                  (1, 0), (1, 1),
                                  (2, 0), (2, 1),
                                  (3, 0), (3, 1),
                                  (4, 0), (4, 1),
                                  (5, 0), (5, 1),
                                  (6, 0), (6, 1),
                                  (7, 0), (7, 1)]
        self.white_pieces_list = [(0, 6), (0, 7),
                                  (1, 6), (1, 7),
                                  (2, 6), (2, 7),
                                  (3, 6), (3, 7),
                                  (4, 6), (4, 7),
                                  (5, 6), (5, 7),
                                  (6, 6), (6, 7),
                                  (7, 6), (7, 7)]
        self.black_position_bitboard = 217020518514230019
        self.white_position_bitboard = 13889313184910721216
        self.black_available_takes_bitboard = 289360691352306692
        self.white_available_takes_bitboard = 2314885530818453536