"""
We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position 
of the ith chip from position[i] to:

    position[i] + 2 or position[i] - 2 with cost = 0.
    position[i] + 1 or position[i] - 1 with cost = 1.

Return the minimum cost needed to move all the chips to the same position.

Example 1:

    https://assets.leetcode.com/uploads/2020/08/15/chips_e1.jpg

    Input: position = [1,2,3]
    Output: 1
    Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
                 Second step: Move the chip at position 2 to position 1 with cost = 1.
                 Total cost is 1.

Example 2:

    https://assets.leetcode.com/uploads/2020/08/15/chip_e2.jpg

    Input: position = [2,2,2,3,3]
    Output: 2
    Explanation: We can move the two chips at poistion 3 to position 2. Each move has cost = 1. 
                 The total cost = 2.

Example 3:

    Input: position = [1,1000000000]
    Output: 1

Constraints:
    1. 1 <= position.length <= 100
    2. 1 <= position[i] <= 10^9
"""

from collections import Counter


class Solution:
    def minCostToMoveChips(self, position) -> int:    # faster
        cnt = Counter([pi % 2 for pi in position])
        return min(cnt.values()) if len(cnt) > 1 else 0

    def minCostToMoveChips2(self, position) -> int:
        n_odd = n_even = 0
        for pi in position:
            if pi % 2:
                n_odd += 1
            else:
                n_even += 1
        
        return min(n_odd, n_even)
