"""
Given an array A of integers, return true if and only if it is a valid mountain array. Recall 
that A is a mountain array if and only if:

    1. A.length >= 3
    2. There exists some i with 0 < i < A.length - 1 such that:
        i. A[0] < A[1] < ... A[i-1] < A[i]
        ii. A[i] > A[i+1] > ... > A[A.length - 1]

https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png

Example 1:

    Input: [2,1]
    Output: false

Example 2:

    Input: [3,5,5]
    Output: false

Example 3:

    Input: [0,3,2,1]
    Output: true

Note:
1. 0 <= A.length <= 10000
2. 0 <= A[i] <= 10000 
"""


class Solution:
    def validMountainArray(self, A):
        if len(A) < 3:
            return False
        
        stage = 0
        for i in range(1, len(A)):
            if (A[i] == A[i-1]) or (i == 1 and A[i] < A[i-1]) or (stage == 1 and A[i] > A[i-1]):
                return False
            elif A[i] < A[i-1]:
                stage = 1
        
        return stage == 1
