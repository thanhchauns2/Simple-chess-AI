import pygame
from config import *

black_pieces = ['P', 'B', 'N', 'R', 'K', 'Q']

white_pieces = ['p', 'b', 'n', 'r', 'k', 'q']

class Pieces:
    
    def draw(self, screen, x, y):
        image = pygame.image.load(self.image_link)
        screen.blit(image, (x * chess_pieces, y * chess_pieces))
    
    def check_blank(self, x):
        return x == ' '
    
    def vertical(self, board, old_pos, new_pos):
        if old_pos[0] != new_pos[0]:
            return False
        for i in range(1, 8):
            if old_pos[1] + i == new_pos[1]:
                return True
            if old_pos[1] + i > 7 or old_pos[1] + i < 0 or not self.check_blank(board[old_pos[0]][old_pos[1] + i]):
                break

        for i in range(1, 8):
            if old_pos[1] - i == new_pos[1]:
                return True
            if old_pos[1] - i > 7 or old_pos[1] - i < 0 or not self.check_blank(board[old_pos[0]][old_pos[1] - i]):
                break
        return False
    
    def horizontal(self, board, old_pos, new_pos):
        if old_pos[1] != new_pos[1]:
            return False
        for i in range(1, 8):
            if old_pos[0] + i == new_pos[0]:
                return True
            if old_pos[0] + i > 7 or old_pos[0] + i < 0 or not self.check_blank(board[old_pos[0] + i][old_pos[1]]):
                break

        for i in range(1, 8):
            if old_pos[0] - i == new_pos[0]:
                return True
            if old_pos[0] - i > 7 or old_pos[0] - i < 0 or not self.check_blank(board[old_pos[0] - i][old_pos[1]]):
                break
    
    def diagonal(self, board, old_pos, new_pos):
        for i in range(1, 8):
            if old_pos[0] + i == new_pos[0] and old_pos[1] + i == new_pos[1]:
                return True
            if old_pos[0] + i > 7 or old_pos[0] + i < 0 or old_pos[1] + i > 7 or old_pos[1] + i < 0 or not self.check_blank(board[old_pos[0] + i][old_pos[1] + i]):
                break
        
        for i in range(1, 8):
            if old_pos[0] - i == new_pos[0] and old_pos[1] - i == new_pos[1]:
                return True
            if old_pos[0] - i > 7 or old_pos[0] - i < 0 or old_pos[1] - i > 7 or old_pos[1] - i < 0 or not self.check_blank(board[old_pos[0] - i][old_pos[1] - i]):
                break
        
        for i in range(1, 8):
            if old_pos[0] + i == new_pos[0] and old_pos[1] - i == new_pos[1]:
                return True
            if old_pos[0] + i > 7 or old_pos[0] + i < 0 or old_pos[1] - i > 7 or old_pos[1] - i < 0 or not self.check_blank(board[old_pos[0] + i][old_pos[1] - i]):
                break
        
        for i in range(1, 8):
            if old_pos[0] - i == new_pos[0] and old_pos[1] + i == new_pos[1]:
                return True
            if old_pos[0] - i > 7 or old_pos[0] - i < 0 or old_pos[1] + i > 7 or old_pos[1] + i < 0 or not self.check_blank(board[old_pos[0] - i][old_pos[1] + i]):
                break
        
        return False

class Pawn(Pieces):

    def taking_piece(self, board, old_pos, new_pos):
        if old_pos[1] != new_pos[1] + self.direction:
            return False
        if abs(old_pos[0] - new_pos[0]) != 1:
            return False
        if board[new_pos[0]][new_pos[1]] in self.anti_color:
            return True
        return False

    def first_move(self, board, old_pos, new_pos):
        if old_pos[1] == new_pos[1] + 2 * self.direction and old_pos[0] == new_pos[0]:
            if old_pos[1] != self.first_place:
                return False
            if board[new_pos[0]][new_pos[1] + self.direction] != ' ' or board[new_pos[0]][new_pos[1]] != ' ':
                return False
            return True
        return False

    def regular_move(self, board, old_pos, new_pos):
        if old_pos[1] != new_pos[1] + self.direction:
            return False
        if abs(old_pos[0] - new_pos[0]) != 0:
            return False
        if board[new_pos[0]][new_pos[1]] != ' ':
            return False
        return True

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in self.color:
            return False
        if self.taking_piece(board, old_pos, new_pos):
            return True
        if self.first_move(board, old_pos, new_pos):
            return True
        if self.regular_move(board, old_pos, new_pos):
            return True
        return False

