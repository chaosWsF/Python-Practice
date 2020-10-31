"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

    Element at grid[i][j] moves to grid[i][j + 1].
    Element at grid[i][n - 1] moves to grid[i + 1][0].
    Element at grid[m - 1][n - 1] moves to grid[0][0].

Return the 2D grid after applying shift operation k times.

Example 1:

https://assets.leetcode.com/uploads/2019/11/05/e1.png

    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
    Output: [[9,1,2],[3,4,5],[6,7,8]]

Example 2:

https://assets.leetcode.com/uploads/2019/11/05/e2.png

    Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
    Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:

    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
    Output: [[1,2,3],[4,5,6],[7,8,9]]

Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m <= 50
    4. 1 <= n <= 50
    5. -1000 <= grid[i][j] <= 1000
    6. 0 <= k <= 100
"""


class Solution:
    def shiftGrid(self, grid, k: int):
        n = len(grid[0])
        tmp = sum(grid, [])
        l = len(tmp)
        k = k % l
        if k == 0:
            return grid
        else:
            res = tmp[-k:] + tmp[:-k]
            return [res[i:i+n] for i in range(0, l, n)]
