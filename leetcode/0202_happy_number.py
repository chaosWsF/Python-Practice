"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive 
integer, replace the number by the sum of the squares of its digits, and repeat the process 
until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does 
not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 
    Input: 19
    Output: true
    Explanation: 
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        """
            tortoise and hare for detecting loop
        """
        def get_next(num: int) -> int:
            total_sum = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total_sum += digit * digit
            
            return total_sum
        
        tortoise = n
        hare = get_next(n)
        while hare != 1 and hare != tortoise:
            tortoise = get_next(tortoise)
            hare = get_next(get_next(hare))
        
        return hare == 1
    
    def isHappy1(self, n):    # 28ms
        def helper(n):
            res = 0
            n = str(n)
            for s in n:
                res += int(s) * int(s)
            return res
        
        while n >= 10:
            n = helper(n)
        
        return n in [1, 7]

    def isHappy2(self, n):    # 28ms
        def helper(n):
            res = 0
            while n > 0:
                res += (n % 10) * (n % 10)
                n //= 10
            return res
        
        while n >= 10:
            n = helper(n)
        
        return n in [1, 7]
    
    def isHappy3(self, n):    # 24ms
        used_nums = {}
        while (n != 1) and (n not in used_nums):
            used_nums[n] = 1
            n = sum(int(s) * int(s) for s in str(n))
        return n == 1
