import pygame
from drawing.board import *
from draw import *
from config import *
from drawing.pieces import *
from AI import *

pygame.init()

screen = new_chess_board()

board = new_board()

selected = False

old_pos = (0, 0)

player = 1

play_vs_computer = False

while True:
    event = pygame.event.get()
    for ev in event:
        # for i in board:
        #     print(i)
        if selected:
            screen = draw_highlighted_board(board, old_pos[0], old_pos[1])
        else:
            screen = draw_board(board)
        pygame.display.update()
        if play_vs_computer == True:
            if player == -1:
                board = computer_move(board)
                player = 1
                continue
        if ev.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif ev.type == pygame.MOUSEBUTTONUP:
            if selected:
                selected = False
                pos = pygame.mouse.get_pos()
                new_pos = (pos[0] // chess_pieces, pos[1] // chess_pieces)
                if is_valid(board, new_pos, old_pos):
                    if board[old_pos[0]][old_pos[1]] == 'k':
                        if old_pos == (4, 7) and new_pos == (6, 7):
                            board[5][7] = 'r'
                            board[6][7] = 'k'
                            board[7][7] = ' '
                        elif old_pos == (4, 7) and new_pos == (2, 7):
                            board[3][7] = 'r'
                            board[2][7] = 'k'
                            board[0][7] = ' '
                        change_state_white_king()
                    elif board[old_pos[0]][old_pos[1]] == 'K':
                        if old_pos == (4, 0) and new_pos == (6, 0):
                            board[5][0] = 'R'
                            board[6][0] = 'K'
                            board[7][0] = ' '
                        elif old_pos == (4, 0) and new_pos == (2, 0):
                            board[3][0] = 'R'
                            board[2][0] = 'K'
                            board[0][0] = ' '
                        change_state_black_king()
                    board[new_pos[0]][new_pos[1]] = board[old_pos[0]][old_pos[1]]
                    board[old_pos[0]][old_pos[1]] = ' '
                    player = -player
            else:
                pos = pygame.mouse.get_pos()
                old_pos = (pos[0] // chess_pieces, pos[1] // chess_pieces)
                if board[old_pos[0]][old_pos[1]] == ' ':
                    continue
                if board[old_pos[0]][old_pos[1]] in black_pieces and player == 1:
                    continue
                if board[old_pos[0]][old_pos[1]] in white_pieces and player == -1:
                    continue
                selected = True