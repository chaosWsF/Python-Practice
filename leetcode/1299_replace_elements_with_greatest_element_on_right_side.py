"""
Given an array arr, replace every element in that array with the greatest element 
among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:

    Input: arr = [17,18,5,4,6,1]
    Output: [18,6,6,6,1,-1]

Constraints:
    1. 1 <= arr.length <= 10^4
    2. 1 <= arr[i] <= 10^5
"""


class Solution:
    def replaceElements(self, arr):
        res = [-1]
        max_num = float('-inf')
        while len(arr) > 1:
            max_num = max(arr.pop(), max_num)
            res.append(max_num)
        
        return res[::-1]

    def replaceElements2(self, arr):
        max_num = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            tmp = max_num
            max_num = max(max_num, arr[i])
            arr[i] = tmp
        
        return arr
