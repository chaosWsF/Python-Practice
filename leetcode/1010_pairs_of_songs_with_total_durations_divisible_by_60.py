"""
In a list of songs, the i-th song has a duration of time[i] seconds. Return the number of 
pairs of songs for which their total duration in seconds is divisible by 60. Formally, we 
want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

Example 1:

    Input: [30,20,150,100,40]
    Output: 3
    Explanation: Three pairs have a total duration divisible by 60:
        (time[0] = 30, time[2] = 150): total duration 180
        (time[1] = 20, time[3] = 100): total duration 120
        (time[1] = 20, time[4] = 40): total duration 60

Example 2:

    Input: [60,60,60]
    Output: 3
    Explanation: All three pairs have a total duration of 120, which is divisible by 60.

Note:
    1. 1 <= time.length <= 60000
    2. 1 <= time[i] <= 500
"""


from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time) -> int:    # 212ms
        d = defaultdict(int)
        for t in time:
            d[t % 60] += 1
        
        res = (d[0] * (d[0] - 1) + d[30] * (d[30] - 1)) / 2 + sum(d[i]*d[60-i] for i in range(1, 30))
        return int(res)
