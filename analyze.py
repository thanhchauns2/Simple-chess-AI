from evaluation import *
from draw import *
from drawing.pieces import *

def check_late(board):
    minor_white_pieces = 0
    minor_black_pieces = 0
    white_queen = 0
    black_queen = 0
    for i in board:
        minor_white_pieces += i.count('r') + i.count('b') + i.count('n')
        minor_black_pieces += i.count('R') + i.count('B') + i.count('N')
        white_queen += i.count('q')
        black_queen += i.count('Q')
    serial = (white_queen == 0 or (white_queen == 1 and minor_white_pieces == 1)) + (black_queen == 0 or (black_queen == 1 and minor_black_pieces == 1))
    return serial == 2


def analyze_current_state(board):
    white = 0
    black = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'p':
                white += 10
                white += white_pawn_board[i][j]
            elif board[i][j] == 'P':
                black += 10
                black += black_pawn_board[i][j]
            elif board[i][j] == 'r':
                white += 50
                white += white_rook_board[i][j]
            elif board[i][j] == 'R':
                black += 50
                black += black_rook_board[i][j]
            elif board[i][j] == 'n':
                white += 30
                white += white_knight_board[i][j]
            elif board[i][j] == 'N':
                black += 30
                black += black_knight_board[i][j]
            elif board[i][j] == 'b':
                white += 30
                white += white_bishop_board[i][j]
            elif board[i][j] == 'B':
                black += 30
                black += black_bishop_board[i][j]
            elif board[i][j] == 'q':
                white += 90
                white += white_queen_board[i][j]
            elif board[i][j] == 'Q':
                black += 90
                black += black_queen_board[i][j]
            elif board[i][j] == 'k':
                white += 900
                if (check_late(board)):
                    white += white_king_late_board[i][j]
                else:
                    white += white_king_early_board[i][j]
            elif board[i][j] == 'K':
                black += 900
                if (check_late(board)):
                    black += black_king_late_board[i][j]
                else:
                    black += black_king_early_board[i][j]
    return white - black

def check_end_game(board):
    if white_king_dead(board):
        return -1
    elif black_king_dead(board):
        return 1
    return 0

def get_available_moves(board, i, j):
    available_moves = []
    for x in range(8):
        for y in range(8):
            if is_valid(board, (x, y), (i, j)):
                available_moves.append((x, y))
    return available_moves

def white_king_dead(board):
    available_moves = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'k':
                available_moves = get_available_moves(board, i, j)
                available_moves.append((i, j))
                break
    for i in range(8):
        for j in range(8):
            if board[i][j] in black_pieces:
                for x, y in available_moves:
                    if not is_valid(board, (x, y), (i, j)):
                        return False
    return True

def black_king_dead(board):
    available_moves = []
    m, n = 0, 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'K':
                available_moves = get_available_moves(board, i, j)
                available_moves.append((i, j))
                m, n = i, j
                break
    # print(available_moves)
    for (x, y) in available_moves:
        board[x][y], board[m][n] = board[m][n], board[x][y]
        ck = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] in white_pieces:
                    # if board[i][j] == 'q':
                        # print(i, j, x, y, is_valid(board, (x, y), (i, j)))
                    if is_valid(board, (x, y), (i, j)):
                        ck = 1
                        break
        board[x][y], board[m][n] = board[m][n], board[x][y]
        if ck == 0:
            # print(x, y)
            return False
    return True