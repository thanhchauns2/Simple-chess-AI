white_pawn_board = [[100, 50, 10, 5, 0, 5, 5, 0],
                    [100, 50, 10, 5, 0, -5, 10, 0],
                    [100, 50, 20, 10, 0, -10, 10, 0],
                    [100, 50, 30, 25, 20, 0, -20, 0],
                    [100, 50, 30, 25, 20, 0, -20, 0],
                    [100, 50, 20, 10, 0, -10, 10, 0],
                    [100, 50, 10, 5, 0, -5, 10, 0],
                    [100, 50, 10, 5, 0, 5, 5, 0]]

white_knight_board = [[-50, -40, -30, -30, -30, -30, -40, -50],
                      [-40, -20, 5, 0, 5, 0, -20, -40],
                      [-30, 0, 10, 15, 15, 10, 0, -30],
                      [-30, 5, 15, 20, 20, 15, 0, -30],
                      [-30, 5, 15, 20, 20, 15, 0, -30],
                      [-30, 0, 10, 15, 15, 10, 0, -30],
                      [-40, -20, 5, 0, 5, 0, -20, -40],
                      [-50, -40, -30, -30, -30, -30, -40, -50]]

white_bishop_board = [[-20, -10, -10, -10, -10, -10, -10, -20],
                      [-10, 0, 0, 5, 0, 10, 5, -10],
                      [-10, 0, 5, 5, 10, 10, 0, -10],
                      [-10, 0, 10, 10, 10, 10, 0, -10],
                      [-10, 0, 10, 10, 10, 10, 0, -10],
                      [-10, 0, 5, 5, 10, 10, 0, -10],
                      [-10, 0, 0, 5, 0, 10, 5, -10],
                      [-20, -10, -10, -10, -10, -10, -10, -20]]

white_rook_board = [[0, 5, -5, -5, -5, -5, -5, 0],
                    [0, 10, 0, 0, 0, 0, 0, 0],
                    [0, 10, 0, 0, 0, 0, 0, 0],
                    [0, 10, 0, 0, 0, 0, 0, 5],
                    [0, 10, 0, 0, 0, 0, 0, 5],
                    [0, 10, 0, 0, 0, 0, 0, 0],
                    [0, 10, 0, 0, 0, 0, 0, 0],
                    [0, 5, -5, -5, -5, -5, -5, 0]]

white_queen_board = [[-20, -10, -10, -5, 0, -10, -10, -20],
                     [-10, 0, 0, 0, 0, 5, 0, -10],
                     [-10, 0, 5, 5, 5, 5, 5, -10],
                     [-5, 0, 5, 5, 5, 5, 0, -5],
                     [-5, 0, 5, 5, 5, 5, 0, -5],
                     [-10, 0, 5, 5, 5, 5, 0, -10],
                     [-10, 0, 0, 0, 0, 0, 0, -10],
                     [-20, -10, -10, -5, -5, -10, -10, -20]]

white_king_early_board = [[-30, -30, -30, -30, -20, -10, 20, 20],
                          [-40, -40, -40, -40, -30, -20, 20, 30],
                          [-40, -40, -40, -40, -30, -20, 0, 10],
                          [-50, -50, -50, -50, -40, -20, 0, 0],
                          [-50, -50, -50, -50, -40, -20, 0, 0],
                          [-40, -40, -40, -40, -30, -20, 0, 10],
                          [-40, -40, -40, -40, -30, -20, 20, 30],
                          [-30, -30, -30, -30, -20, -10, 20, 20]]

white_king_late_board = [[-50, -30, -30, -30, -30, -30, -30, -50],
                         [-40, -20, -10, -10, -10, -10, -30, -30],
                         [-30, -10, 20, 30, 30, 20, 0, -30],
                         [-20, 0, 30, 40, 40, 30, 0, -30],
                         [-20, 0, 30, 40, 40, 30, 0, -30],
                         [-30, -10, 20, 30, 30, 20, 0, -30],
                         [-40, -20, -10, -10, -10, -10, -30, -30],
                         [-50, -30, -30, -30, -30, -30, -30, -50]]

