"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

    Input: [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s.
                 The maximum number of consecutive 1s is 3.

Note:
    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000
"""


class Solution:
    def findMaxConsecutiveOnes1(self, nums):
        res = 0
        i = 0
        while i < len(nums):
            j = 0
            while i + j < len(nums) and nums[i+j] == 1:
                j += 1
            
            res = max(res, j)
            if j > 0:
                i += j
            else:
                i += 1
        
        return res

    def findMaxConsecutiveOnes2(self, nums):    # lowest runtime
        return len(sorted(''.join(map(str, nums)).split('0'))[-1])

    def findMaxConsecutiveOnes3(self, nums):
        res = 0
        one_counter = 0
        for x in nums:
            if x:
                one_counter += 1
                res = max(res, one_counter)
            else:
                one_counter = 0

        return res
