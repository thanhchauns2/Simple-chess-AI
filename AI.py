from analyze import *
from drawing.board import *
import copy

def computer_move(board):

    available_moves = get_black_available_moves(board)
    temp_moves = []
    current_point = analyze_current_state(board)
    before = 'late'
    if check_late(board):
        before = 'late'
    else:
        before = 'early'

    for x in available_moves:
        temp_board = copy.deepcopy(board)
        make_moves(temp_board, x[0], x[1])
        after = check_late(board)
        point = analyze_next_state(current_point, x[0], x[1], board[x[0][0]][x[0][1]], board[x[1][0]][x[1][1]], before, after)
        x = [x[0], x[1], point]
        temp_moves.append(x)

    available_moves = temp_moves
    available_moves.sort(key = lambda x : x[2])
    available_moves = available_moves[best_moves_limit:]
    temp_moves.clear()

    for x in available_moves:
        x[2] = deep_analyze(board, x[0], x[1])[2]
        temp_moves.append(x)
    
    available_moves = temp_moves
    available_moves.sort(key = lambda x : x[2])

    make_moves(board, available_moves[0][0], available_moves[0][1])

    return board

def deep_analyze(board, old_pos, new_pos, tag = 'black', dept = 0, max_dept = analyze_dept):

    temp_board = copy.deepcopy(board)
    make_moves(temp_board, old_pos, new_pos)
    current_point = analyze_current_state(board)

    if white_king_dead(board):
        return [old_pos, new_pos, (int)(-1e10)]
    if black_king_dead(board):
        return [old_pos, new_pos, (int)(1e10)]

    if tag == 'black':
        available_moves = get_black_available_moves(temp_board)
        temp_moves = []

        before = 'late'
        if check_late(board):
            before = 'late'
        else:
            before = 'early'

        for i in board:
            print(i)

        if len(available_moves) == 0:
            return [old_pos, new_pos, (int)(1e10)]

        print(available_moves)

        for x in available_moves:
            temp_board_2 = copy.deepcopy(temp_board)
            after = check_late(board)
            point = analyze_next_state(current_point, x[0], x[1], temp_board[x[0][0]][x[0][1]], temp_board[x[1][0]][x[1][1]], before, after)
            print(current_point, point)
            if len(temp_moves) >= best_moves_limit and temp_moves[0][2] >= point:
                continue
            make_moves(temp_board_2, x[0], x[1])
            x = [x[0], x[1], point]
            temp_moves.append(x)
            if len(temp_moves) > best_moves_limit:
                temp_moves.sort(key = lambda x : x[2])
                temp_moves = temp_moves[best_moves_limit:]

        print(temp_moves)

        available_moves = temp_moves

        print(available_moves)

        if dept == max_dept:
            return available_moves[0]
        else:
            temp_moves = []
            for x in available_moves:
                x[2] = deep_analyze(temp_board_2, x[0], x[1], 'white', dept + 1, max_dept)[2]
                temp_moves.append(x)
            available_moves = temp_moves
            available_moves.sort(key = lambda x : x[2])
            return available_moves[0]
    else:
        available_moves = get_white_available_moves(temp_board)
        temp_moves = []
        before = 'late'
        if check_late(board):
            before = 'late'
        else:
            before = 'early'

        if len(available_moves) == 0:
            return [old_pos, new_pos, (int)(-1e10)]

        for x in available_moves:
            temp_board_2 = copy.deepcopy(temp_board)
            after = check_late(board)
            point = analyze_next_state(current_point, x[0], x[1], temp_board[x[0][0]][x[0][1]], temp_board[x[1][0]][x[1][1]], before, after)
            if len(temp_moves) >= best_moves_limit and temp_moves[0][2] >= point:
                continue
            make_moves(temp_board_2, x[0], x[1])
            x = [x[0], x[1], point]
            temp_moves.append(x)
            if len(temp_moves) > best_moves_limit:
                temp_moves.sort(key = lambda x : x[2])
                temp_moves = temp_moves[-best_moves_limit:]

        available_moves = temp_moves

        if dept == max_dept:
            return available_moves[-1]
        else:
            temp_moves = []
            for x in available_moves:
                x[2] = deep_analyze(temp_board_2, x[0], x[1], 'black', dept + 1, max_dept)[2]
                temp_moves.append(x)
            available_moves = temp_moves
            available_moves.sort(key = lambda x : x[2])
            return available_moves[-1]