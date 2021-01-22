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
        """
        Recursion
        Runtime: 40ms
        """
        candidates.sort()

        def helper(nums, t: int):
            res = []
            used = set()
            for i, x in enumerate(nums):
                if x not in used:
                    if x > t:
                        return res
                    elif x == t:
                        res.append([x])
                        return res
                    
                    used.add(x)
                    if i < len(nums) - 1:
                        next_comb = helper(nums[i+1:], t - x)
                        for l in next_comb:
                            res.append([x] + l)

            return res
        
        return helper(candidates, target)
