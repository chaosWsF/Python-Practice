"""
Implement pow(x, n), which calculates x raised to the power n.

Example 1:

    Input: 2.00000, 10
    Output: 1024.00000

Example 2:

    Input: 2.10000, 3
    Output: 9.26100

Example 3:

    Input: 2.00000, -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:
    1. -100.0 < x < 100.0
    2. n is a 32-bit signed integer, within the range 
    3. [−2^31, 2^31 − 1]
"""


class Solution:
    def myPow(self, x, n):
        """Binary Search"""
        if n == 0:
            return 1
        
        # 0's negative power = inf
        if x == 0:
            return 0
        
        if n < 0:
            n = -n
            x = 1 / x

        sig = (n % 2 == 1) and (x < 0)
        x = abs(x)

        result = 1
        while n > 0:
            cur_pow = 1
            cur_result = x
            while cur_pow <= n:
                cur_pow <<= 1
                if cur_pow <= n:
                    cur_result *= cur_result
            
            n -= cur_pow >> 1
            result *= cur_result

        if sig:
            return -result
        else:
            return result
