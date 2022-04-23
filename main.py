import pygame
from drawing.board import *
from draw import *
from config import *
from drawing.pieces import *
from AI import *
from evaluation import *
from analyze import *
import time

# pygame.init()

play_vs_computer = True

machine_learning = True

# piece_list = counting_pieces(board)


def run():

    # screen = new_chess_board()

    board = new_board()

    state = State()

    selected = False

    old_pos = (0, 0)

    player = 1

    END = 0

    black_moves = []

    white_moves = []

    sequence_moves = []

    while True:
        # event = pygame.event.get()
        # for ev in event:
            # if selected:
            #     screen = draw_highlighted_board(state, old_pos[0], old_pos[1])
            # else:
            #     screen = draw_board(state)
            END = check_end_game(state)
            if END == 1:
                # draw_text(screen, 'You Lost.')
                update_win(black_moves)
                update_lose(white_moves)
                if machine_learning:
                    time.sleep(2)
                    return
            elif END == -1:
                # draw_text(screen, 'You won!')
                update_win(white_moves)
                update_lose(black_moves)
                if machine_learning:
                    time.sleep(2)
                    return
            # pygame.display.update()
            # if ev.type == pygame.QUIT:
            #     pygame.quit()
            #     return
            if not END and machine_learning == True:
                if player == 1:
                    state = computer_move(state, white_moves, sequence_moves,
                                          0)
                    player = -1
                else:
                    state = computer_move(state, black_moves, sequence_moves,
                                          1)
                    player = 1
                continue
            elif not END and play_vs_computer == True:
                if player == -1:
                    state = computer_move(state, black_moves, sequence_moves,
                                          1)
                    player = 1
                    continue
            # elif ev.type == pygame.MOUSEBUTTONUP:
                # if END != 0:
                #     exit(0)
                # if selected:
                #     selected = False
                #     pos = pygame.mouse.get_pos()
                #     new_pos = (pos[0] // chess_pieces, pos[1] // chess_pieces)
                #     if is_valid(state, new_pos, old_pos):
                #         if state.board[old_pos[0]][old_pos[1]] == 'k':
                #             change_state_white_king(new_pos)
                #         elif state.board[old_pos[0]][old_pos[1]] == 'K':
                #             change_state_black_king(new_pos)
                #         make_moves(state, old_pos, new_pos)
                #         sequence_moves.append([old_pos, new_pos])
                #         id = Zobrist_code(state)
                #         white_moves.append(id)
                #         player = -player
                # else:
                #     pos = pygame.mouse.get_pos()
                #     old_pos = (pos[0] // chess_pieces, pos[1] // chess_pieces)
                #     if state.board[old_pos[0]][old_pos[1]] == ' ':
                #         continue
                #     if state.board[old_pos[0]][
                #             old_pos[1]] in black_pieces and player == 1:
                #         continue
                #     if state.board[old_pos[0]][
                #             old_pos[1]] in white_pieces and player == -1:
                #         continue
                #     selected = True


from keep_alive import keep_alive

keep_alive()

if machine_learning == True:
    while True:
        run()
else:
    run()
