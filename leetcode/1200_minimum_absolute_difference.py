"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two 
elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

    a, b are from arr
    a < b
    b - a equals to the minimum absolute difference of any two elements in arr

Example 1:

    Input: arr = [4,2,1,3]
    Output: [[1,2],[2,3],[3,4]]
    Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Example 2:

    Input: arr = [1,3,6,10,15]
    Output: [[1,3]]

Example 3:

    Input: arr = [3,8,-10,23,19,-4,-14,27]
    Output: [[-14,-10],[19,23],[23,27]] 

Constraints:
    1. 2 <= arr.length <= 10^5
    2. -10^6 <= arr[i] <= 10^6
"""


class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        dis_min = min(arr[i] - arr[i-1] for i in range(1, len(arr)))
        return [[x, y] for x, y in zip(arr, arr[1:]) if y - x == dis_min]

    def minimumAbsDifference2(self, arr):    # faster
        arr.sort()
        dis_min, res = 2e6, []
        for x, y in zip(arr, arr[1:]):
            dis = y - x
            if dis < dis_min:
                dis_min, res = dis, [[x, y]]
            elif dis == dis_min:
                res.append([x, y])
        
        return res
