"""
Given an array nums of n integers and an integer target, find three integers in nums such that 
the sum is closest to target. Return the sum of the three integers. You may assume that each 
input would have exactly one solution.

Example 1:

    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Constraints:
    1. 3 <= nums.length <= 10^3
    2. -10^3 <= nums[i] <= 10^3
    3. -10^4 <= target <= 10^4
"""


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        """
        Two pointers
        """
        nums.sort()
        n, dist = len(nums), float('inf')
        for i in range(n - 2):
            a, b = i + 1, n - 1
            while a < b:
                cur = target - nums[i] - nums[a] - nums[b]
                if abs(cur) < abs(dist):
                    dist = cur
                
                if cur > 0:
                    a += 1
                else:
                    b -= 1
                
                if dist == 0:
                    return target - dist
        
        return target - dist
