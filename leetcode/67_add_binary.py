"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters
1 or 0.

Example 1:

    Input: a = "11", b = "1"
    Output: "100"

Example 2:

    Input: a = "1010", b = "1011"
    Output: "10101"
"""


class Solution:
    def addBinary1(self, a, b):
        """Convert into binary integer (builtin)"""
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary2(self, a, b):
        """Convert into digit adding"""
        if len(a) < len(b):
            tmp = a
            a = b
            b = tmp
        
        c = ''
        i = 1
        carrier = 0
        while i <= len(a):
            if i <= len(b):
                d = int(a[-i]) + int(b[-i]) + carrier
            else:
                d = int(a[-i]) + carrier
            
            if d >= 2:
                c += str(d - 2)
                carrier = 1
            else:
                c += str(d)
                carrier = 0

            i += 1
        
        if carrier == 0:
            return c[::-1]
        else:
            return '1' + c[::-1]
