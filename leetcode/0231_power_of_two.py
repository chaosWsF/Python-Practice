"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

    Input: 1
    Output: true 
    Explanation: 2^0 = 1

Example 2:

    Input: 16
    Output: true
    Explanation: 2^4 = 16

Example 3:

    Input: 218
    Output: false
"""


class Solution:
    def isPowerOfTwo1(self, n):
        """20ms"""
        return (n > 0) and (bin(n).count('1') == 1)
        # return (n > 0) and (sum(int(s) for s in bin(n)[2:]) == 1)

    def isPowerOfTwo2(self, n):
        """32ms"""
        k = 1
        while k < n:
            k <<= 1
        
        return k == n

    def isPowerOfTwo3(self, n):
        """24ms"""
        return (n > 0) and (n & (n - 1) == 0)
        # return not n & (n - 1) if n else False
