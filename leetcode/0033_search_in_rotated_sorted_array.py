"""
You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become 
[4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

Example 1:

    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

Example 3:

    Input: nums = [1], target = 0
    Output: -1

Constraints:
    1. 1 <= nums.length <= 5000
    2. -10^4 <= nums[i] <= 10^4
    3. All values of nums are unique.
    4. nums is guaranteed to be rotated at some pivot.
    5. -10^4 <= target <= 10^4
"""


class Solution:
    def search(self, nums, target: int) -> int:
        a, b = 0, len(nums) - 1
        while a <= b:
            mid = (a + b) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[a]:
                if nums[a] <= target < nums[mid]:
                    b = mid - 1
                else:
                    a = mid + 1
            else:
                if nums[mid] < target <= nums[b]:
                    a = mid + 1
                else:
                    b = mid - 1
        
        return -1
    
    # def search2(self, nums, target: int) -> int:
    #     """
    #     Slow, by two steps
    #     """
    #     def helper(i: int, j: int) -> int:
    #         """
    #         Given starting and ending indices, apply binary search to the ascending sub-list.
    #         """
    #         while i <= j:
    #             if target < nums[i] or target > nums[j]:
    #                 return -1
    #             elif target == nums[i]:
    #                 return i
    #             elif target == nums[j]:
    #                 return j

    #             mid = (i + j) // 2
    #             if nums[mid] == target:
    #                 return mid
    #             elif nums[mid] > target:
    #                 j = mid - 1
    #             else:
    #                 i = mid + 1

    #         return -1

    #     if nums[0] <= nums[-1]:
    #         return helper(0, len(nums)-1)
        
    #     a, b = 0, len(nums) - 1
    #     while a < b:
    #         c = (a + b) // 2
    #         if nums[c] < nums[a]:
    #             b = c
    #         elif nums[c] > nums[a]:
    #             a = c
    #         else:
    #             break

    #     if target >= nums[0]:
    #         return helper(0, a)
    #     else:
    #         return helper(a+1, len(nums)-1)
