"""
Given an array A of integers, we must modify the array in the following way: we choose an i and replace 
A[i] with -A[i], and we repeat this process K times in total. (We may choose the same index i multiple 
times.) Return the largest possible sum of the array after modifying it in this way.

Example 1:

    Input: A = [4,2,3], K = 1
    Output: 5
    Explanation: Choose indices (1,) and A becomes [4,-2,3].

Example 2:

    Input: A = [3,-1,0,2], K = 3
    Output: 6
    Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].

Example 3:

    Input: A = [2,-3,-1,5,-4], K = 2
    Output: 13
    Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].

Note:
    1. 1 <= A.length <= 10000
    2. 1 <= K <= 10000
    3. -100 <= A[i] <= 100
"""


class Solution:
    def largestSumAfterKNegations1(self, A, K):    # 32ms
        A.sort()
        n = len(A)
        if K <= n and A[K-1] < 0:
            return sum(A) - 2 * sum(A[:K])
        
        i = 0
        while i < n and A[i] < 0:
            A[i] = -A[i]
            i += 1
        
        return sum(A) - (K - i) % 2 * min(A) * 2
