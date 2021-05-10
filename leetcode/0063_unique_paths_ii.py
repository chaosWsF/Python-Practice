"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Example 1:

    https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg

    Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    Output: 2
    Explanation: There is one obstacle in the middle of the 3x3 grid above.
    There are two ways to reach the bottom-right corner:
    1. Right -> Right -> Down -> Down
    2. Down -> Down -> Right -> Right

Example 2:

    https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg

    Input: obstacleGrid = [[0,1],[0,0]]
    Output: 1

Constraints:
    1. m == obstacleGrid.length
    2. n == obstacleGrid[i].length
    3. 1 <= m, n <= 100
    4. obstacleGrid[i][j] is 0 or 1.
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        pass
