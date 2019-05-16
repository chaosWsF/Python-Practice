from itertools import combinations


class Solution:
    def twoSum(self, nums, target):
        result = []
        for i, j in combinations(list(range(len(nums))), 2):
            if nums[i] + nums[j] == target:
                result = [i, j]
                break
        
        return result


# =================================================================
# 24ms solution
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         map: Dict[int] = {}
#         for index, element in enumerate(nums):
#             if element in map:
#                 return (map[element], index)
#             map[target - element] = index
# =================================================================

if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
