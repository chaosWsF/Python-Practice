"""
Count the number of prime numbers less than a non-negative number, n.

Example:
    Input: 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""


class Solution:
    def countPrimes1(self, n):
        """sieve of Eratosthenes"""
        d = [True] * (n + 1)
        res = 0
        for i in range(2, int(n ** .5) + 1):
            if d[i]:
                j = i * i
                while j < n:
                    if d[j]:
                        d[j] = False
                        res += 1
                    j += i
        
        return n - 2 - res if n > 2 else 0

    def countPrimes2(self, n):
        """Euler's sieve"""
        nums = list(range(3, n, 2))
        ps = [2]
        while nums:
            p = nums[0]
            ps.append(p)
            for i in range(0, len(nums), p):
                nums[i] = 0
            nums = list(filter(None, nums))
        
        return len(ps) if n > 2 else 0
