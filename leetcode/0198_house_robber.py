"""
You are a professional robber planning to rob houses along a street. Each house has a certain 
amount of money stashed, the only constraint stopping you from robbing each of them is that 
adjacent houses have security system connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine 
the maximum amount of money you can rob tonight without alerting the police.

Example 1:

    Input: [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                Total amount you can rob = 1 + 3 = 4.

Example 2:

    Input: [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
                Total amount you can rob = 2 + 9 + 1 = 12.
"""


class Solution:
    def rob(self, nums):
        """Brute Force (Time Limit Exceeded)"""
        res = 0
        for i in range(len(nums)):
            res = max(res, nums[i] + self.rob(nums[i+2:]))
        return res

    def rob2(self, nums):
        """DP"""
        if not nums:
            return 0
        
        p_0 = nums[0]
        if len(nums) == 1:
            return p_0
            
        p_1 = max(p_0, nums[1])
        for i in range(2, len(nums)):
            p_2 = max(p_1, p_0 + nums[i])
            p_0 = p_1
            p_1 = p_2
        
        return p_1
