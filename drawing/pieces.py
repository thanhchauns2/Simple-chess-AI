import pygame
from config import *

black_pieces = ['P', 'B', 'N', 'R', 'K', 'Q']

white_pieces = ['p', 'b', 'n', 'r', 'k', 'q']

class white_pawn:

    def __init__(self):

        self.image_link = '.\\images\\white_pawn.jpg'

    def draw(self, screen, x, y):
        image = pygame.image.load(self.image_link)
        screen.blit(image, (x * chess_pieces, y * chess_pieces))

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in white_pieces:
            return False
        if old_pos[1] == new_pos[1] + 2 and old_pos[0] == new_pos[0]:
            if old_pos[1] != 6:
                return False
            if board[new_pos[0]][new_pos[1] + 1] != ' ':
                return False
            return True
        if old_pos[1] != new_pos[1] + 1:
            return False
        if old_pos[0] != new_pos[0]:
            if abs(old_pos[0] - new_pos[0]) != 1:
                return False
            if board[new_pos[0]][new_pos[1]] in black_pieces:
                return True
            return False
        else:
            if board[new_pos[0]][new_pos[1]] in black_pieces:
                return False
            return True

class black_pawn:

    def __init__(self):

        self.image_link = '.\\images\\black_pawn.png'

    def draw(self, screen, x, y):
        image = pygame.image.load(self.image_link)
        screen.blit(image, (x * chess_pieces, y * chess_pieces))

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in black_pieces:
            return False
        if old_pos[1] == new_pos[1] - 2 and old_pos[0] == new_pos[0]:
            if old_pos[1] != 1:
                return False
            if board[new_pos[0]][new_pos[1] - 1] != ' ':
                return False
            return True
        if old_pos[1] != new_pos[1] - 1:
            return False
        if old_pos[0] != new_pos[0]:
            if abs(old_pos[0] - new_pos[0]) != 1:
                return False
            if board[new_pos[0]][new_pos[1]] in white_pieces:
                return True
            return False
        else:
            if board[new_pos[0]][new_pos[1]] in white_pieces:
                return False
            return True


class white_rook:

    def __init__(self):

        self.image_link = '.\\images\\white_rook.png'

    def draw(self, screen, x, y):
        image = pygame.image.load(self.image_link)
        screen.blit(image, (x * chess_pieces, y * chess_pieces))

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in white_pieces:
            return False
        if old_pos[0] != new_pos[0] and old_pos[1] != new_pos[1]:
            return False
        if old_pos[0] == new_pos[0] and old_pos[1] == new_pos[1]:
            return False
        if old_pos[0] == new_pos[0]:
            if old_pos[1] > new_pos[1]:
                for i in range(old_pos[1] - 1, new_pos[1], -1):
                    if board[old_pos[0]][i] != ' ':
                        return False
                return True
            else:
                for i in range(old_pos[1] + 1, new_pos[1]):
                    if board[old_pos[0]][i] != ' ':
                        return False
                return True
        else:
            if old_pos[0] > new_pos[0]:
                for i in range(old_pos[0] - 1, new_pos[0], -1):
                    if board[i][old_pos[1]] != ' ':
                        return False
                return True
            else:
                for i in range(old_pos[0] + 1, new_pos[0]):
                    if board[i][old_pos[1]] != ' ':
                        return False
                return True

class black_rook:

    def __init__(self):

        self.image_link = '.\\images\\black_rook.png'

    def draw(self, screen, x, y):
        image = pygame.image.load(self.image_link)
        screen.blit(image, (x * chess_pieces, y * chess_pieces))

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in black_pieces:
            return False
        if old_pos[0] != new_pos[0] and old_pos[1] != new_pos[1]:
            return False
        if old_pos[0] == new_pos[0] and old_pos[1] == new_pos[1]:
            return False
        if old_pos[0] == new_pos[0]:
            if old_pos[1] > new_pos[1]:
                for i in range(old_pos[1] - 1, new_pos[1], -1):
                    if board[old_pos[0]][i] != ' ':
                        return False
                return True
            else:
                for i in range(old_pos[1] + 1, new_pos[1]):
                    if board[old_pos[0]][i] != ' ':
                        return False
                return True
        else:
            if old_pos[0] > new_pos[0]:
                for i in range(old_pos[0] - 1, new_pos[0], -1):
                    if board[i][old_pos[1]] != ' ':
                        return False
                return True
            else:
                for i in range(old_pos[0] + 1, new_pos[0]):
                    if board[i][old_pos[1]] != ' ':
                        return False
                return True

