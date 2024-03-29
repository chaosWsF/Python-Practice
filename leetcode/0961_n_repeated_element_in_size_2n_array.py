"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is 
repeated N times. Return the element repeated N times.

Example 1:

    Input: [1,2,3,3]
    Output: 3

Example 2:

    Input: [2,1,2,5,3,2]
    Output: 2

Example 3:

    Input: [5,1,5,2,5,3,5,4]
    Output: 5

Note:
    1. 4 <= A.length <= 10000
    2. 0 <= A[i] < 10000
    3. A.length is even
"""


class Solution:
    def repeatedNTimes(self, A):
        d = set()
        for x in A:
            if x in d:
                return x
            else:
                d.add(x)

    def repeatedNTimes2(self, A):
        return int((sum(A) - sum(set(A))) / (len(A) / 2 - 1))
