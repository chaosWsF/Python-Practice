"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

    Input: 16
    Output: true

Example 2:

    Input: 5
    Output: false

Follow up: Could you solve it without loops/recursion?
"""
from math import log10


class Solution:
    def isPowerOfFour1(self, num):
        """28ms"""
        num_bin = bin(num)
        return (num > 0) and (len(num_bin) % 2 == 0) and (num_bin.count('1') == 1)
    
    def isPowerOfFour2(self, num):
        """28ms"""
        k = 1
        while k < num:
            k <<= 2
        
        return k == num

    def isPowerOfFour3(self, num):
        """12ms"""
        return (num > 0) and ((log10(num) / log10(4)) % 1 == 0)
