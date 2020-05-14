"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

Example:

    Input: 28
    Output: True
    Explanation: 28 = 1 + 2 + 4 + 7 + 14

Note: The input number n will not exceed 100,000,000. (1e8)
"""


class Solution:
    def checkPerfectNumber(self, num):    # 36ms
        if num <= 2:
            return False
        
        div_sum = 1
        for i in range(2, int(num**.5)+1):
            if num % i == 0:
                div_sum += i + num // i
        
        return div_sum == num

    def checkPerfectNumber2(self, num):    # 20ms, list of perfect of number based on Mersenne prime
        return num in set([6, 28, 496, 8128, 33550336])
