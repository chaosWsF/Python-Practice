"""
Given an array A of integers, return true if and only if we can partition the array into three non-empty 
parts with equal sums. Formally, we can partition the array if we can find indexes i+1 < j with 
(A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

Example 1:

    Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
    Output: true
    Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:

    Input: A = [0,2,1,-6,6,7,9,-1,2,0,1]
    Output: false

Example 3:

    Input: A = [3,3,6,5,-2,2,5,1,-9,4]
    Output: true
    Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

Constraints:
    1. 3 <= A.length <= 50000
    2. -10^4 <= A[i] <= 10^4
"""


class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        S = sum(A)
        if S % 3 == 0:
            S_P = S / 3
            cur = A[0]
            for i in range(1, len(A)-2):
                if cur == S_P:
                    cur = A[i]
                    for j in range(i+1, len(A)-1):
                        if cur == S_P:
                            return True
                        else:
                            cur += A[j]
                    
                    if cur == S_P:
                        return A[-1] == S_P
                else:
                    cur += A[i]

            if cur == S_P:
                return A[-1] == S_P

        return False