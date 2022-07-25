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
    def majorityElement(self, nums: List[int]) -> int:
        """
            Boyer-Moore Voting Algorithm (try to proof by contradiction)
            O(n), O(1)
        """
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
    
    def majorityElement0(self, nums: List[int]) -> int:
        """O(n), O(n)"""
        d = {}    # or collections.Counter
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        return max(d, key=d.get)
    
    def majorityElement1(self, nums):
        """
            O(nlgn), O(1) or O(n)
            160ms (99.45%) 14MB (100%)
        """
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement2(self, nums):
        """
            O(nlgn), O(lgn)
            Divide and Conquer (256ms 14.7MB)
        """
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
