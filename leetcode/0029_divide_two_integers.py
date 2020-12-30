"""
Given two integers dividend and divisor, divide two integers without using 
multiplication, division and mod operator.

Return the q after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

    Input: dividend = 10, divisor = 3
    Output: 3

Example 2:

    Input: dividend = 7, divisor = -3
    Output: -2

Note:
    1. Both dividend and divisor will be 32-bit signed integers.
    2. The divisor will never be 0.
    3. Assume we are dealing with an environment which could only store integers 
       within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For the purpose 
       of this problem, assume that your function returns 2^31 − 1 when the division 
       result overflows.
"""


class Solution:
    def divide1(self, dividend: int, divisor: int) -> int:
        """
        Using stepwise range()
        """
        sig = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)

        if divisor == 1:
            result = dividend
        else:
            result = len(range(0, dividend + 1, divisor)) - 1

        if sig:
            return max(-result, -2**31)
        else:
            return min(result, 2**31 - 1)

    def divide2(self, dividend: int, divisor: int) -> int:
        """
        Bitwise Operation
        """
        sig = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)

        q = 0
        while dividend >= divisor:
            cur_q, cur_d = self._bit_size(dividend, divisor)
            q += cur_q
            dividend -= cur_d
        
        if sig:
            return max(-q, -2**31)
        else:
            return min(q, 2**31 - 1)

    def _bit_size(self, dividend: int, divisor: int):
        """
        To find max bit size
        """
        q = 1
        while divisor < dividend:
            divisor <<= 1
            q <<= 1
        
        if divisor == dividend:
            return q, divisor
        else:
            return q >> 1, divisor >> 1
