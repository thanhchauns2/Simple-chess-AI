import pygame
from drawing.board import *
from draw import *
from config import *
from drawing.pieces import *
from AI import *
from evaluation import *
from analyze import *

pygame.init()

screen = new_chess_board()

board = new_board()

selected = False

old_pos = (0, 0)

player = 1

play_vs_computer = True

END = 0

piece_list = counting_pieces(board)

while True:
    event = pygame.event.get()
    for ev in event:
        if selected:
            screen = draw_highlighted_board(board, old_pos[0], old_pos[1])
        else:
            screen = draw_board(board)
        END = check_end_game(piece_list)
        if END == 1:
            draw_text(screen, 'You Lost.')
        elif END == -1:
            draw_text(screen, 'You won!')
        pygame.display.update()
        if not END and play_vs_computer == True:
            if player == -1:
                board = computer_move(board, piece_list)
                player = 1
                continue
        if ev.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif ev.type == pygame.MOUSEBUTTONUP:
            if END != 0:
                exit(0)
            if selected:
                selected = False
                pos = pygame.mouse.get_pos()
                new_pos = (pos[0] // chess_pieces, pos[1] // chess_pieces)
                if is_valid(board, new_pos, old_pos):
                    if board[old_pos[0]][old_pos[1]] == 'k':
                        change_state_white_king(new_pos)
                    elif board[old_pos[0]][old_pos[1]] == 'K':
                        change_state_black_king(new_pos)
                    make_moves(piece_list, board, old_pos, new_pos)
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