"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements 
that don't appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:

    Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
    Output: [2,2,2,1,4,3,3,9,6,7,19]

Constraints:
    1. arr1.length, arr2.length <= 1000
    2. 0 <= arr1[i], arr2[i] <= 1000
    3. Each arr2[i] is distinct.
    4. Each arr2[i] is in arr1.
"""

from collections import Counter


class Solution:
    def relativeSortArray(self, arr1, arr2):    # 32ms
        arr2_map = dict(zip(arr2, range(len(arr2))))
        return (
            sorted([x for x in arr1 if x in arr2_map], key=arr2_map.get) + 
            sorted([x for x in arr1 if x not in arr2_map])
        )
    
    def relativeSortArray2(self, arr1, arr2):    # 24ms
        arr1_cnt, arr2_set = Counter(arr1), set(arr2)
        return (
            [x for x in arr2 for _ in range(arr1_cnt[x])] + 
            sorted([x for x in arr1 if x not in arr2_set])
        )
