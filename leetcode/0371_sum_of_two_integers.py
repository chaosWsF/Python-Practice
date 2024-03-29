"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

    Input: a = 1, b = 2
    Output: 3

Example 2:

    Input: a = -2, b = 3
    Output: 1
"""


class Solution:
    def getSum(self, a, b):
        mask = 2 ** 32 - 1
        while b & mask:
            a, b = (a ^ b), ((a & b) << 1)
        
        return a & mask if b > mask else a
