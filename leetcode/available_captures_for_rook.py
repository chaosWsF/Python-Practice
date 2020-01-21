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
        board_square = []
        for row in board:
            board_square.extend(row)

        square_index = board_square.index('R')

        n_pawn = 0

        r_row = square_index // 8
        for up in range(r_row):
            if board_square[square_index - 8 * (up + 1)] == 'p':
                n_pawn += 1
                break
            elif board_square[square_index - 8 * (up + 1)] == 'B':
                break
        
        for down in range(7 - r_row):
            if board_square[square_index + 8 * (down + 1)] == 'p':
                n_pawn += 1
                break
            elif board_square[square_index + 8 * (down + 1)] == 'B':
                break
        
        r_col = square_index % 8
        for left in range(r_col):
            if board_square[square_index - left - 1] == 'p':
                n_pawn += 1
                break
            elif board_square[square_index - left - 1] == 'B':
                break
        
        for right in range(7 - r_col):
            if board_square[square_index + right + 1] == 'p':
                n_pawn += 1
                break
            elif board_square[square_index + right + 1] == 'B':
                break
        
        return n_pawn