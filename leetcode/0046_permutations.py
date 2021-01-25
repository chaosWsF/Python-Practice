"""
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Example 1:

    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

Example 3:

    Input: nums = [1]
    Output: [[1]]

Constraints:
    1. 1 <= nums.length <= 6
    2. -10 <= nums[i] <= 10
    3. All the integers of nums are unique.
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        32ms
        """
        if len(nums) == 1:
            return [nums]
        else:
            return [[nums[i]] + l for i in range(len(nums)) for l in self.permute(nums[:i] + nums[(i + 1):])]
