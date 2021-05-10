"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:

    https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg

    Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
    Output: 7
    Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

    Input: grid = [[1,2,3],[4,5,6]]
    Output: 12

Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m, n <= 200
    4. 0 <= grid[i][j] <= 100
"""


class Solution:
    def minPathSum(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    pass
                elif i == 0:
                    grid[i][j] += grid[0][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][0]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]
