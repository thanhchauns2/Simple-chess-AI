from evaluation import *
from draw import *
from drawing.pieces import *

def check_late(state):
    serial  = (state.pieces_counting['q'] == 0 
           or (state.pieces_counting['q'] == 1 and state.pieces_counting['n'] + state.pieces_counting['r'] + state.pieces_counting['b'] <= 1))
    serial += (state.pieces_counting['Q'] == 0 
           or (state.pieces_counting['Q'] == 1 and state.pieces_counting['N'] + state.pieces_counting['R'] + state.pieces_counting['B'] <= 1))
    return serial == 2

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

def analyze_current_state(state):
    white = 0
    black = 0
    late = check_late(state)

    for (i, j) in state.black_pieces_list:
        if state.board[i][j] == 'K':
            black -= 900
            if late:
                black += evaluate['K']['late'][i][j]
            else:
                black += evaluate['K']['early'][i][j]
        else:
            black += pieces[state.board[i][j]]
            black += evaluate[state.board[i][j]][i][j]
    
    for (i, j) in state.white_pieces_list:
        if state.board[i][j] == 'k':
            white -= 900
            if late:
                white += evaluate['k']['late'][i][j]
            else:
                white += evaluate['k']['early'][i][j]
        else:
            white += pieces[state.board[i][j]]
            white += evaluate[state.board[i][j]][i][j]

    return white + black

    # for i in range(8):
    #     for j in range(8):
    #         if board[i][j] == 'k':
    #             white += 900
    #             if late:
    #                 white += evaluate['k']['late'][i][j]
    #             else:
    #                 white += evaluate['k']['early'][i][j]
    #         elif board[i][j] == 'K':
    #             black -= 900
    #             if late:
    #                 black += evaluate['K']['late'][i][j]
    #             else:
    #                 black += evaluate['K']['early'][i][j]
    #         elif board[i][j] in white_pieces:
    #             white += pieces[board[i][j]]
    #             white += evaluate[board[i][j]][i][j]
    #         else:
    #             black += pieces[board[i][j]]
    #             black += evaluate[board[i][j]][i][j]
    # return white + black

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

def check_end_game(state):
    if state.pieces_counting['k'] == 0:
        return 1
    elif state.pieces_counting['K'] == 0:
        return -1
    return 0

def get_available_moves(board, i, j):
    available_moves = []
    if board[i][j] == 'p':
        available_moves = available_moves + wp.available_moves(board, (i, j))
    elif board[i][j] == 'P':
        available_moves = available_moves + bp.available_moves(board, (i, j))
    elif board[i][j] == 'r':
        available_moves = available_moves + wr.available_moves(board, (i, j))
    elif board[i][j] == 'R':
        available_moves = available_moves + br.available_moves(board, (i, j))
    elif board[i][j] == 'n':
        available_moves = available_moves + wn.available_moves(board, (i, j))
    elif board[i][j] == 'N':
        available_moves = available_moves + bn.available_moves(board, (i, j))
    elif board[i][j] == 'b':
        available_moves = available_moves + wb.available_moves(board, (i, j))
    elif board[i][j] == 'B':
        available_moves = available_moves + bb.available_moves(board, (i, j))
    elif board[i][j] == 'q':
        available_moves = available_moves + wq.available_moves(board, (i, j))
    elif board[i][j] == 'Q':
        available_moves = available_moves + bq.available_moves(board, (i, j))
    elif board[i][j] == 'k':
        available_moves = available_moves + wk.available_moves(board, (i, j))
    elif board[i][j] == 'K':
        available_moves = available_moves + bk.available_moves(board, (i, j))
    return available_moves
    # for x in range(8):
    #     for y in range(8):
    #         if is_valid(board, (x, y), (i, j)):
    #             available_moves.append((x, y))
    # return available_moves

# def get_available_moves_multiple_pieces(board, pieces):
#     available_moves = []
#     for x in pieces:
#         available_moves += get_available_moves(board, x[0], x[1])
#     return available_moves
    # for x in range(8):
    #     for y in range(8):
    #         for i in pieces:
    #             if i == (x, y):
    #                 continue
    #             if is_valid(board, (x, y), (i[0], i[1])):
    #                 available_moves.append([i, (x, y)])
    # return available_moves

def get_black_available_moves(state):
    available_moves = []
    for i in state.black_pieces_list:
        available_moves += get_available_moves(state.board, i[0], i[1])
    return available_moves
    # pieces = []
    # for i in range(8):
    #     for j in range(8):
    #         if board[i][j] in black_pieces:
    #             pieces.append((i, j))
    # return get_available_moves_multiple_pieces(board, pieces)

def get_white_available_moves(state):
    available_moves = []
    for i in state.white_pieces_list:
        available_moves += get_available_moves(state.board, i[0], i[1])
    return available_moves
    # pieces = []
    # for i in range(8):
    #     for j in range(8):
    #         if board[i][j] in white_pieces:
    #             pieces.append((i, j))
    # return get_available_moves_multiple_pieces(board, pieces)