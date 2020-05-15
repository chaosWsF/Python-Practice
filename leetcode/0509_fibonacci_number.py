"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
    
    F(0) = 0,   F(1) = 1
    F(N) = F(N - 1) + F(N - 2), for N > 1.

Given N, calculate F(N). 

Example 1:

    Input: 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

    Input: 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:

    Input: 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Note:
    0 ≤ N ≤ 30.
"""


class Solution:
    def fib(self, N):
        r_1 = (1 + 5 ** .5) / 2
        r_2 = (1 - 5 ** .5) / 2
        return int((r_1 ** N - r_2 ** N) / (r_1 - r_2))

    def fib2(self, N):
        if N == 0:
            return 0
        
        f_0 = 0
        f_1 = 1
        for _ in range(N - 1):
            f_2 = f_0 + f_1
            f_0 = f_1
            f_1 = f_2
        
        return f_1

    def fib3(self, N):
        def helper(n):
            k = n // 2
            if k == 0:
                return (0, 1)
            else:
                f_0, f_1 = helper(k)
                f_2 = f_0 * f_0 + f_1 * f_1
                f_3 = (2 * f_0 + f_1) * f_1
                if n % 2 == 0:
                    return (f_2, f_3)
                else:
                    return (f_3, f_2 + f_3)
        
        return helper(N + 1)[0]