class white_knight:

    def __init__(self):

        self.image_link = '.\\images\\white_knight.png'

    def draw(self, screen, x, y):
        image = pygame.image.load(self.image_link)
        screen.blit(image, (x * chess_pieces, y * chess_pieces))

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in white_pieces:
            return False
        if new_pos[0] == old_pos[0] or new_pos[1] == old_pos[1]:
            return False
        if abs(new_pos[0] - old_pos[0]) + abs(new_pos[1] - old_pos[1]) == 3:
            return True
        return False

class black_knight:

    def __init__(self):

        self.image_link = '.\\images\\black_knight.png'

    def draw(self, screen, x, y):
        image = pygame.image.load(self.image_link)
        screen.blit(image, (x * chess_pieces, y * chess_pieces))

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in black_pieces:
            return False
        if new_pos[0] == old_pos[0] or new_pos[1] == old_pos[1]:
            return False
        if abs(new_pos[0] - old_pos[0]) + abs(new_pos[1] - old_pos[1]) == 3:
            return True
        return False

class white_bishop:

    def __init__(self):

        self.image_link = '.\\images\\white_bishop.png'

    def draw(self, screen, x, y):
        image = pygame.image.load(self.image_link)
        screen.blit(image, (x * chess_pieces, y * chess_pieces))

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in white_pieces:
            return False
        if abs(old_pos[0] - new_pos[0]) != abs(old_pos[1] - new_pos[1]):
            return False
        if old_pos[0] == new_pos[0] and old_pos[1] == new_pos[1]:
            return False
        dist = abs(old_pos[0] - new_pos[0])
        if old_pos[0] > new_pos[0]:
            if old_pos[1] > new_pos[1]:
                for i in range(1, dist):
                    if board[old_pos[0] - i][old_pos[1] - i] != ' ':
                        return False
                return True
            else:
                for i in range(1, dist):
                    if board[old_pos[0] - i][old_pos[1] + i] != ' ':
                        return False
                return True
        else:
            if old_pos[1] > new_pos[1]:
                for i in range(1, dist):
                    if board[old_pos[0] + i][old_pos[1] - i] != ' ':
                        return False
                return True
            else:
                for i in range(1, dist):
                    if board[old_pos[0] + i][old_pos[1] + i] != ' ':
                        return False
                return True
            

class black_bishop:

    def __init__(self):

        self.image_link = '.\\images\\black_bishop.png'

    def draw(self, screen, x, y):
        image = pygame.image.load(self.image_link)
        screen.blit(image, (x * chess_pieces, y * chess_pieces))

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in black_pieces:
            return False
        if abs(old_pos[0] - new_pos[0]) != abs(old_pos[1] - new_pos[1]):
            return False
        if old_pos[0] == new_pos[0] and old_pos[1] == new_pos[1]:
            return False
        dist = abs(old_pos[0] - new_pos[0])
        if old_pos[0] > new_pos[0]:
            if old_pos[1] > new_pos[1]:
                for i in range(1, dist):
                    if board[old_pos[0] - i][old_pos[1] - i] != ' ':
                        return False
                return True
            else:
                for i in range(1, dist):
                    if board[old_pos[0] - i][old_pos[1] + i] != ' ':
                        return False
                return True
        else:
            if old_pos[1] > new_pos[1]:
                for i in range(1, dist):
                    if board[old_pos[0] + i][old_pos[1] - i] != ' ':
                        return False
                return True
            else:
                for i in range(1, dist):
                    if board[old_pos[0] + i][old_pos[1] + i] != ' ':
                        return False
                return True

class white_king:

    def __init__(self):

        self.image_link = '.\\images\\white_king.png'

        self.moved = False

    def draw(self, screen, x, y):
        image = pygame.image.load(self.image_link)
        screen.blit(image, (x * chess_pieces, y * chess_pieces))

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
        if board[new_pos[0]][new_pos[1]] in white_pieces:
            return False
        if new_pos == (6, 7):
            return self.castled_king_side(board)
        if new_pos == (2, 7):
            return self.castled_queen_side(board)
        if abs(old_pos[0] - new_pos[0]) > 1 or abs(old_pos[1] - new_pos[1]) > 1:
            return False
        if old_pos[0] == new_pos[0] and old_pos[1] == new_pos[1]:
            return False
        return True

