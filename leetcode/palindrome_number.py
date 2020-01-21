"""
Determine whether an integer is a palindrome. An integer is a 
palindrome when it reads the same backward as forward.

Example 1:

    Input: 121
    Output: true

Example 2:

    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right 
    to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is 
    not a palindrome.

Follow up:

Coud you solve it without converting the integer to a string?
"""


class Solution:
    def isPalindrome(self, x):
        """only use integer"""
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            digits = []
            while x > 0:
                digits.append(x % 10)
                x = x // 10
            
            return digits[::-1] == digits
    
    def isPalindrome2(self, x):
        """use integer and math module"""
        from math import log10

        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            n = int(log10(x)) + 1
            for i in range(n // 2):
                up_dig = x // 10**(n-1-i) % 10
                low_dig = x // 10**i % 10
                if up_dig != low_dig:
                    return False
            
            return True
    
    def isPalindrome3(self, x):
        """string method"""
        return str(x)[::-1] == str(x)
