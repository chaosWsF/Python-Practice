"""
On a N * N grid, we place some 1 * 1 * 1 cubes. Each value v = grid[i][j] represents a tower of v cubes 
placed on top of grid cell (i, j). Return the total surface area of the resulting shapes.

Example 1:

    Input: [[2]]
    Output: 10

Example 2:

    Input: [[1,2],[3,4]]
    Output: 34

Example 3:

    Input: [[1,0],[0,2]]
    Output: 16

Example 4:

    Input: [[1,1,1],[1,0,1],[1,1,1]]
    Output: 32

Example 5:

    Input: [[2,2,2],[2,1,2],[2,2,2]]
    Output: 46

Note:
    1. 1 <= N <= 50
    2. 0 <= grid[i][j] <= 50
"""


class Solution:
    def surfaceArea(self, grid):
        """slower, O(N^2)"""
        N, res = len(grid), 0
        for i in range(N):
            for j in range(N):
                v = grid[i][j]
                if v > 0:
                    res += 2
                    for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                        if 0 <= x < N and 0 <= y < N:
                            v_n = grid[x][y]
                        else:
                            v_n = 0

                        res += max(v - v_n, 0)
        
        return res

    def surfaceArea2(self, grid):
        S1 = sum(x > 0 for row in grid for x in row)

        S2 = 0
        for row in grid:
            prev = 0
            for x in row:
                if x > prev:
                    S2 += x - prev
                
                prev = x

        S3 = 0
        for i in range(len(grid[0])):
            prev = 0
            for row in grid:
                if row[i] > prev:
                    S3 += row[i] - prev
                
                prev = row[i]
        
        return 2 * (S1 + S2 + S3)
