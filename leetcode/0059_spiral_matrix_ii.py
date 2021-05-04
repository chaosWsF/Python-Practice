"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

Example 1:

    https://assets.leetcode.com/uploads/2020/11/13/spiraln.jpg

    Input: n = 3
    Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

    Input: n = 1
    Output: [[1]]

Constraints:
    1 <= n <= 20
"""


class Solution:
    def generateMatrix(self, n: int):    # 24ms
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        x = 1

        def helper(r0, c0, r1, c1, x0):
            for c in range(c0, c1 + 1):
                matrix[r0][c] = x0
                x0 += 1
            
            for r in range(r0 + 1, r1 + 1):
                matrix[r][c1] = x0
                x0 += 1
            
            if r0 < r1 and c0 < c1:    # multi-row and multi-col
                for c in range(c1 - 1, c0, -1):
                    matrix[r1][c] = x0
                    x0 += 1
                
                for r in range(r1, r0, -1):
                    matrix[r][c0] = x0
                    x0 += 1

            return x0


        r0, c0, r1, c1 = 0, 0, len(matrix)-1, len(matrix[0])-1
        while r0 <= r1 and c0 <= c1:
            x = helper(r0, c0, r1, c1, x)
            r0 += 1
            c0 += 1
            r1 -= 1
            c1 -= 1
        
        return matrix
