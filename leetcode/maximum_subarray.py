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
        """dynamic programming"""
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max([nums[0], nums[1], nums[0] + nums[1]])
        
        sub_sums = [nums[0], nums[-1]]
        for i in range(1, len(nums) - 1):
            sub_sum = nums[i]
            sub_sums.append(sub_sum)
            j_left = i - 1
            j_right = i + 1
            while (j_left >= 0) and (j_right <= len(nums)-1):
                if nums[j_left] >= nums[j_right]:
                    sub_sum += nums[j_left]
                    sub_sums.append(sub_sum)
                    j_left += -1
                else:
                    sub_sum += nums[j_right]
                    sub_sums.append(sub_sum)
                    j_right += 1

        return max(sub_sums)

    def maxSubArray2(self, nums):
        """brutal solution, bad"""
        max_sum = sum(nums)
        for n_sub in range(1, len(nums)):
            for i in range(len(nums) - n_sub + 1):
                sub_sum = sum(nums[i:i+n_sub])
                if sub_sum > max_sum:
                    max_sum = sub_sum
        return max_sum
