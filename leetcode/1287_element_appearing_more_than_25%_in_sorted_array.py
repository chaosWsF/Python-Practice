"""
Given an integer array sorted in non-decreasing order, there is exactly one integer 
in the array that occurs more than 25% of the time.

Return that integer.

Example 1:

    Input: arr = [1,2,2,6,6,6,6,7,10]
    Output: 6

Constraints:
    1. 1 <= arr.length <= 10^4
    2. 0 <= arr[i] <= 10^5
"""


class Solution:
    def findSpecialInteger(self, arr) -> int:
        k = len(arr) // 4
        for i in range(len(arr)):
            if arr[i] == arr[i+k]:
                return arr[i]
