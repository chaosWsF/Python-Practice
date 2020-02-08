"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to
be a non-negative integer.

Since the return type is an integer, the decimal digits are
truncated and only the integer part of the result is returned.

Example 1:

    Input: 4
    Output: 2

Example 2:

    Input: 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since 
                 the decimal part is truncated, 2 is returned.
"""


class Solution:
    def mySqrt(self, x):
        """Not use it!"""
        return int(x**.5)
    
    def mySqrt2(self, x):
        """Newton's (Newton–Raphson) method"""
        if x == 0:
            return 0
        
        x_0 = 1 + x / 2
        while (int(x_0) * int(x_0) > x) or ((int(x_0) + 1) * (int(x_0) + 1) <= x):
            x_0 = (x_0 + x / x_0) / 2

        return int(x_0)

    def mySqrt3(self, x):
        """The Bisection Method"""
        i = 0
        j = x
        while i < j:
            m = (i + j) // 2
            if m * m > x:
                j = m - 1
            elif m * m == x:
                return m
            else:
                i = m + 1
        
        if i * i > x:
            return i - 1
        else:
            return i

    def mySqrt4(self, x):
        """The Secant Method"""
        if x == 0:
            return 0
        
        p_0 = 0
        p_1 = x
        p = p_1 - (p_1 * p_1 - x) / (p_1 + p_0)
        while (int(p) * int(p) > x) or ((int(p) + 1) * (int(p) + 1) <= x):
            p_0 = p_1
            p_1 = p
            p = p_1 - (p_1 * p_1 - x) / (p_1 + p_0)

        return int(p)
