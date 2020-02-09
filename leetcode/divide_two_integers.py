"""
Given two integers dividend and divisor, divide two integers 
without using multiplication, division and mod operator.

Return the q after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

    Input: dividend = 10, divisor = 3
    Output: 3

Example 2:

    Input: dividend = 7, divisor = -3
    Output: -2

Note:

    Both dividend and divisor will be 32-bit signed integers.
    The divisor will never be 0.
    Assume we are dealing with an environment which could only 
    store integers within the 32-bit signed integer range: 
    [−2^31, 2^31 − 1]. For the purpose of this problem, assume 
    that your function returns 2^31 − 1 when the division result 
    overflows.
"""


class Solution:
    def divide1(self, dividend, divisor):
        """Use Range Stepwise"""
        sig = (dividend > 0) ^ (divisor > 0)
        if abs(divisor) == 1:
            result = 1
        else:
            result = len(range(0, abs(dividend) + 1, abs(divisor))) - 1

        if sig:
            return max(-result, -2**31)
        else:
            return min(result, 2**31 - 1)

    def divide2(self, dividend, divisor):
        """While Loop (Bitwise Operation)"""
        sig = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        q = 0
        while dividend >= divisor:
            cur_q, cur_d = self._bit_size(dividend, divisor)
            q += cur_q
            dividend -= cur_d
        
        if sig:
            return max(-q, -2**31)
        else:
            return min(q, 2**31 - 1)

    def _bit_size(self, dividend, divisor):
        """find max bit size"""
        q = 1
        while divisor < dividend:
            divisor <<= 1
            q <<= 1
        
        if divisor == dividend:
            return q, divisor
        else:
            return q >> 1, divisor >> 1
