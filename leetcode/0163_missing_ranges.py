"""
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return [“2”, “4->49”, “51->74”, “76->99”].
"""


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        """
        O(n), O(n)
        """
        def helper(low: int, high: int) -> str:
            return str(low) + '->' + str(high) if low != high else str(low)
        
        if len(nums) == 0:
            return [helper(lower, upper)]

        res = []
        if nums[0] > lower:
            res.append(helper(lower, nums[0]-1))
        
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                res.append(helper(nums[i]+1, nums[i+1]-1))

        if nums[-1] < upper:
            res.append(helper(nums[-1]+1, upper))
        
        return res
