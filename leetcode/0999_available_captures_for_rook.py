"""
On an 8 x 8 chessboard, there is one white rook. There also may 
be empty squares, white bishops, and black pawns. These are 
given as characters 'R', '.', 'B', and 'p' respectively. 
Uppercase characters represent white pieces, and lowercase 
characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four 
cardinal directions (north, east, west, and south), then moves 
in that direction until it chooses to stop, reaches the edge of 
the board, or captures an opposite colored pawn by moving to 
the same square it occupies.  Also, rooks cannot move into 
the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

Example 1:

    Input: [[".",".",".",".",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            [".",".",".","R",".",".",".","p"],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."]]
    Output: 3
    Explanation: In this example the rook is able to capture
    all the pawns.

Example 2:

    Input: [[".",".",".",".",".",".",".","."],
            [".","p","p","p","p","p",".","."],
            [".","p","p","B","p","p",".","."],
            [".","p","B","R","B","p",".","."],
            [".","p","p","B","p","p",".","."],
            [".","p","p","p","p","p",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."]]
    Output: 0
    Explanation: Bishops are blocking the rook to capture any 
    pawn.

Example 3:

    Input: [[".",".",".",".",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            ["p","p",".","R",".","p","B","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".","B",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            [".",".",".",".",".",".",".","."]]
    Output: 3
    Explanation: The rook can capture the pawns at positions 
    b5, d6 and f5.

Note:
    board.length == board[i].length == 8
    board[i][j] is either 'R', '.', 'B', or 'p'
    There is exactly one cell with board[i][j] == 'R'
"""


class Solution:
    def numRookCaptures(self, board):
        """change 2-dim into 1-dim, then use mod 8 table"""
        board = sum(board, [])
        
        r_index = board.index('R')
        r_row = r_index // 8
        r_col = r_index % 8
        
        # left, right, up, down
        dir_size = [-1, 1, -8, 8]
        step_range = [r_col, 7 - r_col, r_row, 7 - r_row]

        n_pawn = 0
        for d in range(4):
            ds = dir_size[d]
            for one_step in range(step_range[d]):
                if board[r_index + ds * (one_step + 1)] == 'p':
                    n_pawn += 1
                    break
                elif board[r_index + ds * (one_step + 1)] == 'B':
                    break

        return n_pawn

    def numRookCaptures2(self, board):
        """string method"""
        board = sum(board, [])

        r_index = board.index('R')
        n_col = r_index % 8
        r_row = board[r_index - n_col:r_index - n_col + 8]
        r_col = board[n_col::8]

        n_pawn = 0

        rrow_str = ''.join(filter(lambda x: x != '.', r_row))
        if 'pR' in rrow_str:
            n_pawn += 1
    
        if 'Rp' in rrow_str:
            n_pawn += 1
        
        rcol_str = ''.join(filter(lambda x: x != '.', r_col))
        if 'pR' in rcol_str:
            n_pawn += 1
        
        if 'Rp' in rcol_str:
            n_pawn += 1

        return n_pawn
