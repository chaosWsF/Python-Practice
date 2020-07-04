"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed). Once you pay the 
cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, 
and you can either start from the step with index 0, or the step with index 1.

Example 1:

    Input: cost = [10, 15, 20]
    Output: 15
    Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:

    Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    Output: 6
    Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:
    1. cost will have a length in the range [2, 1000].
    2. Every cost[i] will be an integer in the range [0, 999].
"""


class Solution:
    def minCostClimbingStairs1(self, cost):
        """dynamic programming (backward)"""
        final_cost = []
        cost.reverse()
        for i in range(len(cost)):
            if i < 2:
                final_cost.append(cost[i])
            else:
                final_cost.append(cost[i] + min(final_cost[i-1], final_cost[i-2]))
        
        return min(final_cost[-2:])

    def minCostClimbingStairs2(self, cost):
        """forward solution"""
        f0, f1 = cost[0:2]
        for i in range(2, len(cost)):
            cur = cost[i] + min(f0, f1)
            f0, f1 = f1, cur
        
        return min(f0, f1)
