"""
Given an array nums of n integers and an integer target, are there elements 
a, b, c, and d in nums such that a + b + c + d = target? Find all unique 
quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

Example 1:

    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

    Input: nums = [], target = 0
    Output: []

Constraints:
    1. 0 <= nums.length <= 200
    2. -109 <= nums[i] <= 109
    3. -109 <= target <= 109
"""


class Solution:
    def fourSum(self, nums, target: int):    # 80ms
        if not nums:
            return []
        
        n = len(nums)
        if n < 4:
            return []
        elif n == 4:
            return [nums] if sum(nums) == target else []
        
        nums.sort()
        res, M = set(), nums[-1]
        for i in range(n - 3):
            x = nums[i]
            if x + 3 * M < target:
                continue
            elif 4 * x > target:
                return res
            
            for j in range(i + 1, n - 2):
                y = nums[j]
                if x + y + 2 * M < target:
                    continue
                elif x + 3 * y > target:
                    break

                t_2sum = target - x - y
                a, b = j + 1, n - 1
                while a < b:
                    cur = nums[a] + nums[b]
                    if cur == t_2sum:
                        res.add((nums[i], nums[j], nums[a], nums[b]))
                        a += 1
                        b -= 1
                    elif cur < t_2sum:
                        a += 1
                    else:
                        b -= 1

        return res
        # return list(map(list, res))