class Rook(Pieces):

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in self.color:
            return False
        if old_pos[0] != new_pos[0] and old_pos[1] != new_pos[1]:
            return False
        if old_pos[0] == new_pos[0] and old_pos[1] == new_pos[1]:
            return False
        if self.vertical(board, old_pos, new_pos):
            return True
        if self.horizontal(board, old_pos, new_pos):
            return True
        return False

class Knight(Pieces):

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in self.color:
            return False
        if new_pos[0] == old_pos[0] or new_pos[1] == old_pos[1]:
            return False
        if abs(new_pos[0] - old_pos[0]) + abs(new_pos[1] - old_pos[1]) == 3:
            return True
        return False

class Bishop(Pieces):

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in white_pieces:
            return False
        if abs(old_pos[0] - new_pos[0]) != abs(old_pos[1] - new_pos[1]):
            return False
        if old_pos[0] == new_pos[0] or old_pos[1] == new_pos[1]:
            return False
        if self.diagonal(board, old_pos, new_pos):
            return True
        return False

class Queen(Pieces):

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in self.color:
            return False
        if old_pos[0] != new_pos[0] and old_pos[1] != new_pos[1]:
            return False
        if old_pos[0] == new_pos[0] and old_pos[1] == new_pos[1]:
            return False
        if self.vertical(board, old_pos, new_pos):
            return True
        if self.horizontal(board, old_pos, new_pos):
            return True
        if self.diagonal(board, old_pos, new_pos):
            return True
        return False

class white_pawn(Pawn):

    def __init__(self):
        self.image_link = '.\\images\\white_pawn.jpg'
        self.direction = 1
        self.first_place = 6
        self.anti_color = black_pieces
        self.color = white_pieces

class black_pawn(Pawn):

    def __init__(self):
        self.image_link = '.\\images\\black_pawn.png'
        self.direction = -1
        self.first_place = 1
        self.anti_color = white_pieces
        self.color = black_pieces

class white_rook(Rook):

    def __init__(self):

        self.image_link = '.\\images\\white_rook.png'
        self.color = white_pieces

class black_rook(Rook):

    def __init__(self):

        self.image_link = '.\\images\\black_rook.png'
        self.color = black_pieces

class white_knight(Knight):

    def __init__(self):

        self.image_link = '.\\images\\white_knight.png'
        self.color = white_pieces

class black_knight(Knight):

    def __init__(self):

        self.image_link = '.\\images\\black_knight.png'
        self.color = black_pieces

class white_bishop(Bishop):

    def __init__(self):

        self.image_link = '.\\images\\white_bishop.png'
        self.color = white_pieces

class black_bishop(Bishop):

    def __init__(self):

        self.image_link = '.\\images\\black_bishop.png'
        self.color = black_pieces

class white_queen(Queen):

    def __init__(self):

        self.image_link = '.\\images\\white_queen.png'
        self.color = white_pieces

class black_queen(Queen):

    def __init__(self):

        self.image_link = '.\\images\\black_queen.png'
        self.color = black_pieces

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

class King(Pieces):
    pass

