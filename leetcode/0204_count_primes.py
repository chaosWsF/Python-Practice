"""
Count the number of prime numbers less than a non-negative number, n.

Example:
    Input: 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""


class Solution:
    def countPrimes(self, n):
        """sieve of Eratosthenes (80ms)"""
        nums = [True] * n
        for i in range(3, int(n ** .5) + 1, 2):
            if nums[i]:
                nums[i*i::2*i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
        
        return len(list(filter(None, nums[3::2]))) + 1 if n > 2 else 0
