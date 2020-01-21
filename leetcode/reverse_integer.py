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
Assume we are dealing with an environment which could only store integers within 
the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        """a direct solution"""
        if -10 < x < 10:
            return x
        elif x <= -10:
            sig = -1
            x = -x
        else:
            sig = 1
        
        digits = []
        while x > 0:
            digits.append(x % 10)
            x = x // 10
        
        for i, d in enumerate(digits):
            x += d * 10 ** (len(digits)-1-i)
        
        x = sig * x

        if -2**31 <= x < 2**31:
            return x
        else:
            return 0

    def reverse2(self, x):
        """string method"""
        if x >=0:
            x = int(str(x)[::-1])
        else:
            x = -int(str(abs(x))[::-1])
        
        if -2**31 <= x < 2**31:
            return x
        else:
            return 0
