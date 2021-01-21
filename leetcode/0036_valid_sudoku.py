"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to 
the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

Example 1:

    <img>

    Input: board = 
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    Output: true

Example 2:

    Input: board = 
        [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
                 Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
    1. board.length == 9
    2. board[i].length == 9
    3. board[i][j] is a digit or '.'.
"""

import numpy as np


class Solution:
    def isValidSudoku1(self, board) -> bool:
        """
        A numpy-style solution
        Runtime: 220ms
        """
        def is_rep(a) -> bool:
            a_filtered = a[a != '.']
            a_filtered = a[np.where(a != '.')]
            return len(set(a_filtered)) != len(a_filtered)
        
        board = np.array(board)
        check_col = np.apply_along_axis(is_rep, 0, board)
        check_row = np.apply_along_axis(is_rep, 1, board)
        if any(check_col) or any(check_row):
            return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = board[i:i+3, j:j+3].flatten()
                if is_rep(box):
                    return False
        
        return True
