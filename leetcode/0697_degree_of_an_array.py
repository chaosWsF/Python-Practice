"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum 
frequency of any one of its elements. Your task is to find the smallest possible length of a (contiguous) 
subarray of nums, that has the same degree as nums.

Example 1:

    Input: [1, 2, 2, 3, 1]
    Output: 2
    Explanation: The input array has a degree of 2 because both elements 1 and 2 appear twice. Of 
                 the subarrays that have the same degree: [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], 
                 [1, 2, 2], [2, 2, 3], [2, 2]. The shortest length is 2. So return 2.

Example 2:

    Input: [1, 2, 2, 3, 1, 4, 2]
    Output: 6

Note:
    nums.length will be between 1 and 50,000.
    nums[i] will be an integer between 0 and 49,999.
"""


class Solution:
    def findShortestSubArray(self, nums):    # 224ms
        d = {}
        for i, x in enumerate(nums):
            if x in d:
                d[x].append(i)
            else:
                d[x] = [i]

        det = []
        for val in d.values():
            n = len(val)
            if n == 1:
                det.append((-1, 1))
            else:
                det.append((-n, val[-1] - val[0] + 1))
        
        return min(det)[1]
