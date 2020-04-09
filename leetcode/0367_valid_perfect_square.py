"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

    Input: 16
    Output: true

Example 2:

    Input: 14
    Output: false
"""


class Solution:
    def isPerfectSquare(self, num):  # 16ms
        if (num % 4) not in [0, 1]:
            return False
        
        a = 1
        b = num
        while a <= b:
            c = (a + b) // 2
            tmp = c * c
            if tmp > num:
                b = c - 1
            elif tmp == num:
                return True
            else:
                a = c + 1
        
        return False
