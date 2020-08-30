"""
Given an array of 4 digits, return the largest 24 hour time that can be made. The smallest 24 hour time is 00:00, 
and the largest is 23:59. Starting from 00:00, a time is larger if more time has elapsed since midnight. Return 
the answer as a string of length 5. If no valid time can be made, return an empty string.

Example 1:

    Input: [1,2,3,4]
    Output: "23:41"

Example 2:

    Input: [5,5,5,5]
    Output: ""

Note:
    1. A.length == 4
    2. 0 <= A[i] <= 9
"""

from itertools import permutations


class Solution:
    def largestTimeFromDigits2(self, A):
        max_minutes = -1
        for a, b, c, d in permutations(A):
            hour = a * 10 + b
            minute = c * 10 + d
            if hour < 24 and minute < 60:
                max_minutes = max(60 * hour + minute, max_minutes)
        
        if max_minutes == -1:
            return ''
        else:
            return f'{max_minutes // 60:02}:{max_minutes % 60:02}'