black_pawn_board = [[0, 5, 5, 0, 5, 10, 50, 100],
                    [0, 10, -5, 0, 5, 10, 50, 100],
                    [0, 10, -10, 0, 10, 20, 50, 100],
                    [0, -20, 0, 20, 25, 30, 50, 100],
                    [0, -20, 0, 20, 25, 30, 50, 100],
                    [0, 10, -10, 0, 10, 20, 50, 100],
                    [0, 10, -5, 0, 5, 10, 50, 100],
                    [0, 5, 5, 0, 5, 10, 50, 100]]

black_knight_board = [[-50, -40, -30, -30, -30, -30, -40, -50],
                      [-40, -20, 0, 5, 0, 5, -20, -40],
                      [-30, 0, 10, 15, 15, 10, 0, -30],
                      [-30, 0, 15, 20, 20, 15, 5, -30],
                      [-30, 0, 15, 20, 20, 15, 5, -30],
                      [-30, 0, 10, 15, 15, 10, 0, -30],
                      [-40, -20, 0, 5, 0, 5, -20, -40],
                      [-50, -40, -30, -30, -30, -30, -40, -50]]

black_bishop_board = [[-20, -10, -10, -10, -10, -10, -10, -20],
                      [-10, 5, 10, 0, 5, 0, 0, -10],
                      [-10, 0, 10, 10, 5, 5, 0, -10],
                      [-10, 0, 10, 10, 10, 10, 0, -10],
                      [-10, 0, 10, 10, 10, 10, 0, -10],
                      [-10, 0, 10, 10, 5, 5, 0, -10],
                      [-10, 5, 10, 0, 5, 0, 0, -10],
                      [-20, -10, -10, -10, -10, -10, -10, -20]]

black_rook_board = [[0, -5, -5, -5, -5, -5, 5, 0],
                    [0, 0, 0, 0, 0, 0, 10, 0],
                    [0, 0, 0, 0, 0, 0, 10, 0],
                    [5, 0, 0, 0, 0, 0, 10, 0],
                    [5, 0, 0, 0, 0, 0, 10, 0],
                    [0, 0, 0, 0, 0, 0, 10, 0],
                    [0, 0, 0, 0, 0, 0, 10, 0],
                    [0, -5, -5, -5, -5, -5, 5, 0]]

black_queen_board = [[-20, -10, -10, 0, -5, -10, -10, -20],
                     [-10, 0, 5, 0, 0, 0, 0, -10],
                     [-10, 5, 5, 5, 5, 5, 0, -10],
                     [-5, 0, 5, 5, 5, 5, 0, -5],
                     [-5, 0, 5, 5, 5, 5, 0, -5],
                     [-10, 0, 5, 5, 5, 5, 0, -10],
                     [-10, 0, 0, 0, 0, 0, 0, -10],
                     [-20, -10, -10, -5, -5, -10, -10, -20]]

black_king_early_board = [[20, 20, -10, -20, -30, -30, -30, -30],
                          [30, 20, -20, -30, -40, -40, -40, -40],
                          [10, 0, -20, -30, -40, -40, -40, -40],
                          [0, 0, -20, -40, -50, -50, -50, -50],
                          [0, 0, -20, -40, -50, -50, -50, -50],
                          [10, 0, -20, -30, -40, -40, -40, -40],
                          [30, 20, -20, -30, -40, -40, -40, -40],
                          [20, 20, -10, -20, -30, -30, -30, -30]]

black_king_late_board = [[-50, -30, -30, -30, -30, -30, -30, -50],
                         [-30, -30, -10, -10, -10, -10, -20, -40],
                         [-30, 0, 20, 30, 30, 20, -10, -30],
                         [-30, 0, 30, 40, 40, 30, 0, -20],
                         [-30, 0, 30, 40, 40, 30, 0, -20],
                         [-30, 0, 20, 30, 30, 20, -10, -30],
                         [-30, -30, -10, -10, -10, -10, -20, -40],
                         [-50, -30, -30, -30, -30, -30, -30, -50]]