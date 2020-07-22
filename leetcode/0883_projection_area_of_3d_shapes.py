"""
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes. Each value 
v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j). Now we view the projection 
of these cubes onto the xy, yz, and zx planes. A projection is like a shadow, that maps our 3 dimensional 
figure to a 2 dimensional plane. Here, we are viewing the "shadow" when looking at the cubes from the top, 
the front, and the side. Return the total area of all three projections. 

Example 1:

    Input: [[2]]
    Output: 5

Example 2:

    Input: [[1,2],[3,4]]
    Output: 17
    Explanation: Here are the three projections ("shadows") of the shape made with each axis-aligned plane.

        https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/02/shadow.png

Example 3:

    Input: [[1,0],[0,2]]
    Output: 8

Example 4:

    Input: [[1,1,1],[1,0,1],[1,1,1]]
    Output: 14

Example 5:

    Input: [[2,2,2],[2,1,2],[2,2,2]]
    Output: 21

Note:
    1. 1 <= grid.length = grid[0].length <= 50
    2. 0 <= grid[i][j] <= 50
"""


class Solution:
    def projectionArea1(self, grid):
        return sum(x > 0 for row in grid for x in row) + sum(map(max, grid)) + sum(map(max, zip(*grid)))

    def projectionArea2(self, grid):
        """slower"""
        N, res = len(grid), 0
        for r in range(N):
            max_row = max_col = 0
            for c in range(N):
                if grid[r][c] > 0:
                    res += 1

                max_row = max(max_row, grid[r][c])
                max_col = max(max_col, grid[c][r])

            res += max_row + max_col

        return res
