"""
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of 
the numbers in the set got duplicated to another number in the set, which results in repetition of 
one number and loss of another number. Given an array nums representing the data status of this set 
after the error. Your task is to firstly find the number occurs twice and then find the number that 
is missing. Return them in the form of an array.

Example 1:

    Input: nums = [1,2,2,4]
    Output: [2,3]

Note:
    1. The given array size will in the range [2, 10000].
    2. The given array's numbers won't have any order.
"""


class Solution:
    def findErrorNums(self, nums):    # 232ms
        nums.sort()

        mis, n = 1, len(nums)
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                dup = nums[i]
            elif nums[i] > nums[i-1] + 1:
                mis = nums[i-1] + 1
        
        return [dup, mis] if nums[n-1] == n else [dup, n]

    def findErrorNums2(self, nums):    # 200ms
        d = {}
        for k in nums:
            if k in d:
                dup = k
            else:
                d[k] = 1

        for i in range(1, len(nums)+1):
            if i not in d:
                return [dup, i]

    def findErrorNums3(self, nums):    # 188ms
        n = len(nums)
        S = sum(set(nums))
        return [sum(nums) - S, n * (n + 1) / 2 - S]
