"""
Let's call an array A a mountain if the following properties hold:

    A.length >= 3
    There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]

Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

    Input: [0,1,0]
    Output: 1

Example 2:

    Input: [0,2,1,0]
    Output: 1

Note:
    1. 3 <= A.length <= 10000
    2. 0 <= A[i] <= 10^6
    3. A is a mountain, as defined above.
"""


class Solution:
    def peakIndexInMountainArray1(self, A):
        for i in range(len(A)):
            if A[i] > A[i + 1]:
                return i

    def peakIndexInMountainArray2(self, A):
        a, b = 0, len(A) - 1
        while a <= b:
            c = (a + b) // 2
            if A[c] < A[c + 1]:
                a = c + 1
            else:
                b = c - 1
        
        return a
