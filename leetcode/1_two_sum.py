# =================================================================
# hash solution
# class Solution(object):
#     def twoSum(self, nums, target):
#         if len(nums) <= 1:
#             return False
#         buff_dict = {}
#         for i in range(len(nums)):
#             if nums[i] in buff_dict:
#                 return [buff_dict[nums[i]], i]
#             else:
#                 buff_dict[target - nums[i]] = i
# =================================================================

from itertools import combinations


class Solution:
    def twoSum(self, nums, target):
        result = []
        for i, j in combinations(list(range(len(nums))), 2):
            if nums[i] + nums[j] == target:
                result = [i, j]
                break
        
        return result


if __name__ == '__main__':
    input1 = [2, 7, 11, 15]
    input2 = 9
    sol = Solution()
    output = sol.twoSum(input1, input2)
    print(output)