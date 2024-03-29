"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed 
by all the odd elements of A. You may return any answer array that satisfies this condition.

Example 1:

    Input: [3,1,2,4]
    Output: [2,4,3,1]
    The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:
    1. 1 <= A.length <= 5000
    2. 0 <= A[i] <= 5000
"""


class Solution:
    def sortArrayByParity1(self, A):
        lst_1, lst_2 = [], []
        for a in A:
            if a % 2 == 0:
                lst_1.append(a)
            else:
                lst_2.append(a)
        
        return lst_1 + lst_2

    def sortArrayByParity2(self, A):
        return sorted(A, key=lambda x: x % 2)
