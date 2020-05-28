"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into 
a new one with different size but keep its original data. You're given a matrix represented 
by a two-dimensional array, and two positive integers r and c representing the row number and 
column number of the wanted reshaped matrix, respectively. The reshaped matrix need to be filled 
with all the elements of the original matrix in the same row-traversing order as they were. If 
the 'reshape' operation with given parameters is possible and legal, output the new reshaped 
matrix; Otherwise, output the original matrix.

Example 1:

    Input: 
        nums = [[1, 2], [3, 4]]
        r = 1, c = 4
    Output: 
        [[1, 2, 3, 4]]
    Explanation:
        The row-traversing of nums is [1, 2, 3, 4]. The new reshaped matrix is a 1 * 4 matrix, fill 
        it row by row by using the previous list.

Example 2:

    Input: 
        nums = [[1, 2], [3, 4]]
        r = 2, c = 4
    Output: 
        [[1, 2], [3, 4]]
    Explanation:
        There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

Note:
    1. The height and width of the given matrix is in range [1, 100].
    2. The given r and c are all positive.
"""


class Solution:
    def matrixReshape1(self, nums, r, c):    # 96ms
        elements = sum(nums, [])
        n = len(elements)
        if r * c != n:
            return nums
        else:
            return [elements[i:i+c] for i in range(0, n, c)]

    def matrixReshape2(self, nums, r, c):    # 88ms
        if len(nums[0]) * len(nums) != r * c:
            return nums
        else:
            elements = sum(nums, [])
            return [elements[i:i+c] for i in range(0, len(elements), c)]
