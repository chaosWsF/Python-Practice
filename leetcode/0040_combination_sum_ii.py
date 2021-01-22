"""
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output: 
        [
        [1,1,6],
        [1,2,5],
        [1,7],
        [2,6]
        ]

Example 2:

    Input: candidates = [2,5,2,1,2], target = 5
    Output: 
        [
        [1,2,2],
        [5]
        ]

Constraints:
    1. 1 <= candidates.length <= 100
    2. 1 <= candidates[i] <= 50
    3. 1 <= target <= 30
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def helper(nums, t: int):
            if len(nums) == 1:
                if t % nums[0] == 0:
                    return [nums * (t // nums[0])]
                else:
                    return []
            
            res = []
            for i, x in enumerate(nums):
                if x > t:
                    return res
                elif x == t:
                    res.append([x])
                    return res
                
                next_comb = helper(nums[i:], t - x)
                for l in next_comb:
                    res.append([x] + l)

            return res
        
        return helper(candidates, target)
