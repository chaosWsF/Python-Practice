"""
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, 
formed from 3 of these lengths. If it is impossible to form any triangle of non-zero area, return 0.

Example 1:

    Input: [2,1,2]
    Output: 5

Example 2:

    Input: [1,2,1]
    Output: 0

Example 3:

    Input: [3,2,3,4]
    Output: 10

Example 4:

    Input: [3,6,2,3]
    Output: 8

Note:
    1. 3 <= A.length <= 10000
    2. 1 <= A[i] <= 10^6
"""


class Solution:
    def largestPerimeter(self, A):
        A.sort(reverse=True)
        i = 0
        while i < len(A) - 2:
            a, b, c = A[i:i+3]
            if b + c > a:
                return a + b + c
            else:
                i += 1
        
        return 0
