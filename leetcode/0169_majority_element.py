"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊n/2⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

    Input: [3,2,3]
    Output: 3

Example 2:

    Input: [2,2,1,1,1,2,2]
    Output: 2
"""


class Solution:
    def majorityElement1(self, nums):
        """160ms (99.45%) 14MB (100%)"""
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement2(self, nums):
        """Divide and Conquer (256ms 14.7MB)"""
        def helper(left=0, right=None):
            if left == right:
                return nums[left]

            mid = (left + right) // 2
            major_left = helper(left, mid)
            major_right = helper(mid + 1, right)
            
            if major_left == major_right:
                return major_left
            
            left_count = 0
            right_count = 0
            for i in range(left, right + 1):
                num = nums[i]
                if num == major_left:
                    left_count += 1
                
                if num == major_right:
                    right_count += 1
            
            if left_count > right_count:
                return major_left
            else:
                return major_right
        
        return helper(0, len(nums) - 1)
