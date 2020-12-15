"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

Example 2:

    Input: nums = []
    Output: []

Example 3:

    Input: nums = [0]
    Output: []

Constraints:
    1. 0 <= nums.length <= 3000
    2. -105 <= nums[i] <= 105
"""

from collections import defaultdict
from bisect import bisect_left


class Solution:
    def threeSum(self, nums):    # too slow
        if len(nums) < 3 or min(nums) > 0 or max(nums) < 0:
            return []
        
        nums.sort()
        res = set()
        for i in range(len(nums) - 1):
            d = set()
            cur = -nums[i]
            for j in range(i + 1, len(nums)):
                x = nums[j]
                if x in d:
                    res.add((-cur, x, cur - x))
                
                d.add(cur - x)
        
        return list(map(list, res))
    
    def threeSum2(self, nums):    # very fast
        if len(nums) < 3 or min(nums) > 0 or max(nums) < 0:
            return []
        
        d, res = defaultdict(int), []
        for x in nums:
            d[x] += 1
        
        nums = sorted(d)
        for k, x in enumerate(nums):
            if x > 0:
                break
            
            two_sum = -x
            num2_min, num2_max = two_sum - nums[-1], two_sum / 2

            i = bisect_left(nums, num2_min, k + 1)
            j = bisect_left(nums, num2_max, i)
            for num2 in nums[i:j]:
                num3 = two_sum - num2
                if num3 in d:
                    res.append([x, num2, num3])
        
        for x in nums:
            if d[x] > 1:
                if x == 0 and d[x] >= 3:
                    res.append([x, x, x])
                elif x != 0 and ((-2 * x) in d):
                    res.append([x, x, -2 * x])
        
        return res
