"""
Given a matrix A, return the transpose of A. The transpose of a matrix is the matrix flipped over it's 
main diagonal, switching the row and column indices of the matrix.

    https://assets.leetcode.com/uploads/2019/10/20/hint_transpose.png

Example 1:

    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:

    Input: [[1,2,3],[4,5,6]]
    Output: [[1,4],[2,5],[3,6]] 

Note:
    1. 1 <= A.length <= 1000
    2. 1 <= A[0].length <= 1000
"""

import numpy as np


class Solution:
    def transpose1(self, A):
        C = len(A[0])
        A = sum(A, [])
        return [A[i::C] for i in range(C)]

    def transpose2(self, A):
        return np.array(A).T.tolist()
    
    def transpose3(self, A):
        return [[row[i] for row in A] for i in range(len(A[0]))]