class white_king(Pieces):

    def __init__(self):

        self.image_link = '.\\images\\white_king.png'
        self.moved = False
        self.x = 4
        self.y = 7

    def get_pos(self):
        return (self.x, self.y)

    def being_checked(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] not in black_pieces:
                    continue
                if board[i][j] == 'P':
                    if bp.is_valid(board, (i, j), self.get_pos()):
                        return True
                elif board[i][j] == 'B':
                    if bb.is_valid(board, (i, j), self.get_pos()):
                        return True
                elif board[i][j] == 'R':
                    if br.is_valid(board, (i, j), self.get_pos()):
                        return True
                elif board[i][j] == 'N':
                    if bn.is_valid(board, (i, j), self.get_pos()):
                        return True
                elif board[i][j] == 'Q':
                    if bq.is_valid(board, (i, j), self.get_pos()):
                        return True
        return False

    def castled_king_side(self, board):
        if self.moved:
            return False
        if board[5][7] == ' ' and board[6][7] == ' ' and board[7][7] == 'r':
            return True
        return False

    def castled_queen_side(self, board):
        if self.moved:
            return False
        if board[1][7] == ' ' and board[2][7] == ' ' and board[3][7] == ' ' and board[0][7] == 'r':
            return True
        return False

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in white_pieces or board[new_pos[0]][new_pos[1]] == 'K':
            return False
        if new_pos == (6, 7):
            return self.castled_king_side(board)
        if new_pos == (2, 7):
            return self.castled_queen_side(board)
        if abs(old_pos[0] - new_pos[0]) > 1 or abs(old_pos[1] - new_pos[1]) > 1:
            return False
        if old_pos[0] == new_pos[0] and old_pos[1] == new_pos[1]:
            return False
        # board[new_pos[0]][new_pos[1]], board[old_pos[0]][old_pos[1]] = board[old_pos[0]][old_pos[1]], board[new_pos[0]][new_pos[1]]
        # for i in range(8):
        #     for j in range(8):
        #         if board[i][j] in black_pieces:
        #             if board[i][j] == 'P':
        #                 if bp.is_valid(board, (i, j), new_pos):
        #                     board[new_pos[0]][new_pos[1]], board[old_pos[0]][old_pos[1]] = board[old_pos[0]][old_pos[1]], board[new_pos[0]][new_pos[1]]
        #                     return False
        #             elif board[i][j] == 'R':
        #                 if br.is_valid(board, (i, j), new_pos):
        #                     board[new_pos[0]][new_pos[1]], board[old_pos[0]][old_pos[1]] = board[old_pos[0]][old_pos[1]], board[new_pos[0]][new_pos[1]]
        #                     return False
        #             elif board[i][j] == 'N':
        #                 if bn.is_valid(board, (i, j), new_pos):
        #                     board[new_pos[0]][new_pos[1]], board[old_pos[0]][old_pos[1]] = board[old_pos[0]][old_pos[1]], board[new_pos[0]][new_pos[1]]
        #                     return False
        #             elif board[i][j] == 'B':
        #                 if bb.is_valid(board, (i, j), new_pos):
        #                     board[new_pos[0]][new_pos[1]], board[old_pos[0]][old_pos[1]] = board[old_pos[0]][old_pos[1]], board[new_pos[0]][new_pos[1]]
        #                     return False
        #             elif board[i][j] == 'Q':
        #                 if bq.is_valid(board, (i, j), new_pos):
        #                     board[new_pos[0]][new_pos[1]], board[old_pos[0]][old_pos[1]] = board[old_pos[0]][old_pos[1]], board[new_pos[0]][new_pos[1]]
        #                     return False
        #             elif board[i][j] == 'K':
        #                 if bk.is_valid(board, (i, j), new_pos):
        #                     board[new_pos[0]][new_pos[1]], board[old_pos[0]][old_pos[1]] = board[old_pos[0]][old_pos[1]], board[new_pos[0]][new_pos[1]]
        #                     return False
        # board[new_pos[0]][new_pos[1]], board[old_pos[0]][old_pos[1]] = board[old_pos[0]][old_pos[1]], board[new_pos[0]][new_pos[1]]
        return True

