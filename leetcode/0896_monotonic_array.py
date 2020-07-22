"""
An array is monotonic if it is either monotone increasing or monotone decreasing. An array A is monotone 
increasing if for all i <= j, A[i] <= A[j]. An array A is monotone decreasing if for all i <= j, 
A[i] >= A[j]. Return true if and only if the given array A is monotonic.

Example 1:

    Input: [1,2,2,3]
    Output: true

Example 2:

    Input: [6,5,4,4]
    Output: true

Example 3:

    Input: [1,3,2]
    Output: false

Example 4:

    Input: [1,2,4,5]
    Output: true

Example 5:

    Input: [1,1,1]
    Output: true

Note:
    1. 1 <= A.length <= 50000
    2. -100000 <= A[i] <= 100000
"""


class Solution:
    def isMonotonic1(self, A):
        return (A == sorted(A) or A == sorted(A, reverse=True))

    def isMonotonic2(self, A):
        prev = flag = None    # flag - {1: increasing, -1: decreasing}
        for x in A:
            if prev is not None:
                if x > prev:
                    if flag is None:
                        flag = 1
                    elif flag == -1:
                        return False
                elif x < prev:
                    if flag is None:
                        flag = -1
                    elif flag == 1:
                        return False
            
            prev = x

        return True

        # flag = None    # flag - {1: increasing, -1: decreasing}
        # for i in range(1, len(A)):
        #     if A[i] > A[i-1]:
        #         if flag is None:
        #             flag = 1
        #         elif flag == -1:
        #             return False
        #     elif A[i] < A[i-1]:
        #         if flag is None:
        #             flag = -1
        #         elif flag == 1:
        #             return False
        # 
        # return True
