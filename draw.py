import pygame
from config import *
from drawing.pieces import *

wp = white_pawn()
bp = black_pawn()
wr = white_rook()
br = black_rook()
wn = white_knight()
bn = black_knight()
wb = white_bishop()
bb = black_bishop()
wq = white_queen()
bq = black_queen()
wk = white_king()
bk = black_king()

def change_state_white_king():
    wk.moved = True

def change_state_black_king():
    bk.moved = True

def draw_board(board):
    screen = pygame.display.set_mode(screen_size)
    screen.fill(screen_color)
    block_size = screen_size[0] / 8
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                continue
            pygame.draw.rect(screen, black_block, (i * block_size, j * block_size, block_size, block_size))

    for i in range(8):
        for j in range(8):
            if board[i][j] == 'r':
                wr.draw(screen, i, j)
            elif board[i][j] == 'n':
                wn.draw(screen, i, j)
            elif board[i][j] == 'b':
                wb.draw(screen, i, j)
            elif board[i][j] == 'k':
                wk.draw(screen, i, j)
            elif board[i][j] == 'q':
                wq.draw(screen, i, j)
            elif board[i][j] == 'p':
                wp.draw(screen, i, j)
            elif board[i][j] == 'R':
                br.draw(screen, i, j)
            elif board[i][j] == 'N':
                bn.draw(screen, i, j)
            elif board[i][j] == 'B':
                bb.draw(screen, i, j)
            elif board[i][j] == 'K':
                bk.draw(screen, i, j)
            elif board[i][j] == 'Q':
                bq.draw(screen, i, j)
            elif board[i][j] == 'P':
                bp.draw(screen, i, j)
    return screen


def draw_highlighted_board(board, x, y):
    screen = pygame.display.set_mode(screen_size)
    screen.fill(screen_color)
    block_size = screen_size[0] / 8
    for i in range(8):
        for j in range(8):
            if i == x and j == y:
                if (i + j) % 2 == 0:
                    pygame.draw.rect(screen, highlighted_white_block, (i * block_size, j * block_size, block_size, block_size))
                else:
                    pygame.draw.rect(screen, highlighted_black_block, (i * block_size, j * block_size, block_size, block_size))
                continue
            if is_valid(board, (i, j), (x, y)):
                if (i + j) % 2 == 0:
                    pygame.draw.rect(screen, highlighted_white_block, (i * block_size, j * block_size, block_size, block_size))
                else:
                    pygame.draw.rect(screen, highlighted_black_block, (i * block_size, j * block_size, block_size, block_size))
                continue
            if (i + j) % 2 == 0:
                continue
            pygame.draw.rect(screen, black_block, (i * block_size, j * block_size, block_size, block_size))


    for i in range(8):
        for j in range(8):
            if board[i][j] == 'r':
                wr.draw(screen, i, j)
            elif board[i][j] == 'n':
                wn.draw(screen, i, j)
            elif board[i][j] == 'b':
                wb.draw(screen, i, j)
            elif board[i][j] == 'k':
                wk.draw(screen, i, j)
            elif board[i][j] == 'q':
                wq.draw(screen, i, j)
            elif board[i][j] == 'p':
                wp.draw(screen, i, j)
            elif board[i][j] == 'R':
                br.draw(screen, i, j)
            elif board[i][j] == 'N':
                bn.draw(screen, i, j)
            elif board[i][j] == 'B':
                bb.draw(screen, i, j)
            elif board[i][j] == 'K':
                bk.draw(screen, i, j)
            elif board[i][j] == 'Q':
                bq.draw(screen, i, j)
            elif board[i][j] == 'P':
                bp.draw(screen, i, j)
    return screen

def is_valid(board, new_pos, old_pos):
    if new_pos[0] < 0 or new_pos[0] > 7 or new_pos[1] < 0 or new_pos[1] > 7:
        return False
    piece = board[old_pos[0]][old_pos[1]]
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
