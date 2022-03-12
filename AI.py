from analyze import *
from drawing.board import *
import copy

def computer_move(board, piece_list):

    available_moves = get_black_available_moves(board)
    temp_moves = []
    current_point = analyze_current_state(board)
    before = counting_pieces(board)

    for x in available_moves:
        point = analyze_next_state(current_point, x[0], x[1], board[x[0][0]][x[0][1]], board[x[1][0]][x[1][1]], before)
        # print(current_point, point)
        if len(temp_moves) >= best_moves_limit and temp_moves[best_moves_limit - 1][2] <= point:
            continue
        captured_piece = board[x[1][0]][x[1][1]]
        promoted = make_moves(piece_list, board, x[0], x[1])
        x = [x[0], x[1], point]
        temp_moves.append(x)
        if len(temp_moves) > best_moves_limit:
            # print(temp_moves)
            temp_moves.sort(key = lambda x : x[2])
            temp_moves = temp_moves[:best_moves_limit]
            # print(temp_moves)
        undo_moves(piece_list, board, x[0], x[1], captured_piece, promoted)

    available_moves = copy.deepcopy(temp_moves)

    for x in available_moves:
        x[2] = deep_analyze(piece_list, board, x[0], x[1])[2]
        temp_moves.append(x)
    
    available_moves = temp_moves
    available_moves.sort(key = lambda x : x[2])
    # print(temp_moves)
    # print(available_moves)

    make_moves(piece_list, board, available_moves[0][0], available_moves[0][1])

    return board

def deep_analyze(piece_list, board, old_pos, new_pos, tag = 'white', depth = 0, max_depth = analyze_depth):

    current_captured_piece = board[new_pos[0]][new_pos[1]]
    current_promotion = make_moves(piece_list, board, old_pos, new_pos)
    current_point = analyze_current_state(board)

    if piece_list['k'] == 0:
        undo_moves(piece_list, board, old_pos, new_pos, current_captured_piece, current_promotion)
        return [old_pos, new_pos, (int)(-1e10)]
    if piece_list['K'] == 0:
        undo_moves(piece_list, board, old_pos, new_pos, current_captured_piece, current_promotion)
        return [old_pos, new_pos, (int)(1e10)]

    if tag == 'black':
        available_moves = get_black_available_moves(board)
        temp_moves = []

        before = counting_pieces(board)

        # for i in board:
        #     print(i)

        if len(available_moves) == 0:
            undo_moves(piece_list, board, old_pos, new_pos, current_captured_piece, current_promotion)
            return [old_pos, new_pos, (int)(1e10)]

        # print(available_moves)

        for x in available_moves:
            point = analyze_next_state(current_point, x[0], x[1], board[x[0][0]][x[0][1]], board[x[1][0]][x[1][1]], before)
            # print(current_point, point)
            if len(temp_moves) >= best_moves_limit and temp_moves[best_moves_limit - 1][2] <= point:
                continue
            captured_piece = board[x[1][0]][x[1][1]]
            promoted = make_moves(piece_list, board, x[0], x[1])
            x = [x[0], x[1], point]
            temp_moves.append(x)
            if len(temp_moves) > best_moves_limit:
                temp_moves.sort(key = lambda x : x[2])
                # print(temp_moves)
                temp_moves = temp_moves[:best_moves_limit]
            undo_moves(piece_list, board, x[0], x[1], captured_piece, promoted)

        # print(temp_moves)

        available_moves = temp_moves

        # print(available_moves)

        if depth == max_depth:
            undo_moves(piece_list, board, old_pos, new_pos, current_captured_piece, current_promotion)
            return available_moves[0]
        else:
            temp_moves = []
            for x in available_moves:
                x[2] = deep_analyze(piece_list, board, x[0], x[1], 'white', depth + 1, max_depth)[2]
                temp_moves.append(x)
            available_moves = temp_moves
            available_moves.sort(key = lambda x : x[2])
            undo_moves(piece_list, board, old_pos, new_pos, current_captured_piece, current_promotion)
            return available_moves[0]
    else:
        available_moves = get_white_available_moves(board)
        temp_moves = []
        before = counting_pieces(board)

        if len(available_moves) == 0:
            undo_moves(piece_list, board, old_pos, new_pos, current_captured_piece, current_promotion)
            return [old_pos, new_pos, (int)(-1e10)]

        for x in available_moves:
            point = analyze_next_state(current_point, x[0], x[1], board[x[0][0]][x[0][1]], board[x[1][0]][x[1][1]], before)
            if len(temp_moves) >= best_moves_limit and temp_moves[0][2] >= point:
                continue
            captured_piece = board[x[1][0]][x[1][1]]
            promoted = make_moves(piece_list, board, x[0], x[1])
            x = [x[0], x[1], point]
            temp_moves.append(x)
            if len(temp_moves) > best_moves_limit:
                temp_moves.sort(key = lambda x : x[2])
                temp_moves = temp_moves[-best_moves_limit:]
            undo_moves(piece_list, board, x[0], x[1], captured_piece, promoted)

        available_moves = temp_moves

        if depth == max_depth:
            undo_moves(piece_list, board, old_pos, new_pos, current_captured_piece, current_promotion)
            return available_moves[-1]
        else:
            temp_moves = []
            for x in available_moves:
                x[2] = deep_analyze(piece_list, board, x[0], x[1], 'black', depth + 1, max_depth)[2]
                temp_moves.append(x)
            available_moves = temp_moves
            available_moves.sort(key = lambda x : x[2])
            undo_moves(piece_list, board, old_pos, new_pos, current_captured_piece, current_promotion)
            return available_moves[-1]