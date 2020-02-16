"""
Given two non-negative integers num1 and num2 represented as 
strings, return the product of num1 and num2, also represented
as a string.

Example 1:

    Input: num1 = "2", num2 = "3"
    Output: "6"

Example 2:

    Input: num1 = "123", num2 = "456"
    Output: "56088"

Note:

    The length of both num1 and num2 is < 110.
    Both num1 and num2 contain only digits 0-9.
    Both num1 and num2 do not contain any leading zero, except the
    number 0 itself.
    You must not use any built-in BigInteger library or convert 
    the inputs to integer directly.
"""


class Solution:
    def multiply1(self, num1, num2):
        """Direct"""
        if len(num1) > len(num2):
            tmp = num2
            num2 = num1
            num1 = tmp
        
        i = 1
        result = 0
        while i <= len(num1):
            j = 1
            while j <= len(num2):
                result += int(num1[-i]) * int(num2[-j]) * 10 ** (i + j - 2)
                j += 1
            
            i += 1

        return str(result)

    def multiply2(self, num1, num2):
        """Karatsuba Algorithm"""
        if (len(num1) < 2) or (len(num2) < 2):
            return str(int(num1) * int(num2))
        
        m = min(len(num1), len(num2)) // 2

        high1, low1 = num1[:-m], num1[-m:]
        high2, low2 = num2[:-m], num2[-m:]

        z0 = int(self.multiply2(low1, low2))
        z1 = int(self.multiply2(str(int(low1) + int(high1)), str(int(low2) + int(high2))))
        z2 = int(self.multiply2(high1, high2))

        return str(z2 * 10 ** (2 * m) + (z1 - z2 - z0) * 10 ** m + z0)
