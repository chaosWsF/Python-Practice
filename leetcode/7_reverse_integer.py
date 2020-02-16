"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

    Input: 123
    Output: 321

Example 2:

    Input: -123
    Output: -321

Example 3:

    Input: 120
    Output: 21

Note:
Assume we are dealing with an environment which could only store 
integers within the 32-bit signed integer range: 
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that 
your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        """a direct solution"""
        if x < 0:
            sig = True
            x = -x
        else:
            sig = False
        
        x_reverse = 0
        while x > 0:
            x_reverse = x_reverse * 10 + x % 10
            x = x // 10
        
        if sig:
            x_reverse = -x_reverse

        if -2**31 <= x_reverse < 2**31:
            return x_reverse
        else:
            return 0

    def reverse2(self, x):
        """string method"""
        if x >= 0:
            x = int(str(x)[::-1])
        else:
            x = -int(str(-x)[::-1])
        
        if -2**31 <= x < 2**31:
            return x
        else:
            return 0
    
    def reverse3(self, x):
        """binary method"""
        from math import log10

        sig = pow(-1, (x < 0))
        x = sig * x
        n = int(log10(x)) + 1
        # n = len(str(x))
        for i in range(n // 2):
            up_dig = x // 10**(n-1-i) % 10
            low_dig = x // 10**i % 10
            delta = up_dig - low_dig
            x += delta * 10**i - delta * 10**(n-1-i)
        
        x = sig * x
        if -2**31 <= x < 2**31:
            return x
        else:
            return 0
