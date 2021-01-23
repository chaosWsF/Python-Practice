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
    1. The length of both num1 and num2 is < 110.
    2. Both num1 and num2 contain only digits 0-9.
    3. Both num1 and num2 do not contain any leading zero, except the
       number 0 itself.
    4. You must not use any built-in BigInteger library or convert 
       the inputs to integer directly.
"""


class Solution:
    def multiply1(self, num1: str, num2: str) -> str:
        """
        Direct arithmetic multiplication
        Runtime: 196ms
        """
        return str(sum([
            ( int(num1[-i]) * int(num2[-j]) * 10 ** (i + j - 2) ) 
            for i in range(1, len(num1) + 1) 
            for j in range(1, len(num2) + 1)
        ]))

    def multiply2(self, num1: str, num2: str) -> str:
        """
        Karatsuba Algorithm for large numbers, https://en.wikipedia.org/wiki/Karatsuba_algorithm
        Runtime: 108ms
        """
        n_1, n_2 = len(num1), len(num2)
        if (n_1 < 2) or (n_2 < 2):
            return str(int(num1) * int(num2))
        
        m = min(n_1, n_2) // 2

        high_1, low_1 = num1[:-m], num1[-m:]
        high_2, low_2 = num2[:-m], num2[-m:]

        z_0 = int(self.multiply2(low_1, low_2))
        z_1 = int(self.multiply2(str(int(low_1) + int(high_1)), str(int(low_2) + int(high_2))))
        z_2 = int(self.multiply2(high_1, high_2))

        return str(z_2 * 10 ** (2 * m) + (z_1 - z_2 - z_0) * 10 ** m + z_0)

    def multiply0(self, num1: str, num2: str) -> str:    # 28ms
        return str(int(num1) * int(num2))
