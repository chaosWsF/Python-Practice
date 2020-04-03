"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

    Input: 27
    Output: true

Example 2:

    Input: 0
    Output: false

Example 3:

    Input: 9
    Output: true

Example 4:

    Input: 45
    Output: false

Follow up:
    Could you do it without using any loop / recursion?
"""
from math import log10


class Solution:
    def isPowerOfThree1(self, n):
        """The solution cannot pass if we use log or log2 due to precision errors."""
        return (n > 0) and ((log10(n) / log10(3)) % 1 == 0)
    
    def isPowerOfThree2(self, n):
        """The integer has the limit 32bits, 3**19 < 2**31 - 1 < 3**20"""
        return (n > 0) and (1162261467 % n == 0)
