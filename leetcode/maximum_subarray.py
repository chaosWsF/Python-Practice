"""
Given an integer array nums, find the contiguous subarray (containing at 
least one number) which has the largest sum and return its sum.

Example:

    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
    If you have figured out the O(n) solution, try coding another 
    solution using the divide and conquer approach, which is more 
    subtle.
"""


class Solution:
    def maxSubArray(self, nums):
        """the divide and conquer approach"""
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1], nums[0] + nums[1])
        
        if len(nums) % 2 == 0:
            nums.insert(len(nums) // 2, 0)
        
        max_sum = max(nums[0], nums[-1])
        i = (len(nums) - 1) // 2
        while 0 < i < len(nums) - 1:
            i_left = i - 1
            i_right = i + 1
            while (i_left >= 0) and (i_right <= len(nums)-1):
                if nums[i_left] >= nums[i_right]:
                    i_left -= 1
                else:
                    i_right += 1

            sub_array = nums[i_left+1:i_right]
            max_sum = max(max_sum, self.maxSubArray(sub_array))

            sub_sum = sum(sub_array)
            if i_left < 0:
                nums = [sub_sum] + nums[i_right:]
            else:
                nums = nums[:i_left+1] + [sub_sum]
            max_sum = max(max_sum, self.maxSubArray(nums))

            i = (len(nums) - 1) // 2

        return max_sum

    def maxSubArray2(self, nums):
        """brutal solution, bad"""
        max_sum = sum(nums)
        for n_sub in range(1, len(nums)):
            for i in range(len(nums) - n_sub + 1):
                sub_sum = sum(nums[i:i+n_sub])
                if sub_sum > max_sum:
                    max_sum = sub_sum
        return max_sum
