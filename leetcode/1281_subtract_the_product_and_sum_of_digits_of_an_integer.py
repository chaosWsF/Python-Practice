"""
Given an integer number n, return the difference between the 
product of its digits and the sum of its digits.

Example 1:

    Input: n = 234
    Output: 15 
    Explanation: 
        Product of digits = 2 * 3 * 4 = 24 
        Sum of digits = 2 + 3 + 4 = 9 
        Result = 24 - 9 = 15

Example 2:

    Input: n = 4421
    Output: 21
    Explanation: 
        Product of digits = 4 * 4 * 2 * 1 = 32 
        Sum of digits = 4 + 4 + 2 + 1 = 11 
        Result = 32 - 11 = 21

Constraints:
    1. 1 <= n <= 10^5
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        S, P = 0, 1
        for s in str(n):
            i = int(s)
            S += i
            P *= i
        
        return P - S

    def subtractProductAndSum2(self, n: int) -> int:
        """
        faster
        """
        S, P = 0, 1
        while n > 0:
            i = n % 10
            S += i
            P *= i
            n //= 10
        
        return P - S