class black_king(Pieces):

    def __init__(self):

        self.image_link = '.\\images\\black_king.png'
        self.moved = False
        self.x = 4
        self.y = 0

    def get_pos(self):
        return (self.x, self.y)

    def being_checked(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] not in white_pieces:
                    continue
                if board[i][j] == 'p':
                    if wp.is_valid(board, (i, j), self.get_pos()):
                        return True
                elif board[i][j] == 'b':
                    if wb.is_valid(board, (i, j), self.get_pos()):
                        return True
                elif board[i][j] == 'r':
                    if wr.is_valid(board, (i, j), self.get_pos()):
                        return True
                elif board[i][j] == 'n':
                    if wn.is_valid(board, (i, j), self.get_pos()):
                        return True
                elif board[i][j] == 'q':
                    if wq.is_valid(board, (i, j), self.get_pos()):
                        return True
        return False

    def castled_king_side(self, board):
        if self.moved:
            return False
        if board[5][0] == ' ' and board[6][0] == ' ' and board[7][0] == 'R':
            return True
        return False

    def castled_queen_side(self, board):
        if self.moved:
            return False
        if board[1][0] == ' ' and board[2][0] == ' ' and board[3][0] == ' ' and board[0][0] == 'R':
            return True
        return False

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in black_pieces or board[new_pos[0]][new_pos[1]] == 'k':
            return False
        if new_pos == (6, 0):
            return self.castled_king_side(board)
        if new_pos == (2, 0):
            return self.castled_queen_side(board)
        if abs(old_pos[0] - new_pos[0]) > 1 or abs(old_pos[1] - new_pos[1]) > 1:
            return False
        if old_pos[0] == new_pos[0] and old_pos[1] == new_pos[1]:
            return False
        
        # board[new_pos[0]][new_pos[1]], board[old_pos[0]][old_pos[1]] = board[old_pos[0]][old_pos[1]], board[new_pos[0]][new_pos[1]]
        # for i in range(8):
        #     for j in range(8):
        #         if board[i][j] in white_pieces:
        #             if board[i][j] == 'p':
        #                 if wp.is_valid(board, (i, j), new_pos):
        #                     board[new_pos[0]][new_pos[1]], board[old_pos[0]][old_pos[1]] = board[old_pos[0]][old_pos[1]], board[new_pos[0]][new_pos[1]]
        #                     return False
        #             elif board[i][j] == 'r':
        #                 if wr.is_valid(board, (i, j), new_pos):
        #                     board[new_pos[0]][new_pos[1]], board[old_pos[0]][old_pos[1]] = board[old_pos[0]][old_pos[1]], board[new_pos[0]][new_pos[1]]
        #                     return False
        #             elif board[i][j] == 'n':
        #                 if wn.is_valid(board, (i, j), new_pos):
        #                     board[new_pos[0]][new_pos[1]], board[old_pos[0]][old_pos[1]] = board[old_pos[0]][old_pos[1]], board[new_pos[0]][new_pos[1]]
        #                     return False
        #             elif board[i][j] == 'b':
        #                 if wb.is_valid(board, (i, j), new_pos):
        #                     board[new_pos[0]][new_pos[1]], board[old_pos[0]][old_pos[1]] = board[old_pos[0]][old_pos[1]], board[new_pos[0]][new_pos[1]]
        #                     return False
        #             elif board[i][j] == 'q':
        #                 if wq.is_valid(board, (i, j), new_pos):
        #                     board[new_pos[0]][new_pos[1]], board[old_pos[0]][old_pos[1]] = board[old_pos[0]][old_pos[1]], board[new_pos[0]][new_pos[1]]
        #                     return False
        #             elif board[i][j] == 'k':
        #                 if wk.is_valid(board, (i, j), new_pos):
        #                     board[new_pos[0]][new_pos[1]], board[old_pos[0]][old_pos[1]] = board[old_pos[0]][old_pos[1]], board[new_pos[0]][new_pos[1]]
        #                     return False
        # board[new_pos[0]][new_pos[1]], board[old_pos[0]][old_pos[1]] = board[old_pos[0]][old_pos[1]], board[new_pos[0]][new_pos[1]]
        return True

wk = white_king()
bk = black_king()