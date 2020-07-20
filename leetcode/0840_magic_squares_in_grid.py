"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all 
have the same sum. Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

Example 1:

    Input: [[4,3,8,4],
            [9,5,1,9],
            [2,7,6,2]]
    Output: 1
    Explanation: 
        The following subgrid is a 3 x 3 magic square:
            4 3 8
            9 5 1
            2 7 6
        while this one is not:
            3 8 4
            5 1 9
            7 6 2
        In total, there is only one magic square inside the given grid.

Note:
    1. 1 <= grid.length <= 10
    2. 1 <= grid[0].length <= 10
    3. 0 <= grid[i][j] <= 15
"""


class Solution:
    def numMagicSquaresInside(self, grid):
        def checker(a, b, c, d, e, f, g, h, i):
            """http://www.mathematische-basteleien.de/magsquare.htm"""
            return (
                e == 5 and 
                sorted([a, b, c, d, e, f, g, h, i]) == [1, 2, 3, 4, 5, 6, 7, 8, 9] and 
                (a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i == c+e+g == 15)
            )
        
        return sum(
            checker(
                grid[r][c], grid[r][c+1], grid[r][c+2], 
                grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2], 
                grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]
            ) for c in range(len(grid[0]) - 2) for r in range(len(grid) - 2)
        )
