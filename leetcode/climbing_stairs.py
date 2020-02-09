"""
You are climbing a stair case. It takes n steps to reach to the 
top.

Each time you can either climb 1 or 2 steps. In how many distinct
ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:

    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
"""


class Solution:
    def climbStairs1(self, n):
        """Combination Formula (builtin)"""
        from math import comb
        n_ways = 0
        for x in range(n // 2 + 1):
            n_ways += comb(n - x, x)
        return n_ways

    def climbStairs2(self, n):
        """Combination Formula"""
        n_ways = 0
        for x in range(n // 2 + 1):
            c = 1
            for r in range(1, x + 1):
                c *= (n - x + 1 - r) / r
            n_ways += c
        return int(n_ways)
    
    def climbStairs3(self, n):
        """Fibonacci Sequence (Formula)"""
        r_1 = (1 + 5 ** .5) / 2
        r_2 = (1 - 5 ** .5) / 2
        n_ways = (r_1 ** (n + 1) - r_2 ** (n + 1)) / (r_1 - r_2)
        return int(n_ways)
    
    def climbStairs4(self, n):
        """Fibonacci Sequence (Recurrence)"""
        f_0 = 1
        f_1 = 1
        for _ in range(1, n):
            f_2 = f_0 + f_1
            f_0 = f_1
            f_1 = f_2
        return f_1

    def climbStairs5(self, n):
        """Fibonacci Sequence (Matrix Form)"""
        def fib(n):
            """Calculate (F(n), F(n+1))"""
            k = n // 2
            if k == 0:
                return (0, 1)
            else:
                f_0, f_1 = fib(k)
                f_2 = f_0 * f_0 + f_1 * f_1
                f_3 = (2 * f_0 + f_1) * f_1
                if n % 2 == 0:
                    return (f_2, f_3)
                else:
                    return (f_3, f_2 + f_3)
        
        return fib(n - 2)[0]
