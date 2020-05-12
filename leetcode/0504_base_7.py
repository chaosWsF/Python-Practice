"""
Given an integer, return its base 7 string representation.

Example 1:

    Input: 100
    Output: "202"

Example 2:

    Input: -7
    Output: "-10"

Note: The input will be in range of [-1e7, 1e7].
"""


class Solution:
    def convertToBase7(self, num):
        if num < 0:
            is_neg = True
            num = -num
        elif num > 0:
            is_neg = False
        else:
            return '0'

        res = []
        while num > 0:
            res.append(str(num % 7))
            num //= 7
        
        if is_neg:
            res.append('-')
        
        return ''.join(res)[::-1]
