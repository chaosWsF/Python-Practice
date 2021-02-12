"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
    
    https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg

    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

Example 2:

    https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg

    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
    1. m == matrix.length
    2. n == matrix[i].length
    3. 1 <= m, n <= 10
    4. -100 <= matrix[i][j] <= 100
"""


class Solution:
    def spiralOrder(self, matrix):
        def helper(r0, c0, r1, c1):
            for c in range(c0, c1 + 1):
                yield r0, c
            
            for r in range(r0 + 1, r1 + 1):
                yield r, c1
            
            # multi-row and multi-col
            if r0 < r1 and c0 < c1:
                for c in range(c1 - 1, c0, -1):
                    yield r1, c
                
                for r in range(r1, r0, -1):
                    yield r, c0
        
        res = []
        r0, c0, r1, c1 = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        while r0 <= r1 and c0 <= c1:
            for r, c in helper(r0, c0, r1, c1):
                res.append(matrix[r][c])
            
            r0 += 1
            c0 += 1
            r1 -= 1
            c1 -= 1
        
        return res