class black_king:

    def __init__(self):

        self.image_link = '.\\images\\black_king.png'

        self.moved = False

    def draw(self, screen, x, y):
        image = pygame.image.load(self.image_link)
        screen.blit(image, (x * chess_pieces, y * chess_pieces))

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
        if board[new_pos[0]][new_pos[1]] in black_pieces:
            return False
        if new_pos == (6, 0):
            return self.castled_king_side(board)
        if new_pos == (2, 0):
            return self.castled_queen_side(board)
        if abs(old_pos[0] - new_pos[0]) > 1 or abs(old_pos[1] - new_pos[1]) > 1:
            return False
        if old_pos[0] == new_pos[0] and old_pos[1] == new_pos[1]:
            return False
        return True

class white_queen:

    def __init__(self):

        self.image_link = '.\\images\\white_queen.png'

    def draw(self, screen, x, y):
        image = pygame.image.load(self.image_link)
        screen.blit(image, (x * chess_pieces, y * chess_pieces))

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in white_pieces:
            return False
        if old_pos[0] == new_pos[0] and old_pos[1] == new_pos[1]:
            return False
        if old_pos[0] == new_pos[0]:
            if old_pos[1] > new_pos[1]:
                for i in range(old_pos[1] - 1, new_pos[1], -1):
                    if board[old_pos[0]][i] != ' ':
                        return False
                return True
            else:
                for i in range(old_pos[1] + 1, new_pos[1]):
                    if board[old_pos[0]][i] != ' ':
                        return False
                return True
        elif old_pos[1] == new_pos[1]:
            if old_pos[0] > new_pos[0]:
                for i in range(old_pos[0] - 1, new_pos[0], -1):
                    if board[i][old_pos[1]] != ' ':
                        return False
                return True
            else:
                for i in range(old_pos[0] + 1, new_pos[0]):
                    if board[i][old_pos[1]] != ' ':
                        return False
                return True
        if abs(old_pos[0] - new_pos[0]) != abs(old_pos[1] - new_pos[1]):
            return False
        dist = abs(old_pos[0] - new_pos[0])
        if old_pos[0] > new_pos[0]:
            if old_pos[1] > new_pos[1]:
                for i in range(1, dist):
                    if board[old_pos[0] - i][old_pos[1] - i] != ' ':
                        return False
                return True
            else:
                for i in range(1, dist):
                    if board[old_pos[0] - i][old_pos[1] + i] != ' ':
                        return False
                return True
        else:
            if old_pos[1] > new_pos[1]:
                for i in range(1, dist):
                    if board[old_pos[0] + i][old_pos[1] - i] != ' ':
                        return False
                return True
            else:
                for i in range(1, dist):
                    if board[old_pos[0] + i][old_pos[1] + i] != ' ':
                        return False
                return True

class black_queen:

    def __init__(self):

        self.image_link = '.\\images\\black_queen.png'

    def draw(self, screen, x, y):
        image = pygame.image.load(self.image_link)
        screen.blit(image, (x * chess_pieces, y * chess_pieces))

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in black_pieces:
            return False
        if old_pos[0] == new_pos[0] and old_pos[1] == new_pos[1]:
            return False
        if old_pos[0] == new_pos[0]:
            if old_pos[1] > new_pos[1]:
                for i in range(old_pos[1] - 1, new_pos[1], -1):
                    if board[old_pos[0]][i] != ' ':
                        return False
                return True
            else:
                for i in range(old_pos[1] + 1, new_pos[1]):
                    if board[old_pos[0]][i] != ' ':
                        return False
                return True
        elif old_pos[1] == new_pos[1]:
            if old_pos[0] > new_pos[0]:
                for i in range(old_pos[0] - 1, new_pos[0], -1):
                    if board[i][old_pos[1]] != ' ':
                        return False
                return True
            else:
                for i in range(old_pos[0] + 1, new_pos[0]):
                    if board[i][old_pos[1]] != ' ':
                        return False
                return True
        if abs(old_pos[0] - new_pos[0]) != abs(old_pos[1] - new_pos[1]):
            return False
        dist = abs(old_pos[0] - new_pos[0])
        if old_pos[0] > new_pos[0]:
            if old_pos[1] > new_pos[1]:
                for i in range(1, dist):
                    if board[old_pos[0] - i][old_pos[1] - i] != ' ':
                        return False
                return True
            else:
                for i in range(1, dist):
                    if board[old_pos[0] - i][old_pos[1] + i] != ' ':
                        return False
                return True
        else:
            if old_pos[1] > new_pos[1]:
                for i in range(1, dist):
                    if board[old_pos[0] + i][old_pos[1] - i] != ' ':
                        return False
                return True
            else:
                for i in range(1, dist):
                    if board[old_pos[0] + i][old_pos[1] + i] != ' ':
                        return False
                return True