"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

Example 2:

    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:

    Input: intervals = [], newInterval = [5,7]
    Output: [[5,7]]

Example 4:

    Input: intervals = [[1,5]], newInterval = [2,3]
    Output: [[1,5]]

Example 5:

    Input: intervals = [[1,5]], newInterval = [2,7]
    Output: [[1,7]]

Constraints:
    1. 0 <= intervals.length <= 10**4
    2. intervals[i].length == 2
    3. 0 <= intervals[i][0] <= intervals[i][1] <= 10**5
    4. intervals is sorted by intervals[i][0] in ascending order.
    5. newInterval.length == 2
    6. 0 <= newInterval[0] <= newInterval[1] <= 10**5
"""


import bisect


class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        
        a, b = newInterval
        i = bisect.bisect(intervals, newInterval)

        l = i - 1
        while l >= 0 and intervals[l][1] >= a:
            newInterval[1] = max(b, intervals[l][1])
            l -= 1
        
        r = i
        while r < len(intervals) and intervals[r][0] <= b:
            r += 1

        if l < i - 1:
            newInterval[0] = intervals[l+1][0]

        if r > i:
            newInterval[1] = intervals[r-1][1]

        return intervals[:l+1] + [newInterval] + intervals[r:]
