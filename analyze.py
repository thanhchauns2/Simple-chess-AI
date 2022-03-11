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

def counting_pieces(board):
    count = {
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
    for i in range(8):
        for j in range(8):
            count[board[i][j]] += 1
    return count

def check_late_using_dict(count):
    if count['q'] == 1 and count['b'] + count['n'] + count['r'] >= 2:
        return False
    elif count['Q'] == 1 and count['B'] + count['N'] + count['R'] >= 2:
        return False
    elif count['q'] > 1:
        return False
    elif count['Q'] > 1:
        return False
    return True

def analyze_current_state(board):
    white = 0
    black = 0
    late = check_late(board)
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'k':
                white += 900
                if late:
                    white += evaluate['k']['late'][i][j]
                else:
                    white += evaluate['k']['early'][i][j]
            elif board[i][j] == 'K':
                black -= 900
                if late:
                    black += evaluate['K']['late'][i][j]
                else:
                    black += evaluate['K']['early'][i][j]
            elif board[i][j] in white_pieces:
                white += pieces[board[i][j]]
                white += evaluate[board[i][j]][i][j]
            else:
                black += pieces[board[i][j]]
                black += evaluate[board[i][j]][i][j]
    return white + black

def analyze_next_state(current_point, old_pos, new_pos, moving_piece, captured_piece, before):
    point = current_point
    state_1 = 'early'
    state_2 = 'early'
    if check_late_using_dict(before):
        state_1 = 'late'
    before[captured_piece] -= 1
    if check_late_using_dict(before):
        state_2 = 'late'
    before[captured_piece] += 1
    if moving_piece == 'k':
        point -= evaluate['k'][state_1][old_pos[0]][old_pos[1]]
        point += evaluate['k'][state_2][new_pos[0]][new_pos[1]]
    elif moving_piece == 'K':
        point -= evaluate['K'][state_1][old_pos[0]][old_pos[1]]
        point += evaluate['K'][state_2][new_pos[0]][new_pos[1]]
    else:
        point -= evaluate[moving_piece][old_pos[0]][old_pos[1]]
        point += evaluate[moving_piece][new_pos[0]][new_pos[1]]
    if captured_piece == 'k':
        point -= evaluate['k'][state_1][new_pos[0]][new_pos[1]]
    elif captured_piece == 'K':
        point -= evaluate['K'][state_1][new_pos[0]][new_pos[1]]
    else:
        point -= evaluate[captured_piece][new_pos[0]][new_pos[1]]
    point -= pieces[captured_piece]
    return point

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

def get_available_moves_multiple_pieces(board, pieces):
    available_moves = []
    for x in range(8):
        for y in range(8):
            for i in pieces:
                if is_valid(board, (x, y), (i[0], i[1])):
                    available_moves.append([i, (x, y)])
    return available_moves

def get_black_available_moves(board):
    pieces = []
    for i in range(8):
        for j in range(8):
            if board[i][j] in black_pieces:
                pieces.append((i, j))
    return get_available_moves_multiple_pieces(board, pieces)

def get_white_available_moves(board):
    pieces = []
    for i in range(8):
        for j in range(8):
            if board[i][j] in white_pieces:
                pieces.append((i, j))
    return get_available_moves_multiple_pieces(board, pieces)

def white_king_dead(board):
    available_moves = []
    m, n = wk.get_pos()
    available_moves = get_available_moves(board, m, n)
    available_moves.append((m, n))
    for (x, y) in available_moves:
        board[x][y], board[m][n] = board[m][n], board[x][y]
        ck = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] in black_pieces:
                    if is_valid(board, (x, y), (i, j)):
                        ck = 1
                        break
        board[x][y], board[m][n] = board[m][n], board[x][y]
        if ck == 0:
            return False
    return True

def black_king_dead(board):
    available_moves = []
    m, n = bk.get_pos()
    available_moves = get_available_moves(board, m, n)
    available_moves.append((m, n))
    for (x, y) in available_moves:
        board[x][y], board[m][n] = board[m][n], board[x][y]
        ck = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] in white_pieces:
                    if is_valid(board, (x, y), (i, j)):
                        ck = 1
                        break
        board[x][y], board[m][n] = board[m][n], board[x][y]
        if ck == 0:
            return False
    return True