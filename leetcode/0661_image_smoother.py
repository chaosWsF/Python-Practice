"""
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to 
make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding 
cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:

    Input:
        [[1,1,1],
         [1,0,1],
         [1,1,1]]
    Output:
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    Explanation:
        For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
        For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
        For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Note:
    The value in the given matrix is in the range of [0, 255].
    The length and width of the given matrix are in the range of [1, 150].
"""

import numpy as np


class Solution:
    def imageSmoother(self, M):
        nrow, ncol = len(M), len(M[0])
        res = [[0] * ncol for _ in range(nrow)]

        for i in range(nrow):
            for j in range(ncol):
                filter_sum = 0
                n = 0
                for r in [i-1, i, i+1]:
                    for c in [j-1, j, j+1]:
                        if 0 <= r < nrow and 0 <= c < ncol:
                            filter_sum += M[r][c]
                            n += 1
                
                res[i][j] += filter_sum // n

        return res

    def imageSmoother2(self, M):    # slow
        nrow, ncol = len(M), len(M[0])
        res = []
        for i in range(nrow):
            cur = []
            for j in range(ncol):
                selected = []
                for r in set([max(0, i-1), i, min(i+1, nrow-1)]):
                    for c in set([max(0, j-1), j, min(j+1, ncol-1)]):
                        selected.append(M[r][c])

                cur.append(sum(selected) // len(selected))
            
            res.append(cur)

        return res
